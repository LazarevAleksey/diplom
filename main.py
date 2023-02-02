# For GUI we chose dear pygui. For each of BUKs we made a different window, and show all
# data in tables. For each of commands we made different button that callback
# a function to create a context menu of command.  

import dearpygui.dearpygui as dpg
import backend.backend_parser as parser
import backend.backend_serial as ser



dpg.create_context()
dpg.create_viewport(title= "VUP-15z", width= 800, height= 600)

def button1_callback(): 
    print(ser.send_command('007','getStatus'))
    dpg.delete_item('MT')
    with dpg.table(parent='main', tag= 'MT', header_row= False, width= 300):
        dpg.add_table_column()
        dpg.add_table_column()
        for i in range(0,25):
            with dpg.table_row(parent='MT', tag=f'row_{i}'):
                dpg.add_text(list(parser.get_status_params)[i])
                dpg.add_text(parser.get_status_params_map[list(parser.get_status_params)[i]])

with dpg.window(tag='main', label="Test arduino", width= 300, height= 600):
    dpg.add_button(tag='gSt',width=300, label='getStatus', callback= button1_callback, user_data= 'User data')
    with dpg.table(tag='MT', header_row= False, width= 300):
        dpg.add_table_column()
        dpg.add_table_column()
        for i in range(0,25):
            with dpg.table_row():
                dpg.add_text(list(parser.get_status_params)[i])
                dpg.add_text(parser.get_status_params_map[list(parser.get_status_params)[i]])

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()

