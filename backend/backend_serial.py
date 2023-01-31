# BUK use RS-485 interfese to interact with user.
# We use RS-485 -> COM driver to switch from RS to USB-COM
# To interact with desctop we use pyserial
# Here is code to transmit and resive messeges


# TODO : ADD generator for commands in send_command()
#      : ADD autodetection for COM
import backend_parser as parser
import serial as ser
PORT = 'COM3' 
BAUD = 38400
BYTE_SIZE = 8
PARITY = 'N'
STOP_BITS = 1
ATTEMPTS = 10


def send_command(str):
    with ser.Serial(PORT, BAUD, BYTE_SIZE, PARITY, STOP_BITS, timeout=1) as port:
        for i in range(ATTEMPTS):
            if port.write(str):
                line = port.readline()
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
