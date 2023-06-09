# In BUK we have several commands to get control info:
# getCount - request for coil response counters and braking stages
# getDelta - request for coefficients to calculate the rate of rise and fall
# of pressure
# getStatus - request for general system parameters
# gPr - pressure request
# For each of them im made a answer pares func and map
# Example of string (getStatus command):
# bmk=009 bmkS=007 bmkSK=2 pr=000 pr0=000 pr1=000 temp=+232 P05=064
# P10=125  P15=219  P20=316  P25=401  P30=489  P35=581  Err=00000000  uPit=23  temHeart=+05
# timeW=00003053 prAtmCal0=+00 prAtmCal1=+00 Styp=00 l=000 temp2=+242 timeR=000006
# cs=114

# Need to store the data from BUK by default = 'default'
get_count_params_map = dict.fromkeys(['bmk', 'cmdP', 'cmd05', 'cmd10', 'cmd15', 'cmd20', 'cmd25', 'cmd30', 'cmd35',
                                      'cmd40', 'countKT1', 'countKR1', 'countKT2', 'countKR2',
                                      'countKT22', 'countKR22', 'cs'], 'default')
gPr_params_map = dict.fromkeys(['bmk', 'pr0', 'pr1', 'pr2', 'er',
                                'bmkC', 'prC0', 'prC1', 'erC', 'cs'], 'default')
get_status_params_map = dict.fromkeys(['bmk', 'bmkS', 'bmkSK', 'pr', 'pr0', 'pr1',
                                       'temp', 'P05', 'P10', 'P15', 'P20', 'P25',
                                       'P30', 'P35', 'Err', 'uPit', 'temHeart', 'timeW', 'prAtmCal0',
                                       'prAtmCal1', 'Styp', 'l', 'temp2', 'timeR', 'cs'], 'default')
get_delta_params_map = dict.fromkeys(
    ['bmk', 'FtUP', 'FtDN', 'FsUP', 'FsDN', 'DelayPT', 'DelayTP', 'AlgT', 'AlgP', 'cs'], 'default')
# Need to load err msg on screen
error_list = ["Неисправен, не подключен или не откалиброван датчик давления 1",
              "Неисправен, не подключен или не откалиброван датчик давления 2",
              "Неисправен или не подключен датчик температуры 1",
              "Неисправен или не подключен датчик температуры 2",
              "Критическое снижение уровня напряжение питания",
              "Критическое повышение уровня напряжение питания",
              "Не работает обогрев БУКЭП",
              "Температура внутри обогреваемого блока меньше 1 C",
              "Перегрузка по току выхода управления катушкой соленоида КТ1",
              "Обрыв цепи по выходу управления катушкой соленоида КТ1",
              "Перегрузка по току выхода управления катушкой соленоида КР1",
              "Обрыв цепи по выходу управления катушкой соленоида КР1",
              "Перегрузка по току выхода управления катушкой соленоида КТ2",
              "Обрыв цепи по выходу управления катушкой соленоида КТ2",
              "Перегрузка по току выхода управления катушкой соленоида КР2",
              "Обрыв цепи по выходу управления катушкой соленоида КР2",
              "Пришла не корректная дистанционная команда по цепям «Р», «Т1»-«Т4»",
              "Пришла не корректная местная команда",
              "Пришла не корректная команда по шине CAN",
              "Включен ручной режим обогрева "]


# Just keys
get_status_params = get_status_params_map.keys()
get_count_params = get_count_params_map.keys()
gPr_params = gPr_params_map.keys()
get_delta_params = get_delta_params_map.keys()

# Take the error tokensible and find the err from error_list

# TODO: Make it works in send_command() from serial


def check_err(string: str) -> list[str]:
    # Each bit in the "Err" line displays a specific error 
    # in the operation of the BMC. 
    # Here we run through the bits and allocate equal "1"
    tmp_err_lst: list[str] = []
    if int(string) == 0:
        return tmp_err_lst
    err = int(string)
    for i in range(len(error_list)):
        if err & 1:
            tmp_err_lst.append(error_list[i])
        err = err >> 1
    return tmp_err_lst


def parse_string(string: str, params: dict[str, str]) -> bool | dict[str, str]:
    # Here we divide the string received from the com port by 
    # the "=" sign and save it to the list. We compare this list 
    # with the dictionary keys described at the beginning of the file. 
    # After that, we check the string composition and if there are no 
    # 'default' values left in the dictionary, we send it for output.
    read_string = string.replace('=', ' ')
    tokens: list[str] = read_string.split()
    if tokens:
        if tokens[0] == 'bmk' and tokens[len(tokens)-2] == 'cs':
            for token in tokens:
                if token in params.keys():
                    params[token] = tokens[tokens.index(token) + 1]
            if 'default' in params.values():
                return False
            return params
    return False

def parse_settings_commans(str: str) -> bool:
    if 'OK' in str:
        return True
    else:
        return False

def parse_com_str(string_b: bytes, last_command: str) -> bool | dict[str, str]:
    # Switch case off all parsers
    string = string_b.decode(encoding='utf-8', errors='ignore')
    if 'incorrect command' in string:
        return False
    elif last_command == 'getStatus\r\n':
        return parse_string(string, get_status_params_map)
    elif last_command == 'gPr\r\n':
        return parse_string(string, gPr_params_map)
    elif last_command == 'getDelta\r\n':
        return parse_string(string, get_delta_params_map)
    elif last_command == 'getCount\r\n':
        return parse_string(string, get_count_params_map)
    else:
        return parse_settings_commans(string)
