# For GUI we chose dear pygui. For each of BUKs we made a different window, and show all
# data in tables. For each of commands we made different button that callback
# a function to create a context menu of command.

import dearpygui.dearpygui as dpg
import backend.backend_parser as parser
import backend.backend_serial as ser
from multiprocessing import Process, Queue

# Setup 4th sort mountain
win_pos: int = 0
current_buks_list: list[str] = []
list_of_buks: list[str] = ['009', '255', '238', '221']
list_of_control_com: list[str] = ['getStatus\r\n',
                                  'gPr\r\n', 'getDelta\r\n', 'getCount\r\n']





def main_com_loop(q: Queue) -> None:
    # Sending commands to all buks (Process 1)
    ser.PORT = ser.avilable_com()
    while True:
        for buk_num in list_of_buks:
            for command in list_of_control_com:
                data = ser.send_command(buk_num, command)
                q.put(data)

def draw_window_table(params_dict: dict[str, str], w:int=300, h:int=600) -> None:
    global win_pos
    with dpg.window(tag=params_dict['bmk'], label=f"Num. {params_dict['bmk']}", width=w, height=h, pos=(win_pos, 0)):
        with dpg.table(tag=f"MT_{params_dict['bmk']}", header_row=False, width=300):
            dpg.add_table_column()
            dpg.add_table_column()
            for i in range(0, len(params_dict.keys())):
                with dpg.table_row():
                    dpg.add_text(list(params_dict)[i])
                    dpg.add_text(params_dict[list(
                        params_dict)[i]])
    win_pos += w

def show_data(q: Queue) -> None:
    # Drow a new window_table if cacth a new buk in Process 1
    global current_buks_list
    if not q.empty():
        params_dict = q.get_nowait()
        if params_dict:
            current_buk = params_dict['bmk']
            if not current_buk in current_buks_list:
                current_buks_list.append(current_buk)
                draw_window_table(params_dict)


def main_window(q: Queue) -> None:
    dpg.create_context()
    dpg.create_viewport(title="VUP-15z", width=1980, height=1024)
    dpg.setup_dearpygui()
    dpg.show_viewport()
    while dpg.is_dearpygui_running():
        show_data(q)
        dpg.render_dearpygui_frame()
    dpg.destroy_context()


if __name__ == '__main__':
    q = Queue()
    p1 = Process(target=main_com_loop, args=(q,))
    p2 = Process(target=main_window, args=(q,))
    p1.start()
    p2.start()
