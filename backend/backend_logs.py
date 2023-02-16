# Here some logs func to registr some strange behavior


import time


def current_time() -> str:
    t = time.localtime()
    cr_t = time.strftime("%H : %M ; % S", t)
    return cr_t


def success_parsing_log(str: str) -> None:
    with open('logs.txt', 'a') as f:
        f.write(f"{current_time()} Success parsing the input string: {str}\n")


def error_parsing_log(str: str) -> None:
    with open('logs.txt', 'a') as f:
        f.write(f"{current_time()} Error parsing the input string: {str}\n")


def error_write_log(str: str) -> None:
    with open('logs.txt', 'a') as f:
        f.write(f"{current_time()} Error in sending string: {str}\n")


def error_open_port_log(PORT: str) -> None:
    with open('logs.txt', 'a') as f:
        f.write(f"{current_time()} Error in opening port: {PORT}\n")
