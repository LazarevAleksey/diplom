# For GUI we chose dear pygui. For each of BUKs we made a different window, and show all
# data in tables. For each of commands we made different button that callback
# a function to create a context menu of command.

import dearpygui.dearpygui as dpg
import backend.backend_parser as parser
import backend.backend_serial as ser
from multiprocessing import Process, Queue
import time
# Setup 4th sort mountain
win_pos: list[int] = [0, 25]
current_buks_list: list[str] = []
list_of_bmk: dict[str, str] = {'009':'STP14' , '010':'STP13', '011':'STP12', '012':'STP11', '013':'STP10', '014':'STP22', '015':'STP09'}
list_of_control_com: list[str] = ['getStatus\r\n',
                                  'gPr\r\n', 'getDelta\r\n', 'getCount\r\n']

def create_theme_imgui_light() -> int:

    with dpg.theme() as theme_id:
        with dpg.theme_component(0):
            dpg.add_theme_color(dpg.mvThemeCol_WindowBg               , (191, 191, 191, 255))
            dpg.add_theme_color(dpg.mvThemeCol_Button                 , (1 * 255, 1 * 255, 1 * 255, 1 * 255))
            dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered          , (0 * 255, 1 * 255, 0 * 255, 1 * 255))
            dpg.add_theme_color(dpg.mvThemeCol_Text                   , (int(0.00 * 255), int(0.00 * 255), int(0.00 * 255), int(1.00 * 255)))
            dpg.add_theme_color(dpg.mvThemeCol_TextDisabled           , (int(0.60 * 255), int(0.60 * 255), int(0.60 * 255), int(1.00 * 255)))
            dpg.add_theme_color(dpg.mvThemeCol_ChildBg                , (int(0.00 * 255), int(0.00 * 255), int(0.00 * 255), int(0.00 * 255)))
            dpg.add_theme_color(dpg.mvThemeCol_PopupBg                , (int(1.00 * 255), int(1.00 * 255), int(1.00 * 255), int(0.98 * 255)))
            dpg.add_theme_color(dpg.mvThemeCol_Border                 , (int(191), int(191), int(191), int(191)))
            dpg.add_theme_color(dpg.mvThemeCol_BorderShadow           , (int(0.00 * 255), int(0.00 * 255), int(0.00 * 255), int(0.00 * 255)))
            dpg.add_theme_color(dpg.mvThemeCol_FrameBg                , (int(1.00 * 255), int(1.00 * 255), int(1.00 * 255), int(1.00 * 255)))
            dpg.add_theme_color(dpg.mvThemeCol_FrameBgHovered         , (int(0.26 * 255), int(0.59 * 255), int(0.98 * 255), int(0.40 * 255)))
            dpg.add_theme_color(dpg.mvThemeCol_FrameBgActive          , (int(0.26 * 255), int(0.59 * 255), int(0.98 * 255), int(0.67 * 255)))
            dpg.add_theme_color(dpg.mvThemeCol_TitleBg                , (int(0.96 * 255), int(0.96 * 255), int(0.96 * 255), int(1.00 * 255)))
            dpg.add_theme_color(dpg.mvThemeCol_TitleBgActive          , (int(0.82 * 255), int(0.82 * 255), int(0.82 * 255), int(1.00 * 255)))
            dpg.add_theme_color(dpg.mvThemeCol_TitleBgCollapsed       , (int(1.00 * 255), int(1.00 * 255), int(1.00 * 255), int(0.51 * 255)))
            dpg.add_theme_color(dpg.mvThemeCol_MenuBarBg              , (int(0.86 * 255), int(0.86 * 255), int(0.86 * 255), int(1.00 * 255)))
            dpg.add_theme_color(dpg.mvThemeCol_ScrollbarBg            , (int(0.98 * 255), int(0.98 * 255), int(0.98 * 255), int(0.53 * 255)))
            dpg.add_theme_color(dpg.mvThemeCol_ScrollbarGrab          , (int(0.69 * 255), int(0.69 * 255), int(0.69 * 255), int(0.80 * 255)))
            dpg.add_theme_color(dpg.mvThemeCol_ScrollbarGrabHovered   , (int(0.49 * 255), int(0.49 * 255), int(0.49 * 255), int(0.80 * 255)))
            dpg.add_theme_color(dpg.mvThemeCol_ScrollbarGrabActive    , (int(0.49 * 255), int(0.49 * 255), int(0.49 * 255), int(1.00 * 255)))
            dpg.add_theme_color(dpg.mvThemeCol_CheckMark              , (int(0.26 * 255), int(0.59 * 255), int(0.98 * 255), int(1.00 * 255)))
            dpg.add_theme_color(dpg.mvThemeCol_SliderGrab             , (int(0.26 * 255), int(0.59 * 255), int(0.98 * 255), int(0.78 * 255)))
            dpg.add_theme_color(dpg.mvThemeCol_SliderGrabActive       , (int(0.46 * 255), int(0.54 * 255), int(0.80 * 255), int(0.60 * 255)))
            dpg.add_theme_color(dpg.mvThemeCol_ButtonActive           , (int(0.70 * 255), int(1.00 * 255), int(0.70 * 255), int(1.00 * 255)))
            dpg.add_theme_color(dpg.mvThemeCol_Header                 , (int(0.26 * 255), int(0.59 * 255), int(0.98 * 255), int(0.31 * 255)))
            dpg.add_theme_color(dpg.mvThemeCol_HeaderHovered          , (int(0.26 * 255), int(0.59 * 255), int(0.98 * 255), int(0.80 * 255)))
            dpg.add_theme_color(dpg.mvThemeCol_HeaderActive           , (int(0.26 * 255), int(0.59 * 255), int(0.98 * 255), int(1.00 * 255)))
            dpg.add_theme_color(dpg.mvThemeCol_Separator              , (int(0.39 * 255), int(0.39 * 255), int(0.39 * 255), int(0.62 * 255)))
            dpg.add_theme_color(dpg.mvThemeCol_SeparatorHovered       , (int(0.14 * 255), int(0.44 * 255), int(0.80 * 255), int(0.78 * 255)))
            dpg.add_theme_color(dpg.mvThemeCol_SeparatorActive        , (int(0.14 * 255), int(0.44 * 255), int(0.80 * 255), int(1.00 * 255)))
            dpg.add_theme_color(dpg.mvThemeCol_ResizeGrip             , (int(0.35 * 255), int(0.35 * 255), int(0.35 * 255), int(0.17 * 255)))
            dpg.add_theme_color(dpg.mvThemeCol_ResizeGripHovered      , (int(0.26 * 255), int(0.59 * 255), int(0.98 * 255), int(0.67 * 255)))
            dpg.add_theme_color(dpg.mvThemeCol_ResizeGripActive       , (int(0.26 * 255), int(0.59 * 255), int(0.98 * 255), int(0.95 * 255)))
            dpg.add_theme_color(dpg.mvThemeCol_Tab                    , (int(0.76 * 255), int(0.80 * 255), int(0.84 * 255), int(0.93 * 255)))
            dpg.add_theme_color(dpg.mvThemeCol_TabHovered             , (int(0.26 * 255), int(0.59 * 255), int(0.98 * 255), int(0.80 * 255)))
            dpg.add_theme_color(dpg.mvThemeCol_TabActive              , (int(0.60 * 255), int(0.73 * 255), int(0.88 * 255), int(1.00 * 255)))
            dpg.add_theme_color(dpg.mvThemeCol_TabUnfocused           , (int(0.92 * 255), int(0.93 * 255), int(0.94 * 255), int(0.99 * 255)))
            dpg.add_theme_color(dpg.mvThemeCol_TabUnfocusedActive     , (int(0.74 * 255), int(0.82 * 255), int(0.91 * 255), int(1.00 * 255)))
            dpg.add_theme_color(dpg.mvThemeCol_DockingPreview         , (int(0.26 * 255), int(0.59 * 255), int(0.98 * 255), int(0.22 * 255)))
            dpg.add_theme_color(dpg.mvThemeCol_DockingEmptyBg         , (int(0.20 * 255), int(0.20 * 255), int(0.20 * 255), int(1.00 * 255)))
            dpg.add_theme_color(dpg.mvThemeCol_PlotLines              , (int(0.39 * 255), int(0.39 * 255), int(0.39 * 255), int(1.00 * 255)))
            dpg.add_theme_color(dpg.mvThemeCol_PlotLinesHovered       , (int(1.00 * 255), int(0.43 * 255), int(0.35 * 255), int(1.00 * 255)))
            dpg.add_theme_color(dpg.mvThemeCol_PlotHistogram          , (int(0.90 * 255), int(0.70 * 255), int(0.00 * 255), int(1.00 * 255)))
            dpg.add_theme_color(dpg.mvThemeCol_PlotHistogramHovered   , (int(1.00 * 255), int(0.45 * 255), int(0.00 * 255), int(1.00 * 255)))
            dpg.add_theme_color(dpg.mvThemeCol_TableHeaderBg          , (int(0.78 * 255), int(0.87 * 255), int(0.98 * 255), int(1.00 * 255)))
            dpg.add_theme_color(dpg.mvThemeCol_TableBorderStrong      , (int(0.57 * 255), int(0.57 * 255), int(0.64 * 255), int(1.00 * 255)))
            dpg.add_theme_color(dpg.mvThemeCol_TableBorderLight       , (int(0.68 * 255), int(0.68 * 255), int(0.74 * 255), int(1.00 * 255)))
            dpg.add_theme_color(dpg.mvThemeCol_TableRowBg             , (int(0.00 * 255), int(0.00 * 255), int(0.00 * 255), int(0.00 * 255)))
            dpg.add_theme_color(dpg.mvThemeCol_TableRowBgAlt          , (int(0.30 * 255), int(0.30 * 255), int(0.30 * 255), int(0.09 * 255)))
            dpg.add_theme_color(dpg.mvThemeCol_TextSelectedBg         , (int(0.26 * 255), int(0.59 * 255), int(0.98 * 255), int(0.35 * 255)))
            dpg.add_theme_color(dpg.mvThemeCol_DragDropTarget         , (int(0.26 * 255), int(0.59 * 255), int(0.98 * 255), int(0.95 * 255)))
            dpg.add_theme_color(dpg.mvThemeCol_NavHighlight           , (int(0.26 * 255), int(0.59 * 255), int(0.98 * 255), int(0.80 * 255)))
            dpg.add_theme_color(dpg.mvThemeCol_NavWindowingHighlight  , (int(0.70 * 255), int(0.70 * 255), int(0.70 * 255), int(0.70 * 255)))
            dpg.add_theme_color(dpg.mvThemeCol_NavWindowingDimBg      , (int(0.20 * 255), int(0.20 * 255), int(0.20 * 255), int(0.20 * 255)))
            dpg.add_theme_color(dpg.mvThemeCol_ModalWindowDimBg       , (int(0.20 * 255), int(0.20 * 255), int(0.20 * 255), int(0.35 * 255)))
            dpg.add_theme_color(dpg.mvPlotCol_FrameBg       , (int(1.00 * 255), int(1.00 * 255), int(1.00 * 255), int(1.00 * 255)), category=dpg.mvThemeCat_Plots)
            dpg.add_theme_color(dpg.mvPlotCol_PlotBg        , (int(0.42 * 255), int(0.57 * 255), int(1.00 * 255), int(0.13 * 255)), category=dpg.mvThemeCat_Plots)
            dpg.add_theme_color(dpg.mvPlotCol_PlotBorder    , (int(0.00 * 255), int(0.00 * 255), int(0.00 * 255), int(0.00 * 255)), category=dpg.mvThemeCat_Plots)
            dpg.add_theme_color(dpg.mvPlotCol_LegendBg      , (int(1.00 * 255), int(1.00 * 255), int(1.00 * 255), int(0.98 * 255)), category=dpg.mvThemeCat_Plots)
            dpg.add_theme_color(dpg.mvPlotCol_LegendBorder  , (int(0.82 * 255), int(0.82 * 255), int(0.82 * 255), int(0.80 * 255)), category=dpg.mvThemeCat_Plots)
            dpg.add_theme_color(dpg.mvPlotCol_LegendText    , (int(0.00 * 255), int(0.00 * 255), int(0.00 * 255), int(1.00 * 255)), category=dpg.mvThemeCat_Plots)
            dpg.add_theme_color(dpg.mvPlotCol_TitleText     , (int(0.00 * 255), int(0.00 * 255), int(0.00 * 255), int(1.00 * 255)), category=dpg.mvThemeCat_Plots)
            dpg.add_theme_color(dpg.mvPlotCol_InlayText     , (int(0.00 * 255), int(0.00 * 255), int(0.00 * 255), int(1.00 * 255)), category=dpg.mvThemeCat_Plots)
            dpg.add_theme_color(dpg.mvPlotCol_XAxis         , (int(0.00 * 255), int(0.00 * 255), int(0.00 * 255), int(1.00 * 255)), category=dpg.mvThemeCat_Plots)
            dpg.add_theme_color(dpg.mvPlotCol_XAxisGrid     , (int(1.00 * 255), int(1.00 * 255), int(1.00 * 255), int(1.00 * 255)), category=dpg.mvThemeCat_Plots)
            dpg.add_theme_color(dpg.mvPlotCol_YAxis         , (int(0.00 * 255), int(0.00 * 255), int(0.00 * 255), int(1.00 * 255)), category=dpg.mvThemeCat_Plots)
            dpg.add_theme_color(dpg.mvPlotCol_YAxisGrid     , (int(1.00 * 255), int(1.00 * 255), int(1.00 * 255), int(1.00 * 255)), category=dpg.mvThemeCat_Plots)
            dpg.add_theme_color(dpg.mvPlotCol_YAxis2        , (int(0.00 * 255), int(0.00 * 255), int(0.00 * 255), int(1.00 * 255)), category=dpg.mvThemeCat_Plots)
            dpg.add_theme_color(dpg.mvPlotCol_YAxisGrid2    , (int(0.00 * 255), int(0.00 * 255), int(0.00 * 255), int(0.50 * 255)), category=dpg.mvThemeCat_Plots)
            dpg.add_theme_color(dpg.mvPlotCol_YAxis3        , (int(0.00 * 255), int(0.00 * 255), int(0.00 * 255), int(1.00 * 255)), category=dpg.mvThemeCat_Plots)
            dpg.add_theme_color(dpg.mvPlotCol_YAxisGrid3    , (int(0.00 * 255), int(0.00 * 255), int(0.00 * 255), int(0.50 * 255)), category=dpg.mvThemeCat_Plots)
            dpg.add_theme_color(dpg.mvPlotCol_Selection     , (int(0.82 * 255), int(0.64 * 255), int(0.03 * 255), int(1.00 * 255)), category=dpg.mvThemeCat_Plots)
            dpg.add_theme_color(dpg.mvPlotCol_Query         , (int(0.00 * 255), int(0.84 * 255), int(0.37 * 255), int(1.00 * 255)), category=dpg.mvThemeCat_Plots)
            dpg.add_theme_color(dpg.mvPlotCol_Crosshairs    , (int(0.00 * 255), int(0.00 * 255), int(0.00 * 255), int(0.50 * 255)), category=dpg.mvThemeCat_Plots)
            dpg.add_theme_color(dpg.mvNodeCol_NodeBackground, (240, 240, 240, 255), category=dpg.mvThemeCat_Nodes)
            dpg.add_theme_color(dpg.mvNodeCol_NodeBackgroundHovered, (240, 240, 240, 255), category=dpg.mvThemeCat_Nodes)
            dpg.add_theme_color(dpg.mvNodeCol_NodeBackgroundSelected, (240, 240, 240, 255), category=dpg.mvThemeCat_Nodes)
            dpg.add_theme_color(dpg.mvNodeCol_NodeOutline, (100, 100, 100, 255), category=dpg.mvThemeCat_Nodes)
            dpg.add_theme_color(dpg.mvNodeCol_TitleBar, (248, 248, 248, 255), category=dpg.mvThemeCat_Nodes)
            dpg.add_theme_color(dpg.mvNodeCol_TitleBarHovered, (209, 209, 209, 255), category=dpg.mvThemeCat_Nodes)
            dpg.add_theme_color(dpg.mvNodeCol_TitleBarSelected, (209, 209, 209, 255), category=dpg.mvThemeCat_Nodes)
            dpg.add_theme_color(dpg.mvNodeCol_Link, (66, 150, 250, 100), category=dpg.mvThemeCat_Nodes)
            dpg.add_theme_color(dpg.mvNodeCol_LinkHovered, (66, 150, 250, 242), category=dpg.mvThemeCat_Nodes)
            dpg.add_theme_color(dpg.mvNodeCol_LinkSelected, (66, 150, 250, 242), category=dpg.mvThemeCat_Nodes)
            dpg.add_theme_color(dpg.mvNodeCol_Pin, (66, 150, 250, 160), category=dpg.mvThemeCat_Nodes)
            dpg.add_theme_color(dpg.mvNodeCol_PinHovered, (66, 150, 250, 255), category=dpg.mvThemeCat_Nodes)
            dpg.add_theme_color(dpg.mvNodeCol_BoxSelector, (90, 170, 250, 30), category=dpg.mvThemeCat_Nodes)
            dpg.add_theme_color(dpg.mvNodeCol_BoxSelectorOutline, (90, 170, 250, 150), category=dpg.mvThemeCat_Nodes)
            dpg.add_theme_color(dpg.mvNodeCol_GridBackground, (225, 225, 225, 255), category=dpg.mvThemeCat_Nodes)
            dpg.add_theme_color(dpg.mvNodeCol_GridLine, (180, 180, 180, 100), category=dpg.mvThemeCat_Nodes)

    return theme_id



def main_com_loop(q: Queue) -> None:
    ser.PORT = ser.avilable_com()
    commands_list:list[str] = []
    with ser.serial.Serial(ser.PORT, ser.BAUD, ser.BYTE_SIZE, ser.PARITY, ser.STOP_BITS, timeout=0.3) as port:
        while True:
            for bmk in list_of_bmk.keys():
                for command in list_of_control_com[:1]:
                    commands_list.append(ser.commands_generator(bmk, command).encode())       
                data = ser.send_command(commands_list, port)
                print({'bmk': f'{bmk}', 'data': data})
                q.put({'bmk': f'{bmk}', 'data': data})
                commands_list = []


def draw_window_table(sender:int, add_data:str ,user_data:dict[str, dict[str, str]]) -> None:
    bmk: str = user_data['bmk']
    data_for_table = user_data['data']['getStatus\r\n']
    if dpg.does_item_exist(f"INFO:{bmk}"):
        dpg.delete_item(f"INFO:{bmk}")
    with dpg.window(tag=f"INFO:{bmk}", label=f"Num. {bmk}", autosize= True):
        with dpg.table(tag=f"MT_{bmk}", header_row=False, width=300):
            dpg.add_table_column()
            dpg.add_table_column()
            for i in range(0, len(data_for_table.keys())):
                with dpg.table_row():
                    dpg.add_text(list(data_for_table)[i])
                    dpg.add_text(data_for_table[list(
                        data_for_table)[i]])


def show_bmk_windows(q: Queue) -> None:
    global current_buks_list
    if not q.empty():
        params_dict = q.get_nowait()
        current_bmk = params_dict['bmk']
        if params_dict['data']['getStatus\r\n']:
            if not current_bmk in current_buks_list:
                current_buks_list.append(current_bmk)
                redraw_bmk_window(params_dict)



def redraw_bmk_window(params_dict: dict[str, str]) -> None:
    global win_pos
    bmk:str = params_dict['bmk']
    new_pos = dpg.get_item_pos(f"BMK:{bmk}")
    dpg.delete_item(f"BMK:{bmk}")
    with dpg.window(tag=f"BMK:{bmk}", pos= new_pos, no_background= False, no_resize=True, no_close=True, no_title_bar=True, autosize=True):
        dpg.add_button(label= "BMK INFO", tag=f"bmk_{bmk}", pos = (7, 20), callback=draw_window_table, user_data= params_dict)
        dpg.add_button(label= "ERRORS", tag = f"err_{bmk}", pos = (100, 20))
        dpg.add_text(f"{list_of_bmk[bmk]}", pos= (60, 40))
        dpg.draw_line(p1 = (0, 50), p2= (150, 50), thickness=3, color=(0, 0, 0, 255), tag=f'line_{bmk}')

def draw_bmk_window_at_runtime() -> None:
    for bmk in list_of_bmk.keys():
        with dpg.window(tag=f"BMK:{bmk}", pos= win_pos, no_background= False, no_resize=True, no_close=True, no_title_bar=True, autosize=True):
            dpg.add_button(label= "BMK INFO", tag=f"bmk_{bmk}", pos = (7, 20))
            dpg.add_button(label= "ERRORS", tag = f"err_{bmk}", pos = (100, 20))
            dpg.add_text(f"{list_of_bmk[bmk]}", pos= (60, 40), tag=f'text_{bmk}')
            dpg.draw_line(p1 = (0, 50), p2= (150, 50), thickness=3, color=(255, 255, 0, 255), tag =f'line_{bmk}')
        win_pos[0] +=  150

def main_window(q: Queue) -> None:
    dpg.create_context()
    with dpg.window(tag = "Main window"):
        with dpg.menu_bar():
            dpg.add_menu_item(label="Help")
            dpg.add_menu_item(label="About")
    draw_bmk_window_at_runtime()
    dpg.bind_theme(create_theme_imgui_light())
    dpg.set_primary_window("Main window", True)

    dpg.create_viewport(title="VUP-15z", width=1980, height=1024)
    dpg.setup_dearpygui()
    dpg.show_viewport()
    # dpg.show_style_editor()

    while dpg.is_dearpygui_running():
        show_bmk_windows(q)
        dpg.render_dearpygui_frame()
    dpg.destroy_context()


if __name__ == '__main__':
    q = Queue()
    p1 = Process(target=main_com_loop, args=(q,))
    p2 = Process(target=main_window, args=(q,))
    p1.start()
    p2.start()
