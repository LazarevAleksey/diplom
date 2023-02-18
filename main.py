# For GUI we chose dear pygui. For each of BUKs we made a different window, and show all
# data in tables. For each of commands we made different button that callback
# a function to create a context menu of command.

import dearpygui.dearpygui as dpg
import backend.backend_parser as parser
import backend.backend_serial as ser
from threading import Thread

def com_sending() -> None:
    while True:
        print(ser.send_command('007', 'getStatus'))

def butn_callback() -> None:
    print(parser.check_err(parser.get_status_params_map['Err']))

def main_window() -> None:        
    dpg.create_context()
    dpg.create_viewport(title="VUP-15z", width=800, height=600)
    dpg.setup_dearpygui()
    with dpg.window(tag='main', label="Test arduino", width=300, height=600):
        dpg.add_button(callback= butn_callback)
        with dpg.table(tag='MT', header_row=False, width=300):
            dpg.add_table_column()
            dpg.add_table_column()
            for i in range(0, 25):
                with dpg.table_row():
                    dpg.add_text(list(parser.get_status_params)[i])
                    dpg.add_text(parser.get_status_params_map[list(
                        parser.get_status_params)[i]])   
    dpg.show_viewport()
    while dpg.is_dearpygui_running():
        dpg.delete_item('MT')
        with dpg.table(parent='main', tag='MT', header_row=False, width=300):
            dpg.add_table_column()
            dpg.add_table_column()
            for i in range(0, 25):
                with dpg.table_row(parent='MT', tag=f'row_{i}'):
                    dpg.add_text(list(parser.get_status_params)[i])
                    dpg.add_text(parser.get_status_params_map[list(
                        parser.get_status_params)[i]])
        dpg.render_dearpygui_frame()
    dpg.destroy_context()


if __name__ == "__main__":
    t1 = Thread(target= com_sending)
    t2 = Thread(target= main_window)
    t1.daemon = True
    t2.daemon = True
    t1.start()
    t2.start()
    while True:
        pass
