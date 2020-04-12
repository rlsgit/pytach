"""
The itach driver.

"""

import logging

from pytach.itach import iTach

_LOGGER = logging.getLogger(__name__)

class iTachIR(iTach):
  def __init__(self, config, persist=False):
    iTach.__init__(self,config,persist)
    _LOGGER.debug(f"iTachIR '{self.name} ({self.host}:{self.port})' loaded...")
    
  def prontoToGC(self, module, port, data,count=1):
    data = data.strip()
    dataL = []
    for x in data.split(" "):
      dataL.append(int(x,16))

    if (len(dataL) < 4) or (dataL[0] != 0) or ((dataL[2] + dataL[3]) * 2 != (len(dataL) - 4)):
      _LOGGER.error(f"Invalid PRONTO data '{data}'!")
      return False

    frequency = int((1000000 / (float(dataL[1]) * 0.241246)) / 1000) * 1000
    offset = dataL[2] if count > 1 else 1
    
    result = f"sendir,{module}:{port},1,{frequency},{count},{offset}"

    x=4
    while x < len(dataL):
      result += f",{str(dataL[x])}"
      x += 1

    result += "\r"
    _LOGGER.debug(f"PRONTO to GC: '{result}'!")
    
    return result
  
  def send(self, module, port, data):
    gcData = data
    if not gcData.startswith("sendir"):
      gcData = self.prontoToGC(module,port,data)

    if not gcData.endswith("\r"):
      gcData += "\r"
    
    _LOGGER.debug(f"iTachIR '{self.name} ({self.host}:{self.port})' sending '{gcData}'...")
    response = self.socketSend(gcData)

    return response.decode("utf-8")
