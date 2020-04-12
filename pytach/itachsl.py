"""
The itach driver.

"""

import logging

import pytach.itach

_LOGGER = logging.getLogger(__name__)

class iTachSL(pytach.itach.iTach):
  def __init__(self, config, persist=False):
    pytach.itach.iTach.__init__(self,config,persist)
    _LOGGER.debug(f"iTachSL '{self.name} ({self.host}:{self.port})' loaded...")

  def send(self, module, port, data):
    _LOGGER.debug(f"iTachSL '{self.name} ({self.host}:{self.port})' sending {repr(data)}...")
    self.socketSend(data)
