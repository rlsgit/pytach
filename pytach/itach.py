"""
The itach driver.

"""

from __future__ import annotations
import logging
import socket
from typing import Callable

import pytach.const as const
from pytach.discovery import iTachDiscover
from pytach.itachdevice import iTachDevice

_LOGGER = logging.getLogger(__name__)

class iTach:
  @classmethod
  def discover(cls, callback:Callable[[dict],None], timeout:int = 0) -> None:
    return iTachDiscover(callback,timeout)
    
  @classmethod
  def createHost(cls, config, persist=False) -> iTach:
    type = config.get(const.CONF_TYPE)
    if type == const.TYPE_IR:
      import pytach.itachir
      return pytach.itachir.iTachIR(config,persist)
    elif type == const.TYPE_SL:
      import pytach.itachsl
      return pytach.itachsl.iTachSL(config,persist)

    _LOGGER.error(f"Invalid device type ({type})!")
    return None

  def __init__(self, config, persist=False):
    self.config = config
    self.name = config.get(const.CONF_NAME)
    self.host = config.get(const.CONF_HOST)
    self.type = config.get(const.CONF_TYPE)
    self.port = config.get(const.CONF_PORT, const.DEFAULT_IR_PORT if self.type == const.TYPE_IR else const.DEFAULT_SERIAL_PORT)
    self.persist = persist
    
    self.devices = {}
    if const.CONF_DEVICES in config:
      for device in config.get(const.CONF_DEVICES):
        self.addDevice(device)

    _LOGGER.debug(f"iTach created: {self.host}:{self.port}")

    self.sock = None
    if persist:
      _LOGGER.debug(f"iTach '{self.name}' is persistent...")
      self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      self.sock.settimeout(const.CONNECT_TIMEOUT)
      self.sock.connect((self.host, self.port))
        
  def toString(self):
    ret = f'{{ "{const.CONF_NAME}":"{self.name}", "{const.CONF_HOST}":"{self.host}", "{const.CONF_DEVICES}": {{'
    for name,device in self.devices.items():
      ret += f' "{name}":"{device.toString()}",'
    ret += " }"
    return ret

  def addDevice(self, config) -> iTachDevice:
    ret = iTachDevice(self,config)
    self.devices.update({ config.get(const.CONF_NAME): ret })
    return ret

  def removeDevice(self, name) -> None:
    self.devices.pop(name, None)

  def getDevice(self,name):
    if name in self.devices:
      return self.devices[name]
      
    return None

  def socketSend(self,data):
    closeSock = False
    if self.sock is None:
      self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      self.sock.settimeout(const.CONNECT_TIMEOUT)
      self.sock.connect((self.host, self.port))
      closeSock = True

    response = None
    try:
        _LOGGER.debug(f"sendSocket sending '{data}'...")
        self.sock.sendall(data.encode())
        response = self.sock.recv(const.BUFFER_SIZE)
        _LOGGER.debug(f"sendSocket received '{response}'...")
    except socket.error as error:
        _LOGGER.error(f"sendSocket error: '{str(error)}'...")

    if closeSock:
      self.sock.close()
      self.sock = None

    return response
