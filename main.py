# For GUI we chose dear pygui. For each of BUKs we made a different window, and show all
# data in tables. For each of commands we made different button that callback
# a function to create a context menu of command.
# TODO: Counter of false data and repainting bmk window
# TODO: Logs buttn and menu for it
# TODO: Paint stp text if hovered by mouse
# TODO: Settings commands
import backend.backend_parser as parser
import backend.backend_serial as ser
from gui.callbacks import *
from multiprocessing import Process, Queue
import time
import serial
import random


list_for_plot_x:list[float] = []
list_for_plot_y1:list[float] = []
list_for_plot_y2:list[float] = []
win_pos: list[int] = [400, 100]
current_buks_list: list[str] = []

list_of_control_com: list[str] = ['getStatus\r\n',
                                  'gPr\r\n', 'getDelta\r\n', 'getCount\r\n']


def draw_scheme_at_run_time() -> None:
    windows_bmk_pos:list[list[int]] = []
    for bmk in list_of_bmk.keys():
        windows_bmk_pos.append(dpg.get_item_pos(f"BMK:{bmk}"))
    w, h, c, d = dpg.load_image('./post.png')
    with dpg.texture_registry(show=False):
        dpg.add_static_texture(width=w, height=h, default_value=d, tag="post_tag")
    
    with dpg.window(tag=f"TIME", pos= (470, 80), no_background= True, no_resize=True, no_close=True, no_title_bar=True, autosize=False):    
        dpg.add_text(tag = 'time_tag',pos=(10,0), default_value="TIME", color=(0, 0, 0, 255))
    dpg.draw_line(parent = "Main window", p1= (470,65), p2 = (550,65), thickness=20, color=(int(0.70 * 255), int(1.00 * 255), int(0.70 * 255), int(1.00 * 255)))
        
    dpg.add_image(parent = "Main window", texture_tag = 'post_tag', pos=(350, 570), width = 300, height = 200)
    dpg.add_text(parent = "Main window", pos=(180, 60), default_value = "МОСКВА",          color = (0, 0, 0, 255))
    dpg.add_text(parent = "Main window", pos=(470, 60), default_value = "СТП АРС-4",       color = (0, 0, 0, 255), tag = "Main lable")
    dpg.add_text(parent = "Main window", pos=(750, 60), default_value = "САНКТ-ПЕТЕРБУРГ", color = (0, 0, 0, 255))
    dpg.add_text(parent = "Main window", pos=(180, windows_bmk_pos[2][1] - 20), default_value = "107СПУ")
    dpg.add_text(parent = "Main window", pos=(290, windows_bmk_pos[2][1] + 5 ), default_value = "107")
    dpg.add_text(parent = "Main window", pos=(100, windows_bmk_pos[7][1] - 20), default_value = "106-119СПУ")
    dpg.add_text(parent = "Main window", pos=(210, windows_bmk_pos[7][1] - 20), default_value = "119-120АПУ")
    dpg.add_text(parent = "Main window", pos=(290, windows_bmk_pos[7][1] + 5 ), default_value = "120")
    dpg.add_text(parent = "Main window", pos=(150, windows_bmk_pos[7][1] + 5 ), default_value = "119")
    dpg.draw_arrow(parent = "Main window", p1 = (100, 50), p2=(300, 50), thickness = 3, color=(0, 0, 0, 255))
    dpg.draw_arrow(parent = "Main window", p1 = (900, 50), p2=(700, 50), thickness = 3, color=(0, 0, 0, 255))
    dpg.draw_line(parent = "Main window", p1 = (90,  windows_bmk_pos[2][1] - 25), p2=(300, windows_bmk_pos[2][1] - 25), thickness = 4, color=(0, 0, 0, 255))
    dpg.draw_line(parent = "Main window", p1 = (300, windows_bmk_pos[2][1] - 25), p2=(windows_bmk_pos[0][0], windows_bmk_pos[0][1] +   29), thickness = 4, color=(0, 0, 0, 255))
    dpg.draw_line(parent = "Main window", p1 = (300, windows_bmk_pos[2][1] - 25), p2=(windows_bmk_pos[2][0], windows_bmk_pos[2][1] +   30),thickness = 4, color=(0, 0, 0, 255))
    dpg.draw_line(parent = "Main window", p1 = (300, windows_bmk_pos[7][1] - 25), p2=(windows_bmk_pos[4][0], windows_bmk_pos[4][1] +   29), thickness = 4, color=(0, 0, 0, 255))
    dpg.draw_line(parent = "Main window", p1 = (300, windows_bmk_pos[7][1] - 25), p2=(windows_bmk_pos[7][0], windows_bmk_pos[7][1] +   29), thickness = 4, color=(0, 0, 0, 255))
    dpg.draw_line(parent = "Main window", p1 = (160, windows_bmk_pos[7][1] - 25), p2=(windows_bmk_pos[10][0], windows_bmk_pos[10][1] + 29), thickness = 4, color=(0, 0, 0, 255))
    dpg.draw_line(parent = "Main window", p1 = (90,  windows_bmk_pos[7][1] - 25), p2=(300, windows_bmk_pos[7][1] - 25), thickness=4, color=(0, 0, 0, 255))
    for i in range(len(windows_bmk_pos)):
        if i == 1 or i == 3 or i == 6 or i ==9 or i == 11:
            dpg.draw_line(parent ="Main window", p1 = (400, windows_bmk_pos[i][1] + 29), p2=(900, windows_bmk_pos[i][1] + 29), thickness=4, color=(0, 0, 0, 255))
    
def main_com_loop(q: Queue) -> None:
    ser.PORT = ser.avilable_com()
    commands_list:list[bytes] = []
    with serial.Serial(ser.PORT, ser.BAUD, ser.BYTE_SIZE, ser.PARITY, ser.STOP_BITS, timeout=0.5) as port:
        while True:
            for bmk in list_of_bmk.keys():
                for command in list_of_control_com[:4]:
                    commands_list.append(ser.commands_generator(bmk, command).encode())       
                data = ser.send_command(commands_list, port)
                q.put({'bmk': f'{bmk}', 'data': data})
                commands_list = []
                
q_global = Queue()
cnt:int = 0
def create_dict_to_emulate_bmk(commands_list:list[str], q:Queue) -> None:
    global cnt
    dict_to_write:dict[str, bool | dict[str, str]] = {}
    for command in commands_list:
        cnt += 1
        command_name = f'{command[8:]}'
        bmk_num = f'{command[4:7]}'
        if command_name =='getStatus\r\n':
            time.sleep(0.2)
            if cnt > 20 and cnt < 24:
                dict_to_write[f'{command_name}'] = parser.parse_com_str(f"={bmk_num} bmkS=007 bmkSK=2 pr={str(random.randrange(0,400))} pr0=000 pr1=000 temp=+232 P05=064 P10=125  P15=219  P20=316  P25=401  P30=489  P35=581  Err=00000300  uPit=23  temHeart=+05 timeW=00003053 prAtmCal0=+00 prAtmCal1=+00 Styp=00 l=000 temp2=+242 timeR=000006 cs=114\r\n".encode(), command_name)
                q.put({'bmk': f'{bmk_num}', 'data': dict_to_write})
            else:
                dict_to_write[f'{command_name}'] = parser.parse_com_str(f"bmk={bmk_num} bmkS=007 bmkSK=2 pr={str(random.randrange(0,400))} pr0=000 pr1=000 temp=+232 P05=064 P10=125  P15=219  P20=316  P25=401  P30=489  P35=581  Err=00000300  uPit=23  temHeart=+05 timeW=00003053 prAtmCal0=+00 prAtmCal1=+00 Styp=00 l=000 temp2=+242 timeR=000006 cs=114\r\n".encode(), command_name)
                q.put({'bmk': f'{bmk_num}', 'data': dict_to_write})
            dict_to_write = {}
        if cnt > 24:
            cnt = 0
        
        elif command_name =='gPr\r\n':
            time.sleep(0.2)
            dict_to_write[f'{command_name}'] = parser.parse_com_str(f"bmk={bmk_num} pr0={str(random.randrange(300,400))} pr1={str(random.randrange(200,400))} pr2=000 er=00000000 bmkC=007 prC0=003 prC1=000 erC=00000000 cs=016".encode(), command_name)
            q.put({'bmk': f'{bmk_num}', 'data': dict_to_write})
            dict_to_write = {}
        

def bmk_emulator(q:Queue) -> None:
    commands_list:list[str] = []   
    for bmk in list_of_bmk.keys():
        for command in list_of_control_com[:1]:
            commands_list.append(ser.commands_generator(bmk, command))    
    while True:
        create_dict_to_emulate_bmk(commands_list, q)
        if not q_global.empty():
            commands_list = q_global.get_nowait()
                        
def show_bmk_windows(q: Queue) -> None:
    global current_buks_list
    if not q.empty():
        params_dict = q.get_nowait()
        current_bmk = params_dict['bmk']
        #TODO: REMOVE TRY AND FIX THIS!
        try:
            if params_dict['data']['getStatus\r\n']:
                if not current_bmk in current_buks_list:
                    current_buks_list.append(current_bmk)
                    redraw_bmk_window(params_dict)
                if int(params_dict['data']['getStatus\r\n']['Err']):
                    if not dpg.get_value(f"line_err{current_bmk}"):
                        dpg.set_value(f"line_err{current_bmk}", True)
                    dpg.set_item_user_data(f"err_{current_bmk}", params_dict)
                else:
                    if dpg.get_value(f"line_err{current_bmk}"):
                        dpg.set_value(f"line_err{current_bmk}", False)
                redraw_window_table(params_dict)
                dpg.set_item_user_data(f"bmk_{current_bmk}", params_dict)
            else:
                current_buks_list =  find_false(current_bmk, current_buks_list)
        except KeyError:
            if params_dict['data']['gPr\r\n']:
                redraw_pr_plot(params_dict['data']['gPr\r\n'])
            else:
                dpg.delete_item(f'line_{current_bmk}')
                dpg.draw_line(parent =f"BMK:{current_bmk}", p1 = (0, 50), p2= (150, 50), thickness=4, color=(255, 0, 255, 255), tag =f'line_{current_bmk}')
    print_real_time()                    
    blick_line_if_error()

def find_false(current_bmk:str, current_buks_list:list[str]) -> list[str]:
    dpg.delete_item(f'line_{current_bmk}')
    dpg.draw_line(parent =f"BMK:{current_bmk}", p1 = (0, 50), p2= (150, 50), thickness=4, color=(255, 0, 255, 255), tag =f'line_{current_bmk}')
    if dpg.get_value(f"line_err{current_bmk}"):
        dpg.set_value(f"line_err{current_bmk}", False)
    dpg.set_item_callback(f'bmk_{current_bmk}', callback= None)
    dpg.set_item_callback(f'err_{current_bmk}', callback= None)
    dpg.bind_item_handler_registry(f'text_{current_bmk}', None)
    current_buks_list.pop(current_buks_list.index(current_bmk))
    return current_buks_list



def blick_line_if_error() -> None:
    if dpg.get_value("cnt") == 0 or dpg.get_value("cnt") == 30:
        for bmk in list_of_bmk.keys():
            if dpg.get_value(f"line_err{bmk}"):
                if dpg.get_value(f"line_cnt{bmk}"):
                    dpg.set_value(f"line_cnt{bmk}", False)
                    dpg.delete_item(f'line_{bmk}')
                    dpg.draw_line(parent =f"BMK:{bmk}", p1 = (0, 50), p2= (150, 50), thickness=4, color=(255, 0, 0, 255), tag =f'line_{bmk}')
                else:
                    dpg.delete_item(f'line_{bmk}')
                    dpg.draw_line(parent =f"BMK:{bmk}", p1 = (0, 50), p2= (150, 50), thickness=4, color=(0, 0, 0, 255), tag =f'line_{bmk}')
                    dpg.set_value(f"line_cnt{bmk}", True)
                dpg.set_value("cnt", 1)
            else:
                return
    else: 
        dpg.set_value("cnt", dpg.get_value("cnt") + 1)

err_pos:list[int] = [800, 700]
def close_err() -> None:
    global err_pos
    err_pos = [800, 700]


def err_callback(sender:int, app_data:str, user_data:dict[str, str]) -> None:
    global err_pos
    bmk:str = user_data['bmk']
    if not user_data['data']['getStatus\r\n']:
        return
    err:str = user_data["data"]['getStatus\r\n']['Err']
    if dpg.does_item_exist(f"ERR:{bmk}"):
        if dpg.is_item_visible(f"ERR:{bmk}"):
            return
        else:
            dpg.delete_item(f"ERR:{bmk}")
    list_of_errors = parser.check_err(err)
    with dpg.window(tag = f"ERR:{bmk}", pos = err_pos, autosize=True, no_move=False, label = f"Ошибки {list_of_bmk[bmk]}", on_close=close_err, min_size=(400, 50)):
        if not list_of_errors:
            dpg.add_text(f"Ошибок нет")
        else:
            for i, err in enumerate(list_of_errors):
                dpg.add_text(f"{i+1}. {str(err)}")
        err_pos[0] -= 50
        err_pos[1] -= 50
    if err_pos[0] == 500 and err_pos[1] == 400:
        err_pos = [800, 700]


def redraw_window_table(params:dict[str, dict[str, dict[str, str]]]) -> None:
    bmk: str = str(params['bmk'])
    data_for_table = params['data']['getStatus\r\n']
    if not data_for_table:
        return
    if dpg.does_item_exist(f"MT_{bmk}"):
        for i in range(len(list(data_for_table)) - 1):
            if i == 14 or i == 5:
                continue
            elif i == 6:
                dpg.set_value(f"row{bmk}_{i}", str(data_for_table[list(data_for_table)[6]])[0] + str(data_for_table[list(data_for_table)[6]])[1:-1] +'.'+str(data_for_table[list(data_for_table)[i]])[3:])
            elif i == 16:
                dpg.set_value(f"row{bmk}_{i}", data_for_table[list(data_for_table)[16]][0] + str(int(data_for_table[list(data_for_table)[16]][1:])))
            elif i == 20:
                dpg.set_value(f"row{bmk}_{i}", styp_torm(data_for_table[list(data_for_table)[20]]))
            elif i == 21:
                dpg.set_value(f"row{bmk}_{i}", state_l(data_for_table[list(data_for_table)[21]]))
            elif i == 22:
                dpg.set_value(f"row{bmk}_{i}", data_for_table[list(data_for_table)[22]][0] + str(data_for_table[list(data_for_table)[22]])[1:-1] +'.'+str(data_for_table[list(data_for_table)[22]])[3:])
            elif i == 15:
                dpg.set_value(f"row{bmk}_{i}", str(int(data_for_table[list(data_for_table)[15]])) + "B")
            elif i == 19 or i == 18:
                dpg.set_value(f"row{bmk}_{i}", data_for_table[list(data_for_table)[i]])
            else:
                dpg.set_value(f"row{bmk}_{i}", int(data_for_table[list(data_for_table)[i]]))


            
i:int  = 0
def redraw_pr_plot(data:dict[str, str]) -> None:
    global i, list_for_plot_y1, list_for_plot_y2, list_for_plot_x
    if dpg.does_item_exist("plot_win"):
        if dpg.is_item_visible("plot_win"):
            i += 1
            list_for_plot_y1.append(int(data['pr0']))
            list_for_plot_y2.append(int(data['pr1']))
            list_for_plot_x.append(i*10)
            dpg.set_value("series_tag1", [list_for_plot_x , list_for_plot_y1])
            dpg.set_value("series_tag2", [list_for_plot_x, list_for_plot_y2])
            # dpg.fit_axis_data("y_axis")
            dpg.fit_axis_data("x_axis")
            if i > 40:
                list_for_plot_y1.pop(0)
                list_for_plot_y2.pop(0)
                list_for_plot_x.pop(0)
        else:
            list_for_plot_y1 = []
            list_for_plot_y2 = []
            list_for_plot_x = []
            dpg.delete_item("plot_win")
            i = 0

def redraw_bmk_window(params_dict: dict[str, dict[str, dict[str, str] ]]) -> None:
    bmk:str = str(params_dict['bmk'])
    new_pos = dpg.get_item_pos(f"BMK:{bmk}")
    dpg.delete_item(f"BMK:{bmk}")
    with dpg.window(tag=f"BMK:{bmk}", pos= new_pos, no_background= True, no_resize=True, no_close=True, no_title_bar=True, autosize=True, no_move=True):
        dpg.add_button(label= " ИНФ.", tag=f"bmk_{bmk}", pos = (7, 20), user_data = params_dict,callback=draw_window_table)
        dpg.add_button(label= "ОШИБ.", tag = f"err_{bmk}", pos = (100, 20), user_data =params_dict, callback= err_callback)
        dpg.add_text(f"{list_of_bmk[bmk]}", pos= (60, 40), tag = f'text_{bmk}', user_data=f"{list_of_bmk[bmk]}")
        dpg.draw_line(p1 = (0, 50), p2= (150, 50), thickness=4, color=(0, 0, 0, 255), tag=f'line_{bmk}')
    dpg.bind_item_handler_registry(f'text_{bmk}', "plot_callback")

inf_pos:list[int] = [0 , 0]

def close_inf() -> None:
    global inf_pos
    inf_pos = [0 , 0]
def draw_window_table(sender:int, add_data:str ,user_data:dict[str, dict[str, dict[str, str]]]) -> None:
    global inf_pos
    bmk: str = str(user_data['bmk'])
    data_for_table = user_data['data']['getStatus\r\n']
    if not data_for_table:
        return
    if dpg.does_item_exist(f"INFO:{bmk}"):
        if dpg.is_item_visible(f"INFO:{bmk}"):
            return
        else:
            dpg.delete_item(f"INFO:{bmk}")
    with dpg.window(tag=f"INFO:{bmk}", label=f"{list_of_bmk[bmk]}", autosize= True, pos = inf_pos, on_close=close_inf):
        with dpg.table(tag=f"MT_{bmk}", header_row=False, width=400, borders_innerH=True, borders_innerV=True, policy= dpg.mvTable_SizingFixedFit):
            dpg.add_table_column()
            dpg.add_table_column()
            draw_info_table(bmk, data_for_table)
        inf_pos[0] += 50
        inf_pos[1] += 50
        if inf_pos[0] == 300 and inf_pos[1] == 300:
            inf_pos[0] = 0
            inf_pos[1] = 0
    dpg.bind_item_font(f"INFO:{bmk}", 'table_font')

def draw_bmk_window_at_runtime() -> None:
    for bmk in list_of_bmk.keys():
        with dpg.window(tag=f"BMK:{bmk}", pos= win_pos, no_background= True, no_resize=True, no_close=True, no_title_bar=True, autosize=True, no_move=True, no_collapse=True):
            dpg.add_button(label= " ИНФ.", tag=f"bmk_{bmk}", pos = (7, 20))
            dpg.add_button(label= "ОШИБ.", tag = f"err_{bmk}", pos = (100, 20))
            dpg.add_text(f"{list_of_bmk[bmk]}", pos= (60, 40), tag=f'text_{bmk}', user_data=f"{list_of_bmk[bmk]}")
            dpg.draw_line(p1 = (0, 50), p2= (150, 50), thickness=4, color=(255, 0, 255, 255), tag =f'line_{bmk}')
        win_pos[0] +=  150
        current_index_bmk = (list(list_of_bmk.keys()).index(bmk) + 1)
        # dpg.bind_item_handler_registry(f'text_{bmk}', "plot_callback")
        if current_index_bmk == 2 or current_index_bmk == 4 or current_index_bmk == 7 or current_index_bmk == 10:
            win_pos[1] += 100
            win_pos[0] = 400


def close_plot() -> None:
    commands_list:list[str] = []
    for bmk in list_of_bmk.keys():
        for command in list_of_control_com[:1]:
            commands_list.append(ser.commands_generator(bmk, command)) 
    q_global.put(commands_list)

def create_plot(sender:int, app_data:list[str]) -> None:
    if dpg.does_item_exist("plot_win"):
        if dpg.is_item_visible("plot_win"):
            return
        else:
            dpg.delete_item("plot_win")
    current_bmk:str = list_of_bmk[app_data[1][5:]]
    with dpg.window(label=f"Показатели давления на {current_bmk}", tag="plot_win", pos = (950, 80), no_background=False, no_title_bar=False, no_resize=True, on_close= close_plot, no_move=True):
        with dpg.plot(label=f"Давление датчика 1 и 2 {current_bmk}", height=450, width=450):
            dpg.add_plot_legend()
            dpg.add_plot_axis(dpg.mvXAxis, label="Счетчик", tag="x_axis")
            dpg.add_plot_axis(dpg.mvYAxis, label="Давление кПа", tag="y_axis")
            dpg.add_line_series(list_for_plot_x, list_for_plot_y1, label=f"Давление датчика 1 {current_bmk}", parent="y_axis", tag="series_tag1")
            dpg.add_line_series(list_for_plot_x, list_for_plot_y2, label=f"Давление датчика 2 {current_bmk}", parent="y_axis", tag="series_tag2")
            dpg.set_axis_limits("y_axis", 0, 500)
            dpg.bind_item_theme("series_tag1", "ser1_theme")
            dpg.bind_item_theme("series_tag2", "ser2_theme")
            # dpg.set_axis_limits("x_axis", 100, 400)
    commands_list:list[str] = []
    for bmk in list_of_bmk.keys():
        for command in list_of_control_com[:1]:
            commands_list.append(ser.commands_generator(bmk, command)) 
    for i in range(1, len(commands_list)*2 , 2):
        commands_list.insert(i, f'bmk:{app_data[1][5:]}:gPr\r\n')
    q_global.put(commands_list)


def main_window(q: Queue) -> None:
    dpg.create_context()
    with dpg.item_handler_registry(tag = "plot_callback"):
        dpg.add_item_clicked_handler(callback=create_plot)
    with dpg.window(tag = "Main window", no_scrollbar= True, no_focus_on_appearing=False, no_resize=True, no_move=True, min_size=(1024, 768), autosize=False):
        with dpg.menu_bar():
            dpg.add_menu_item(label="Настйроки")
            dpg.add_menu_item(label="Помощь")
            with dpg.menu(label="О программе"):
                dpg.add_text(default_value="""Разработано в ЦКЖТ в 2023 году
Разработчик Волков Егор Алексеевич 
По всем вопросам обращаться по адресу: gole00201@gmail.com""")
    draw_bmk_window_at_runtime()
    draw_scheme_at_run_time()
    dpg.bind_theme(create_theme_imgui_light())
    dpg.set_primary_window("Main window", True)
    dpg.create_viewport(title="STP ARS-4", width=1440, height=900, resizable= False)
    with dpg.value_registry():
        for bmk in list_of_bmk.keys():
            dpg.add_bool_value(tag = f"line_err{bmk}", default_value= False)
            dpg.add_bool_value(tag = f"line_cnt{bmk}", default_value= True)
        dpg.add_int_value(tag = f"cnt")
    with dpg.theme(tag = "ser1_theme"):
        with dpg.theme_component(dpg.mvLineSeries):
            dpg.add_theme_color(dpg.mvPlotCol_Line, (0, 255, 0), category= dpg.mvThemeCat_Plots)
    with dpg.theme(tag = "ser2_theme"):
        with dpg.theme_component(dpg.mvLineSeries):
            dpg.add_theme_color(dpg.mvPlotCol_Line, (255, 0, 0), category= dpg.mvThemeCat_Plots)
    with dpg.font_registry():
        with dpg.font("./fonts/Cousine-Bold.ttf", 15, default_font=True, tag='Main_font'):
            dpg.add_font_range_hint(dpg.mvFontRangeHint_Cyrillic)
        with dpg.font("./fonts/Cousine-Regular.ttf", 15, default_font=True, tag='table_font'):
            dpg.add_font_range_hint(dpg.mvFontRangeHint_Cyrillic)
        with dpg.font("./fonts/Cousine-Bold.ttf", 20, default_font=True, tag='lable_font'):
            dpg.add_font_range_hint(dpg.mvFontRangeHint_Cyrillic)
        with dpg.font("./fonts/Cousine-Bold.ttf", 18, default_font=True, tag='time_font'):
            dpg.add_font_range_hint(dpg.mvFontRangeHint_Cyrillic)
    
    dpg.bind_item_font("TIME", "time_font")
    dpg.bind_item_font("Main lable", "lable_font")
    dpg.bind_font('Main_font')

    dpg.setup_dearpygui()
    dpg.show_viewport()
    # dpg.show_style_editor()
    # dpg.show_metrics()
    while dpg.is_dearpygui_running():
        show_bmk_windows(q)
        dpg.render_dearpygui_frame()
    dpg.destroy_context()


if __name__ == '__main__':
    q = Queue()
    p1 = Process(target=bmk_emulator, args=(q,))
    p2 = Process(target=main_window, args=(q,))
    p1.start()
    p2.start()
