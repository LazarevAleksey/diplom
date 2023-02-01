# BUK use RS-485 interfese to interact with user.
# We use RS-485 -> COM driver to switch from RS to USB-COM
# To interact with desctop we use pyserial
# Here is code to transmit and resive messeges


import backend_parser as parser
import serial as ser
import serial.tools.list_ports
PORT = 'default'
BAUD = 9600
BYTE_SIZE = 8
PARITY = 'N'
STOP_BITS = 1
ATTEMPTS = 10
BUK_NAME = 'Arduino'


def avilable_com() -> str:
    ports = serial.tools.list_ports.comports()
    for port, desc, hwid in sorted(ports):
        if BUK_NAME in desc:
            return port


def commands_generator(buk_num: str, command: str) -> str:
    return 'bmk:' + buk_num + ":" + command


def send_command(buk_num: str, command: str) -> bool:
    str_command = str.encode(commands_generator(buk_num, command))
    PORT = avilable_com()
    with ser.Serial(PORT, BAUD, BYTE_SIZE, PARITY, STOP_BITS, timeout=1) as port:
        for i in range(ATTEMPTS):
            if port.write(str_command):
                line = port.readline()
                print(line)
                if parser.parse_com_str(line, "get_status"):
                    # logs
                    return True
                else:
                    # logs
                    continue
            else:
                # logs
                continue
        return False
