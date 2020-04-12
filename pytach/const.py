"""
Constants for the itach driver.
"""

ERRORCODES = {
  '001': 'Invalid command. Command not found.',
  '002': 'Invalid module address (does not exist).',
  '003': 'Invalid connector address (does not exist).',
  '004': 'Invalid ID value.',
  '005': 'Invalid frequency value.',
  '006': 'Invalid repeat value.',
  '007': 'Invalid offset value.',
  '008': 'Invalid pulse count.',
  '009': 'Invalid pulse data.',
  '010': 'Uneven amount of <on|off> statements.',
  '011': 'No carriage return found.',
  '012': 'Repeat count exceeded.',
  '013': 'IR command sent to input connector.',
  '014': 'Blaster command sent to non-blaster connector.',
  '015': 'No carriage return before buffer full.',
  '016': 'No carriage return.',
  '017': 'Bad command syntax.',
  '018': 'Sensor command sent to non-input connector.',
  '019': 'Repeated IR transmission failure.',
  '020': 'Above designated IR <on|off> pair limit.',
  '021': 'Symbol odd boundary.',
  '022': 'Undefined symbol.',
  '023': 'Unknown option.',
  '024': 'Invalid baud rate setting.',
  '025': 'Invalid flow control setting.',
  '026': 'Invalid parity setting.',
  '027': 'Settings are locked'
}

DELAY_BETWEEN_COMMANDS = 100
DEFAULT_IR_PORT = 4998
DEFAULT_SERIAL_PORT = 4999
DEFAULT_TIMEOUT = 2000
DEFAULT_CONCURRENCY = 1
DEFAULT_MODULE = 1

TYPE_IR = "ir"
TYPE_SL = "sl"

CONNECT_TIMEOUT = 5
BUFFER_SIZE = 4096

CONF_HOSTS = "hosts"
CONF_NAME = "name"
CONF_HOST = "host"
CONF_TYPE = "type"
CONF_MODULE = "module"
CONF_PORT = "port"
CONF_DEVICES = "devices"
CONF_COMMANDS = "commands"
CONF_DATA = "data"

# Discovery
UDP_IP = '239.255.250.250'
UDP_PORT = 9131
