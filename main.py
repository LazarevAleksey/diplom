
import dearpygui.dearpygui as dpg
import backend.backend_parser as parser
import backend.backend_serial as ser



dpg.create_context()
dpg.create_viewport(title= "VUP-15z", width= 800, height= 600)

def button1_callback(): 
    print(ser.send_command('007','getStatus'))
    print(parser.get_status_params_map)

with dpg.window(label="Test arduino"):
    dpg.add_button(label='getStatus', callback= button1_callback, user_data= 'User data')

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()

