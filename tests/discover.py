"""
The itach driver discovery test function.

"""

import logging
import asyncio

from pytach import iTach

logging.basicConfig()
_LOGGER = logging.getLogger(__name__)
_LOGGER.setLevel(logging.DEBUG)

_LOGGER.debug("pytach discovery test starting...")

itachs = {}

def gotHost(data:dict) -> None:
  if data["host"] in itachs:
    _LOGGER.info("Skipping existing host %s", data["host"])
  else:
    h = itachs[data["host"]] = iTach.createHost(data)
    _LOGGER.info("Added iTach %s", h.toString())

loop = asyncio.get_event_loop()
loop.run_until_complete(iTach.discover(gotHost,10))
