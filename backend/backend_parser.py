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


get_count_params_map = dict.fromkeys(['bmk', 'cmdP', 'cmd05', 'cmd10', 'cmd15', 'cmd20', 'cmd25', 'cmd30', 'cmd35',
                                      'cmd40', 'countKT1', 'countKR1', 'countKT2', 'countKR2'
                                      'countKT22', 'countKR22', 'cs'], 'default')
gPr_params_map = dict.fromkeys(['bmk', 'pr0', 'pr1', 'pr2', 'er',
                                'bmkC', 'prC0', 'prC1', 'erC', 'cs'], 'default')
get_status_params_map = dict.fromkeys(['bmk', 'bmkS', 'bmkSK', 'pr', 'pr0', 'pr1',
                                   'temp', 'P05', 'P10', 'P15', 'P20', 'P25',
                                   'P30', 'P35', 'Err', 'uPit', 'temHeart', 'timeW', 'prAtmCal0',
                                   'prAtmCal1', 'Styp', 'l', 'temp2', 'timeR', 'cs'], 'default')
get_delta_params_map = dict.fromkeys(
    ['bmk', 'FtUP', 'FtDN', 'FsUP', 'FsDN', 'DelayPT', 'DelayTP', 'AlgT', 'AlgP', 'cs'], 'default')
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


get_status_params = get_status_params_map.keys()
get_count_params = get_count_params_map.keys()
gPr_params = gPr_params_map.keys()
get_delta_params = get_delta_params_map.keys()


def check_err(str: str) -> list:
    if int(str) == 0:
        tmp_err_lst = []
        return tmp_err_lst
    err = int(str)
    for i in range(len(error_list)):
        if err & 1:
            tmp_err_lst.append(error_list[i])
        err = err >> 1
    return tmp_err_lst


def parse_get_status(str: str) -> bool:
    var = str.replace('=', ' ')
    var = var.split()
    if var:
        if var[0] == 'bmk' and var[len(var)-2] == 'cs':
            for i in var:
                if i in get_status_params:
                    get_status_params_map[i] = var[var.index(i)+1]
            if 'default' in get_status_params_map.values():
                return False
            return True
    return False


def parse_gPr(str: str) -> bool:
    var = str.replace('=', ' ')
    var = var.spit()
    for i in var:
        if i in gPr_params_map:
            if not var.index(i) == (len(var)-1):
                gPr_params_map[i] = var[var.index(i) + 1]
    if 'default' in gPr_params_map.values():
        return False
    return True


def parse_get_count(str: str) -> bool:
    var = str.replace('=', ' ')
    var = var.split()
    if var:
        if var[0] == 'bmk' and var[len(var)-2] == 'cs':
            for i in var:
                if i in get_count_params:
                    if not var.index(i) == (len(var)-1):
                        get_count_params_map[i] = var[var.index(i) + 1]
            if 'default' in get_count_params_map.values():
                return False
            return True
    return False


def parse_get_delta(str: str) -> bool:
    var = str.replace('=', ' ')
    var = var.split()
    if var:
        if var[0] == 'bmk' and var[len(var)-2] == 'cs':
            for i in var:
                if i in get_delta_params:
                    if not var.index(i) == (len(var)-1):
                        get_delta_params_map[i] = var[var.index(i) + 1]
            if 'default' in get_delta_params_map.values():
                return False
            return True
    return False


def parse_settings_commans(str: str) -> bool:
    if 'OK' in str:
        return True
    else:
        return False


def parse_com_str(str: str, last_command: str) -> bool:
    str = str.decode(encoding='utf-8', errors='ignore')
    if 'incorrect command' in str:
        return False
    elif last_command == 'get_status':
        return parse_get_status(str)
    elif last_command == 'gPr':
        return parse_gPr(str)
    elif last_command == 'get_count':
        return parse_get_count(str)
    elif last_command == 'get_delta':
        return parse_get_delta(str)
    else:
        return parse_settings_commans(str)


