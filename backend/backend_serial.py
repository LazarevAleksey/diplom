# We use RS-485 -> COM driver to switch from RS to USB-COM
# BUK use RS-485 interfese to interact with user.
# To interact with desctop we use pyserial
# Here is code to transmit and resive messeges
import time
from . import backend_logs as logs
from . import backend_parser as parser
import serial
import serial.tools.list_ports
PORT = 'default'
BAUD = 38400
BYTE_SIZE = 8
PARITY = 'N'
STOP_BITS = 1
ATTEMPTS = 10
BUK_DEV = 'Arduino'

# Check if there available com ports with BUK_NAME in it


def avilable_com() -> str:
    ports = serial.tools.list_ports.comports()
    for port, desc, hwid in sorted(ports):
        if BUK_DEV in desc:
            return str(port)
    return '0'


def commands_generator(buk_num: str, command: str) -> str:
    return 'bmk:' + buk_num + ":" + command

# Send the command and save buk answer in get_status_params_dict_m[]


def send_command(buk_num: str, command: str) -> bool | dict[str, str]:
    str_command = str.encode(commands_generator(buk_num, command))
    if PORT:
        with serial.Serial(PORT, BAUD, BYTE_SIZE, PARITY, STOP_BITS, timeout=0.5) as port:
            for i in range(ATTEMPTS):
                print(str_command)
                if port.write(str_command):
                    line = port.readline()
                    dict_m = parser.parse_com_str(line, command)
                    if dict_m:
                        logs.success_parsing_log(line)
                        return dict_m
                    else:
                        logs.error_parsing_log(line)
                        continue
                else:
                    logs.error_write_log(str_command.decode())
                    continue
            return False
    logs.error_open_port_log(PORT)
    return False
