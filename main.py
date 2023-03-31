# For GUI we chose dear pygui. For each of BUKs we made a different window, and show all
# data in tables. For each of commands we made different button that callback
# a function to create a context menu of command.
# TODO: Logs buttn and menu for it
# TODO: Settings commands
import dearpygui.dearpygui as dpg
import backend.backend_parser as parser
import backend.backend_serial as ser
from gui.misc import *
from gui.callbacks import *
from gui.draw_scheme_stp import *

from multiprocessing import Process, Queue, Value
import time
import serial
import random


cnt: int = 0


def create_dict_to_emulate_bmk(commands_list: list[bytes], q: Queue) -> None:
    dict_to_write: dict[str, bool | dict[str, str]] = {}
    print(commands_list)
    global cnt
    for command in commands_list:
        command_name = f'{command[8:].decode()}'
        bmk_num = f'{command[4:7].decode()}'
        print(command)
        if command == 'bmk:009:getStatus\r\n'.encode():
            cnt += 1
            if cnt > 5 and cnt < 7:
                dict_to_write[f'{command_name}'] = parser.parse_com_str(
                    f"={bmk_num} bmkS=007 bmkSK=2 pr={str(random.randrange(0,400))} pr0=000 pr1=000 temp=+232 P05=064 P10=125  P15=219  P20=316  P25=401  P30=489  P35=581  Err=00000300  uPit=23  temHeart=+05 timeW=00003053 prAtmCal0=+00 prAtmCal1=+00 Styp=00 l=000 temp2=+242 timeR=000006 cs=114\r\n".encode(), command_name)
                q.put({'bmk': f'{bmk_num}', 'data': dict_to_write})
                dict_to_write = {}
            else:
                time.sleep(0.2)
                dict_to_write[f'{command_name}'] = parser.parse_com_str(
                    f"bmk={bmk_num} bmkS=007 bmkSK=2 pr={str(random.randrange(0,400))} pr0=000 pr1=000 temp=+232 P05=064 P10=125  P15=219  P20=316  P25=401  P30=489  P35=581  Err=00000300  uPit=23  temHeart=+05 timeW=00003053 prAtmCal0=+00 prAtmCal1=+00 Styp=00 l=000 temp2=+242 timeR=000006 cs=114\r\n".encode(), command_name)
                q.put({'bmk': f'{bmk_num}', 'data': dict_to_write})
                dict_to_write = {}
            if cnt > 10:
                cnt = 0
            continue
        if command == 'bmk:012:getStatus\r\n'.encode():
            cnt += 1
            if cnt > 5 and cnt < 7:
                dict_to_write[f'{command_name}'] = parser.parse_com_str(
                    f"={bmk_num} bmkS=007 bmkSK=2 pr={str(random.randrange(0,400))} pr0=000 pr1=000 temp=+232 P05=064 P10=125  P15=219  P20=316  P25=401  P30=489  P35=581  Err=00000300  uPit=23  temHeart=+05 timeW=00003053 prAtmCal0=+00 prAtmCal1=+00 Styp=00 l=000 temp2=+242 timeR=000006 cs=114\r\n".encode(), command_name)
                q.put({'bmk': f'{bmk_num}', 'data': dict_to_write})
                dict_to_write = {}
            else:
                time.sleep(0.2)
                dict_to_write[f'{command_name}'] = parser.parse_com_str(
                    f"bmk={bmk_num} bmkS=007 bmkSK=2 pr={str(random.randrange(0,400))} pr0=000 pr1=000 temp=+232 P05=064 P10=125  P15=219  P20=316  P25=401  P30=489  P35=581  Err=00000300  uPit=23  temHeart=+05 timeW=00003053 prAtmCal0=+00 prAtmCal1=+00 Styp=00 l=000 temp2=+242 timeR=000006 cs=114\r\n".encode(), command_name)
                q.put({'bmk': f'{bmk_num}', 'data': dict_to_write})
                dict_to_write = {}
            if cnt > 10:
                cnt = 0
            continue
        if command == 'bmk:010:getStatus\r\n'.encode():
            time.sleep(0.2)
            dict_to_write[f'{command_name}'] = parser.parse_com_str(
                f"bmk={bmk_num} bmkS=007 bmkSK=2 pr={str(random.randrange(0,400))} pr0=000 pr1=000 temp=+232 P05=064 P10=125  P15=219  P20=316  P25=401  P30=489  P35=581  Err=00000300  uPit=23  temHeart=+05 timeW=00003053 prAtmCal0=+00 prAtmCal1=+00 Styp=00 l=000 temp2=+242 timeR=000006 cs=114\r\n".encode(), command_name)
            q.put({'bmk': f'{bmk_num}', 'data': dict_to_write})
            dict_to_write = {}
            continue
        if command_name == 'getStatus\r\n':
            time.sleep(0.2)
            dict_to_write[f'{command_name}'] = parser.parse_com_str(
                f"bmk={bmk_num} bmkS=007 bmkSK=2 pr={str(random.randrange(0,400))} pr0=000 pr1=000 temp=+232 P05=064 P10=125  P15=219  P20=316  P25=401  P30=489  P35=581  Err=00000000  uPit=23  temHeart=+05 timeW=00003053 prAtmCal0=+00 prAtmCal1=+00 Styp=00 l=000 temp2=+242 timeR=000006 cs=114\r\n".encode(), command_name)
            q.put({'bmk': f'{bmk_num}', 'data': dict_to_write})
            dict_to_write = {}
        elif command_name == 'gPr\r\n':
            time.sleep(0.2)
            dict_to_write[f'{command_name}'] = parser.parse_com_str(
                f"bmk={bmk_num} pr0={str(random.randrange(300,400))} pr1={str(random.randrange(200,400))} pr2=000 er=00000000 bmkC=007 prC0=003 prC1=000 erC=00000000 cs=016".encode(), command_name)
            q.put({'bmk': f'{bmk_num}', 'data': dict_to_write})
            dict_to_write = {}


def main_com_loop(q: Queue, q_task: Queue) -> None:
    ser.PORT = ser.avilable_com()
    commands_list: list[bytes] = []
    for bmk in list_of_bmk.keys():
        for command in list_of_control_com[:1]:
            commands_list.append(ser.commands_generator(bmk, command).encode())
    with serial.Serial(ser.PORT, ser.BAUD, ser.BYTE_SIZE, ser.PARITY, ser.STOP_BITS, timeout=0.5) as port:
        while True:
            sending_commands_loop(commands_list, q, port)
            if not q_task.empty():
                commands_list = q_task.get_nowait()


def sending_commands_loop(commands_list: list[bytes], q: Queue, port: serial.Serial) -> None:
    dict_to_write: dict[str, bool | dict[str, str]] = {}
    for command in commands_list:
        bmk_num = f'{command[4:7].decode()}'
        # print({'bmk' : bmk_num, 'data' : ser.send_command(command.decode(), port)})
        q.put({'bmk': bmk_num, 'data': ser.send_command(command.decode(), port)})


def bmk_emulator(q: Queue, q_task: Queue) -> None:
    commands_list: list[bytes] = []
    for bmk in list_of_bmk.keys():
        for command in list_of_control_com[:1]:
            commands_list.append(ser.commands_generator(bmk, command).encode())
    while True:
        create_dict_to_emulate_bmk(commands_list, q)
        if not q_task.empty():
            commands_list = q_task.get_nowait()


def show_bmk_windows(q: Queue) -> None:
    global current_buks_list
    if not q.empty():
        params_dict = q.get_nowait()
        current_bmk = params_dict['bmk']
        # TODO: REMOVE TRY AND FIX THIS!
        try:
            if params_dict['data']['getStatus\r\n']:
                if not current_bmk in current_buks_list:
                    current_buks_list.append(current_bmk)
                    redraw_bmk_window(params_dict)
                redraw_window_table(params_dict)
                manage_error_in_get_status(current_bmk, params_dict)
                dpg.set_item_user_data(f"bmk_{current_bmk}", params_dict)
            else:
                current_buks_list = find_false(current_bmk, current_buks_list)
        except KeyError:
            if params_dict['data']['gPr\r\n']:
                redraw_pr_plot(params_dict['data']['gPr\r\n'])
            else:
                dpg.delete_item(f'line_{current_bmk}')
                dpg.draw_line(parent=f"BMK:{current_bmk}", p1=(0, 50), p2=(
                    150, 50), thickness=4, color=(255, 0, 255, 255), tag=f'line_{current_bmk}')
    blick_line_if_error(current_buks_list)


def manage_error_in_get_status(current_bmk: str, params_dict: dict[str, dict[str, dict[str, str]]]) -> None:
    if int(params_dict['data']['getStatus\r\n']['Err']):
        if not dpg.get_value(f"line_err{current_bmk}"):
            dpg.set_value(f"line_err{current_bmk}", True)
        dpg.set_item_user_data(f"err_{current_bmk}", params_dict)
    else:
        if dpg.get_value(f"line_err{current_bmk}"):
            dpg.set_value(f"line_err{current_bmk}", False)


def find_false(current_bmk: str, current_buks_list: list[str]) -> list[str]:
    # dpg.delete_item(f'line_{current_bmk}')
    # dpg.draw_line(parent =f"BMK:{current_bmk}", p1 = (0, 50), p2= (150, 50), thickness=4, color=(255, 0, 255, 255), tag =f'line_{current_bmk}')
    dpg.delete_item(f'line_bmk_{current_bmk}')
    dpg.draw_line(parent=f"BMK:{current_bmk}", p1=(75, 65), p2=(
        110, 65), thickness=10, color=(255, 0, 255, 255), tag=f'line_bmk_{current_bmk}')
    if dpg.get_value(f"line_err{current_bmk}"):
        dpg.set_value(f"line_err{current_bmk}", False)
    dpg.set_item_callback(f'bmk_{current_bmk}', callback=empty_callback)
    dpg.set_item_callback(f'err_{current_bmk}', callback=empty_callback)
    dpg.set_item_callback(f'pr_{current_bmk}', callback=empty_callback)
    # dpg.bind_item_handler_registry(f'text_{current_bmk}', "empty")
    if current_bmk in current_buks_list:
        current_buks_list.pop(current_buks_list.index(current_bmk))
    return current_buks_list


def blick_line_if_error(current_buks_list: list[str]) -> None:
    if dpg.get_value("cnt") == 60:
        for bmk in current_buks_list:
            if dpg.get_value(f"line_err{bmk}"):
                dpg.delete_item(f'line_bmk_{bmk}')
                dpg.draw_line(parent=f"BMK:{bmk}", p1=(75, 65), p2=(
                    110, 65), thickness=10, color=(255, 0, 0, 255), tag=f'line_bmk_{bmk}')
    if dpg.get_value("cnt") == 120:
        for bmk in current_buks_list:
            if dpg.get_value(f"line_err{bmk}"):
                dpg.delete_item(f'line_bmk_{bmk}')
                dpg.draw_line(parent=f"BMK:{bmk}", p1=(75, 65), p2=(
                    110, 65), thickness=10, color=(0, 0, 255, 255), tag=f'line_bmk_{bmk}')

    dpg.set_value("cnt", dpg.get_value('cnt') + 1)
    if dpg.get_value('cnt') > 120:
        dpg.set_value('cnt', 0)


def redraw_window_table(params: dict[str, dict[str, dict[str, str]]]) -> None:
    bmk: str = str(params['bmk'])
    data_for_table = params['data']['getStatus\r\n']
    if not data_for_table:
        return
    if dpg.does_item_exist(f"MT_{bmk}"):
        for i in range(len(list(data_for_table)) - 1):
            if i == 14 or i == 5:
                continue
            elif i == 6:
                dpg.set_value(f"row{bmk}_{i}", str(data_for_table[list(data_for_table)[6]])[
                              0] + str(data_for_table[list(data_for_table)[6]])[1:-1] + '.'+str(data_for_table[list(data_for_table)[i]])[3:])
            elif i == 16:
                dpg.set_value(f"row{bmk}_{i}", data_for_table[list(data_for_table)[
                              16]][0] + str(int(data_for_table[list(data_for_table)[16]][1:])))
            elif i == 20:
                dpg.set_value(f"row{bmk}_{i}", styp_torm(
                    data_for_table[list(data_for_table)[20]]))
            elif i == 21:
                dpg.set_value(f"row{bmk}_{i}", state_l(
                    data_for_table[list(data_for_table)[21]]))
            elif i == 22:
                dpg.set_value(f"row{bmk}_{i}", data_for_table[list(data_for_table)[22]][0] + str(
                    data_for_table[list(data_for_table)[22]])[1:-1] + '.'+str(data_for_table[list(data_for_table)[22]])[3:])
            elif i == 15:
                dpg.set_value(f"row{bmk}_{i}", str(
                    int(data_for_table[list(data_for_table)[15]])) + "B")
            elif i == 19 or i == 18:
                dpg.set_value(f"row{bmk}_{i}",
                              data_for_table[list(data_for_table)[i]])
            else:
                dpg.set_value(f"row{bmk}_{i}", int(
                    data_for_table[list(data_for_table)[i]]))


i: int = 0


def redraw_pr_plot(data: dict[str, str]) -> None:
    global i, list_for_plot_y1, list_for_plot_y2, list_for_plot_x
    if dpg.does_item_exist("plot_win"):
        if dpg.is_item_visible("plot_win"):
            i += 1
            list_for_plot_y1.append(int(data['pr0']))
            list_for_plot_y2.append(int(data['pr1']))
            list_for_plot_x.append(i*10)
            dpg.set_value("series_tag1", [list_for_plot_x, list_for_plot_y1])
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


def redraw_bmk_window(params_dict: dict[str, dict[str, dict[str, str]]]) -> None:
    bmk: str = str(params_dict['bmk'])
    dpg.delete_item(f'line_{bmk}')
    dpg.draw_line(parent=f"BMK:{bmk}", p1=(0, 53), p2=(
        200, 53), thickness=4, color=(0, 0, 0, 255), tag=f'line_{bmk}')
    dpg.delete_item(f'line_bmk_{bmk}')
    dpg.draw_line(parent=f"BMK:{bmk}", p1=(75, 65), p2=(
        110, 65), thickness=10, color=(0, 0, 255, 255), tag=f'line_bmk_{bmk}')
    dpg.set_item_callback(f'bmk_{bmk}', callback=draw_window_table)
    dpg.set_item_callback(f'err_{bmk}', callback=err_callback)
    dpg.set_item_callback(f'pr_{bmk}', callback=create_plot)
    dpg.set_item_user_data(f'bmk_{bmk}', params_dict)
    dpg.set_item_user_data(f'err_{bmk}', params_dict)


def draw_bmk_window_at_runtime(q_task: Queue) -> None:
    for bmk in list_of_bmk.keys():
        with dpg.window(tag=f"BMK:{bmk}", pos=win_pos, no_background=True, no_resize=True, no_close=True, no_title_bar=True, autosize=True, no_move=True, no_collapse=True):
            dpg.add_button(label=" ИНФ.", tag=f"bmk_{bmk}", pos=(7, 18))
            dpg.add_button(
                label="ДАВЛ.", tag=f'pr_{bmk}', user_data=q_task, pos=(70, 18))
            dpg.add_button(label="ОШИБ.", tag=f"err_{bmk}", pos=(133, 18))
            dpg.add_text(f"{list_of_bmk[bmk]}",
                         pos=(75, 40), tag=f'text_{bmk}')
            dpg.draw_line(p1=(0, 53), p2=(200, 53), thickness=4,
                          color=(0, 0, 0, 255), tag=f'line_{bmk}')
            dpg.draw_line(p1=(75, 65), p2=(110, 65), thickness=10,
                          color=(255, 0, 255, 255), tag=f'line_bmk_{bmk}')
        win_pos[0] += 200
        current_index_bmk = (list(list_of_bmk.keys()).index(bmk) + 1)
        if current_index_bmk == 2 or current_index_bmk == 4 or current_index_bmk == 7 or current_index_bmk == 10:
            win_pos[1] += 100
            win_pos[0] = 400


def main_window(q: Queue, q_task: Queue, p1: Process) -> None:
    dpg.create_context()

    with dpg.window(tag="Main window", no_scrollbar=True, no_focus_on_appearing=False, no_resize=False, no_move=True, autosize=False):
        with dpg.menu_bar():
            with dpg.menu(label="Настроить БМК"):
                for bmk in list_of_bmk.keys():
                    with dpg.menu(label=f'Настроить {list_of_bmk[bmk]}'):
                        dpg.add_button(
                            label="Установить темепературу включения подогрева")
                        dpg.add_button(label="Установить давление по ступеням")
                        dpg.add_button(
                            label="Установить колибровачные значения дла датчиков давления")

            dpg.add_menu_item(label="Помощь")
            with dpg.menu(label="О программе"):
                dpg.add_text(default_value="""Разработано в ЦКЖТ в 2023 году
Разработчик Волков Егор Алексеевич 
По всем вопросам обращаться по адресу: gole00201@gmail.com""")

    draw_bmk_window_at_runtime(q_task)
    draw_scheme_at_run_time()

    dpg.bind_theme(create_theme_imgui_light())


    dpg.set_primary_window("Main window", True)
    dpg.create_viewport(title="STP ARS-4", width=1980, height=1024,
                        resizable=True, min_width=1000, min_height=800)

    with dpg.value_registry():
        for bmk in list_of_bmk.keys():
            dpg.add_bool_value(tag=f"line_err{bmk}", default_value=False)
            dpg.add_bool_value(tag=f"line_cnt{bmk}", default_value=True)
        dpg.add_int_value(tag=f"cnt", default_value=- 120)

    with dpg.theme(tag="ser1_theme"):
        with dpg.theme_component(dpg.mvLineSeries):
            dpg.add_theme_color(dpg.mvPlotCol_Line, (0, 255, 0),
                                category=dpg.mvThemeCat_Plots)
    with dpg.theme(tag="ser2_theme"):
        with dpg.theme_component(dpg.mvLineSeries):
            dpg.add_theme_color(dpg.mvPlotCol_Line, (255, 0, 0),
                                category=dpg.mvThemeCat_Plots)

    with dpg.font_registry():
        with dpg.font("./fonts/Cousine-Bold.ttf", 18, default_font=True, tag='Main_font'):
            dpg.add_font_range_hint(dpg.mvFontRangeHint_Cyrillic)
        with dpg.font("./fonts/Cousine-Regular.ttf", 15, default_font=True, tag='table_font'):
            dpg.add_font_range_hint(dpg.mvFontRangeHint_Cyrillic)
        with dpg.font("./fonts/Cousine-Bold.ttf", 25, default_font=True, tag='lable_font'):
            dpg.add_font_range_hint(dpg.mvFontRangeHint_Cyrillic)
        with dpg.font("./fonts/Cousine-Bold.ttf", 18, default_font=True, tag='time_font'):
            dpg.add_font_range_hint(dpg.mvFontRangeHint_Cyrillic)

    dpg.bind_item_font("TIME", "time_font")
    dpg.bind_item_font("Main lable", "lable_font")
    dpg.bind_font('Main_font')
    # dpg.set_viewport
    dpg.setup_dearpygui()
    dpg.show_viewport()
    # dpg.show_style_editor()
    # dpg.show_metrics()

    while dpg.is_dearpygui_running():
        if q.qsize() > 1000:  # ЕСЛИ СЛИШКОМ ДОЛГО ОКНО БЫЛО СВЕРНУТО, ТО ВОТ ТЕБЕ ПРОПУСК В ГРАФИКЕ
            while not q.empty():
                q.get()
        print_real_time()
        show_bmk_windows(q)
        dpg.render_dearpygui_frame()

    p1.kill()
    dpg.destroy_context()


if __name__ == '__main__':
    q = Queue()
    q_task = Queue()
    p1 = Process(target=bmk_emulator, args=(q, q_task))
    p2 = Process(target=main_window, args=(q, q_task, p1))
    p1.start()
    p2.start()
