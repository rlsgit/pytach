"""
The itach driver test function.

"""

import logging
import logging.config
import time

from pytach import iTach
from pytach import const

logging.config.fileConfig("logging.ini",disable_existing_loggers=False)
_LOGGER = logging.getLogger(__name__)

_LOGGER.info("iTach test starting...")

configIR = {
  "type": const.TYPE_IR,
  "name": "ip2ir01",
  "host": "192.168.1.32",
  # "devices": [
  #   {
  #     "name": "proj",
  #     "port": 2,
  #     "commands": [
  #       {
  #         "name": "on",
  #         "data": "0000 006C 0000 0022 0157 00AB 0015 0040 0015 0040 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0040 0015 0040 0015 0015 0015 0040 0015 0015 0015 0040 0015 0015 0015 0040 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0040 0015 0015 0015 0015 0015 0040 0015 0040 0015 0040 0015 0040 0015 0040 0015 0015 0015 0040 0015 0040 0015 0015 0015 060A"
  #       },
  #       {
  #         "name": "off",
  #         "data": "0000 006C 0000 0022 0157 00AB 0015 0040 0015 0040 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0040 0015 0040 0015 0015 0015 0040 0015 0015 0015 0040 0015 0015 0015 0040 0015 0015 0015 0040 0015 0015 0015 0015 0015 0015 0015 0040 0015 0015 0015 0015 0015 0040 0015 0015 0015 0040 0015 0040 0015 0040 0015 0015 0015 0040 0015 0040 0015 0015 0015 060A"
  #       }
  #     ]
  #   }
  # ]
}

itach = iTach.createHost(configIR)
_LOGGER.info("iTach created: %s", itach.toString())
itach.addDevice({ const.CONF_NAME: "projector", const.CONF_PORT: "2" })
_LOGGER.info("iTach with projector: %s", itach.toString())
itach.removeDevice("projector")
_LOGGER.info("iTach without projector: %s", itach.toString())
projector = itach.addDevice({ const.CONF_NAME: "projector", const.CONF_PORT: "2" })
_LOGGER.info("iTach with projector: %s", itach.toString())
projector.addCommand({ const.CONF_NAME: "blank", const.CONF_DATA: "0000 006C 0000 0022 0157 00AB 0015 0040 0015 0040 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0040 0015 0040 0015 0015 0015 0040 0015 0015 0015 0040 0015 0015 0015 0040 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0040 0015 0015 0015 0015 0015 0040 0015 0040 0015 0040 0015 0040 0015 0040 0015 0015 0015 0040 0015 0040 0015 0015 0015 060A" })
response = projector.sendCommand("blank")
_LOGGER.info("projector on returned: %s", response)


# print(prontoToGC(1,1,"0000 006C 0000 0022 0157 00AB 0015 0040 0015 0040 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0040 0015 0040 0015 0015 0015 0040 0015 0015 0015 0040 0015 0015 0015 0040 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0040 0015 0015 0015 0015 0015 0040 0015 0040 0015 0040 0015 0040 0015 0040 0015 0015 0015 0040 0015 0040 0015 0015 0015 060A"))
# print(prontoToGC(1,1,"0000 006C 0000 0022 0157 00AB 0015 0040 0015 0040 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0040 0015 0040 0015 0015 0015 0040 0015 0015 0015 0040 0015 0015 0015 0040 0015 0015 0015 0040 0015 0015 0015 0015 0015 0015 0015 0040 0015 0015 0015 0015 0015 0040 0015 0015 0015 0040 0015 0040 0015 0040 0015 0015 0015 0040 0015 0040 0015 0015 0015 060A"))

# configIR = {
#   "type": TYPE_IR,
#   "name": "ip2ir01",
#   "host": "192.168.1.32",
#   "devices": [
#     {
#       "name": "proj",
#       "port": 2,
#       "commands": [
#         {
#           "name": "on",
#           "data": "0000 006C 0000 0022 0157 00AB 0015 0040 0015 0040 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0040 0015 0040 0015 0015 0015 0040 0015 0015 0015 0040 0015 0015 0015 0040 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0040 0015 0015 0015 0015 0015 0040 0015 0040 0015 0040 0015 0040 0015 0040 0015 0015 0015 0040 0015 0040 0015 0015 0015 060A"
#         },
#         {
#           "name": "off",
#           "data": "0000 006C 0000 0022 0157 00AB 0015 0040 0015 0040 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0040 0015 0040 0015 0015 0015 0040 0015 0015 0015 0040 0015 0015 0015 0040 0015 0015 0015 0040 0015 0015 0015 0015 0015 0015 0015 0040 0015 0015 0015 0015 0015 0040 0015 0015 0015 0040 0015 0040 0015 0040 0015 0015 0015 0040 0015 0040 0015 0015 0015 060A"
#         }
#       ]
#     }
#   ]
# }
# itachIR = iTach.createHost(configIR)
# print(itachIR.getDevice("proj").sendData("sendir,1:1,1,38000,1,1,343,171,21,64,21,64,21,21,21,21,21,21,21,21,21,21,21,64,21,64,21,21,21,64,21,21,21,64,21,21,21,64,21,21,21,21,21,21,21,21,21,21,21,64,21,21,21,21,21,64,21,64,21,64,21,64,21,64,21,21,21,64,21,64,21,21,21,1546"))

# configSL = {
#   "type": TYPE_SL,
#   "name": "ip2sl01",
#   "host": "192.168.1.31",
#   "devices": [
#     {
#       "name": "mca",
#       "port": 1,
#       "commands": [
#         {
#           "name": "zone1_status",
#           "data": "?11\r"
#         },
#         {
#           "name": "zone1_on",
#           "data": "<11PR01\r"
#         },
#         {
#           "name": "zone1_off",
#           "data": "<11PR00\r"
#         }
#       ]
#     }
#   ]
# }
# itachSL = iTach.createHost(configSL)

#print(itachSL.getDevice("mca").sendCommand("zone1_status"))
#print(itachSL.getDevice("mca").sendCommand("zone1_on"))
#time.sleep(5)
#print(itachSL.getDevice("mca").sendCommand("zone1_off"))
#print(itachSL.getDevice("mca").sendCommand("zone1_status"))

