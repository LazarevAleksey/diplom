import serial.tools.list_ports
import backend.backend_serial as ser
import backend.backend_parser as parser

def print_coms_() -> None:
    ports = serial.tools.list_ports.comports()
    for port, desc, hwid in sorted(ports):
        print(f'{port} {desc} {hwid} was find!')

print_coms_()

