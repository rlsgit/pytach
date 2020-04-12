"""
The itach driver.

"""

import logging

import pytach.const as const

_LOGGER = logging.getLogger(__name__)

class iTachDevice:
  def __init__(self, itach, config:dict):
    self.itach = itach
    self.name = config.get(const.CONF_NAME)
    self.module = config.get(const.CONF_MODULE,const.DEFAULT_MODULE)
    self.port = config.get(const.CONF_PORT)

    self.commands = {}
    if const.CONF_COMMANDS in config:
      for command in config.get(const.CONF_COMMANDS):
        self.addCommand(command)

    _LOGGER.debug(f"iTachDevice '{self.name}' loaded...")
    
  def toString(self) -> str:
    ret = f'{{ "{const.CONF_NAME}":"{self.name}", "{const.CONF_MODULE}":"{self.port}", "{const.CONF_PORT}": {self.port}'
    return ret

  def addCommand(self,command:dict) -> None:
    self.commands.update({ command.get(const.CONF_NAME): command.get(const.CONF_DATA) })

  def removeCommand(self,name:str) -> None:
    self.commands.pop(name)

  def sendCommand(self,command) -> None:
    if command in self.commands:
      data = self.commands[command]
      return self.itach.send(self.module,self.port,data)
      
    _LOGGER.error(f"iTachDevice '{self.name}' command '{command}' not found!")
    return False
