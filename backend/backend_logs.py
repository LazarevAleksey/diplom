# Here some logs func to registr some strange behavior  



def success_parsing_log(str: str) -> None:
    with open('logs.txt', 'a') as f:
        f.write(f"Success parsing the input string: {str}\n")

def error_parsing_log(str: str) -> None:
    with open('logs.txt', 'a') as f:
        f.write(f"Error parsing the input string: {str}\n")

def error_write_log(str: str) -> None:
    with open('logs.txt', 'a') as f:
        f.write(f"Error in sending string: {str}\n")

def error_open_port_log(PORT: str) -> None:
    with open('logs.txt', 'a') as f:
        f.write(f"Error in opening port: {PORT}\n")




