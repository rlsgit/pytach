"""
The itach driver discovery functions.

"""

import logging
import socket
import struct
import time
import sys
from typing import Callable

import pytach.const

_LOGGER = logging.getLogger(__name__)

async def iTachDiscover(callback:Callable[[dict],None], timeout:int = 0) -> None:
  _LOGGER.debug("Starting discovery...")

  # Setup the initial socket
  sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)

  # Allow reuse
  sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

  # Bind
  sock.bind(('',pytach.const.UDP_PORT))

  # Let the router/switch know that we want to recieve traffic
  group = socket.inet_aton(pytach.const.UDP_IP)
  mreq = struct.pack('4sL', group, socket.INADDR_ANY)
  sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

  # Endless loop of traffic
  stoptime = False
  if timeout:
    stoptime = time.time() + timeout

  def decodeMessage(data):
    ret = False
    try:
      tokens = data.split("<-")
      for tok in tokens:
        pairs = tok.split("=")
        if len(pairs) == 2:
          name = pairs[0].strip()
          val = pairs[1].strip()[:-1]

          if not ret:
            ret = {}

          ret[name] = val
    except:
      _LOGGER.warn("Exception decoding discovery message: %s", sys.exc_info())

    return ret

  while True:
    try:
      _LOGGER.debug("Wating for message...")
      data, address = sock.recvfrom(1024)
      _LOGGER.debug("Received %s bytes from %s: %s", len(data), address, data)
      
      ret = decodeMessage(data.decode("utf-8"))
      if ret:
        _LOGGER.debug("Decoded discovery: %s",ret)

        typ = False

        if ret["Model"] == "iTachIP2IR":
          typ = pytach.const.TYPE_IR
        elif ret["Model"] == "iTachIP2SL":
          typ = pytach.const.TYPE_SL

        if typ:
          data = {
            pytach.const.CONF_NAME: ret["UUID"],
            pytach.const.CONF_HOST: address[0],
            pytach.const.CONF_TYPE: typ,
            "discovery": ret
          }
          if callable(callback):
            callback(data)

    except:
      _LOGGER.warn("Exception in discovery: %s", sys.exc_info(), exc_info=True)

    if stoptime:
      if time.time() > stoptime:
        _LOGGER.debug("Discovery timeout reached...")
        break
