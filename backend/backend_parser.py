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
error_list = ["неисправен, не подключен или не откалиброван датчик давления 1",
              "неисправен, не подключен или не откалиброван датчик давления 2",
              "неисправен или не подключен датчик температуры 1",
              "неисправен или не подключен датчик температуры 2",
              "критическое снижение уровня напряжение питания",
              "критическое повышение уровня напряжение питания",
              "не работает обогрев БУКЭП",
              "температура внутри обогреваемого блока меньше 1 C",
              "перегрузка по току выхода управления катушкой соленоида КТ1",
              "обрыв цепи по выходу управления катушкой соленоида КТ1",
              "перегрузка по току выхода управления катушкой соленоида КР1",
              "обрыв цепи по выходу управления катушкой соленоида КР1",
              "перегрузка по току выхода управления катушкой соленоида КТ2",
              "обрыв цепи по выходу управления катушкой соленоида КТ2",
              "перегрузка по току выхода управления катушкой соленоида КР2",
              "обрыв цепи по выходу управления катушкой соленоида КР2",
              "пришла не корректная дистанционная команда по цепям «Р», «Т1»-«Т4»",
              "пришла не корректная местная команда",
              "пришла не корректная команда по шине CAN",
              "включен ручной режим обогрева "]

# Setup 4th sort mountain

list_of_buks: list[str] = ['009', '255', '238', '221']
list_of_control_com: list[str] = ['getStatus\r\n',
                                  'gPr\r\n', 'getDelta\r\n', 'getCount\r\n']

# Just keys
get_status_params = get_status_params_map.keys()
get_count_params = get_count_params_map.keys()
gPr_params = gPr_params_map.keys()
get_delta_params = get_delta_params_map.keys()

# Take the error varible and find the err from error_list

# TODO: Make it works in send_command() from serial


def check_err(string: str) -> list[str]:
    tmp_err_lst: list[str] = []
    if int(string) == 0:
        return tmp_err_lst
    err = int(string)
    for i in range(len(error_list)):
        if err & 1:
            tmp_err_lst.append(error_list[i])
        err = err >> 1
    return tmp_err_lst

# Parse get_status answer


def parse_get_status(string: str) -> bool | dict[str, str]:
    r_string = string.replace('=', ' ')
    var: list[str] = r_string.split()
    if var:
        if var[0] == 'bmk' and var[len(var)-2] == 'cs':
            for i in var:
                if i in get_status_params:
                    get_status_params_map[i] = var[var.index(i) + 1]
            if 'default' in get_status_params_map.values():
                return False
            return get_status_params_map
    return False

# Parse gPr answer


def parse_gPr(string: str) -> bool | dict[str, str]:
    r_string = string.replace('=', ' ')
    var: list[str] = r_string.split()
    if var:
        if var[0] == 'bmk' and var[len(var)-2] == 'cs':
            for i in var:
                if i in gPr_params_map:
                    if not var.index(i) == (len(var)-1):
                        gPr_params_map[i] = var[var.index(i) + 1]
            if 'default' in gPr_params_map.values():
                return False
            return gPr_params_map
    return False
# Parse get_count answer


def parse_get_count(string: str) -> bool | dict[str, str]:
    print(get_count_params)
    r_string = string.replace('=', ' ')
    var: list[str] = r_string.split()
    if var:
        if var[0] == 'bmk' and var[len(var)-2] == 'cs':
            for i in var:
                if i in get_count_params:
                    if not var.index(i) == (len(var)-1):
                        get_count_params_map[i] = var[var.index(i) + 1]
            if 'default' in get_count_params_map.values():
                return False
            return get_count_params_map
    return False

# Parse get_delta answer


def parse_get_delta(string: str) -> bool | dict[str, str]:
    r_string = string.replace('=', ' ')
    var: list[str] = r_string.split()
    if var:
        if var[0] == 'bmk' and var[len(var)-2] == 'cs':
            for i in var:
                if i in get_delta_params:
                    if not var.index(i) == (len(var)-1):
                        get_delta_params_map[i] = var[var.index(i) + 1]
            if 'default' in get_delta_params_map.values():
                return False
            return get_delta_params_map
    return False


def parse_settings_commans(str: str) -> bool:
    if 'OK' in str:
        return True
    else:
        return False

# Collaboration of all the commands


def parse_com_str(string_b: bytes, last_command: str) -> bool | dict[str, str]:
    string = string_b.decode(encoding='utf-8', errors='ignore')
    if 'incorrect command' in string:
        return False
    elif last_command == 'getStatus\r\n':
        return parse_get_status(string)
    elif last_command == 'gPr\r\n':
        return parse_gPr(string)
    elif last_command == 'getDelta\r\n':
        return parse_get_delta(string)
    elif last_command == 'getCount\r\n':
        return parse_get_count(string)
    else:
        return parse_settings_commans(string)
