import dearpygui.dearpygui as dpg
import datetime


list_of_bmk: dict[str, str] = {'009':'СТП 5' , '010':'СТП 6', '011':'СТП 7', '012':'СТП 8', 
                               '013':'СТП 9A', '014':'СТП 9', '015':'СТП 10', '016':'СТП 11A', 
                               '017':'СТП 11', '018':'СТП 12', '020':'СТП 13', '021':'СТП 14'}




def styp_torm(styp:str) ->str:
    if styp == '00':
        return "Нет ступени"
    if styp == '01':
        return "Оттормаживание"
    if styp == '02':
        return "Ступень 0,5"
    if styp == '03':
        return "Ступень 1,0"
    if styp == '04':
        return "Ступень 1,5"
    if styp == '05':
        return "Ступень 2,0"
    if styp == '06':
        return "Ступень 2,5"
    if styp == '07':
        return "Ступень 3,0"
    if styp == '08':
        return "Ступень 3,5"
    if styp == '09':
        return "Ступень 4,0"
    if styp == '10':
        return "Не распознанно"
    if styp == '11':
        #TODO: Log tihs!
        return "Ошибка"
    return ""

def state_l(s:str) ->str:
    if int(s) == 0:
        return "Цепи выключены"
    s_b = bin(int(s))
    s_out:str =""
    if s_b[2] == '1':
        s_out +="P "
    if s_b[3] == '1':
        s_out +="T4 "
    if s_b[4] == '1':
        s_out +="T3 "
    if s_b[5] == '1':
        s_out +="T2 "
    if s_b[6] == '1':
        s_out +="T1 "
    return s_out


def draw_info_table(bmk:str, data_for_table:dict[str, str]) -> None:
    with dpg.table_row(parent= f"MT_{bmk}"):
        dpg.add_text("БМК:")
        dpg.add_text(int(data_for_table[list(data_for_table)[0]]), tag=f"row{bmk}_{0}")
    with dpg.table_row(parent= f"MT_{bmk}"):
        dpg.add_text("БМКC:")
        dpg.add_text(int(data_for_table[list(data_for_table)[1]]), tag=f"row{bmk}_{1}")
    with dpg.table_row(parent= f"MT_{bmk}"):
        dpg.add_text("БМКCК:")
        dpg.add_text(int(data_for_table[list(data_for_table)[2]]), tag=f"row{bmk}_{2}")
    with dpg.table_row(parent= f"MT_{bmk}"):
        dpg.add_text("Давление (кПа):")
        dpg.add_text(int(data_for_table[list(data_for_table)[3]]), tag=f"row{bmk}_{3}")
    with dpg.table_row(parent= f"MT_{bmk}"):
        dpg.add_text("Давление 0 (кПа):")
        dpg.add_text(int(data_for_table[list(data_for_table)[4]]), tag=f"row{bmk}_{4}")
    with dpg.table_row(parent= f"MT_{bmk}"):
        dpg.add_text("Температура: 1")
        dpg.add_text(str(data_for_table[list(data_for_table)[6]])[0] + str(data_for_table[list(data_for_table)[6]])[1:-1] +'.'+str(data_for_table[list(data_for_table)[6]])[3:], tag=f"row{bmk}_{6}")
    with dpg.table_row(parent= f"MT_{bmk}"):
        dpg.add_text("Давление ступени 0,5 (кПа):")
        dpg.add_text(int(data_for_table[list(data_for_table)[7]]), tag=f"row{bmk}_{7}")
    with dpg.table_row(parent= f"MT_{bmk}"):
        dpg.add_text("Давление ступени 1,0 (кПа):")
        dpg.add_text(int(data_for_table[list(data_for_table)[8]]), tag=f"row{bmk}_{8}")
    with dpg.table_row(parent= f"MT_{bmk}"):
        dpg.add_text("Давление ступени 1,5 (кПа):")
        dpg.add_text(int(data_for_table[list(data_for_table)[9]]), tag=f"row{bmk}_{9}")
    with dpg.table_row(parent= f"MT_{bmk}"):
        dpg.add_text("Давление ступени 2,0 (кПа):")
        dpg.add_text(int(data_for_table[list(data_for_table)[10]]), tag=f"row{bmk}_{10}")
    with dpg.table_row(parent= f"MT_{bmk}"):
        dpg.add_text("Давление ступени 2,5 (кПа):")
        dpg.add_text(int(data_for_table[list(data_for_table)[11]]), tag=f"row{bmk}_{11}")
    with dpg.table_row(parent= f"MT_{bmk}"):
        dpg.add_text("Давление ступени 3,0 (кПа):")
        dpg.add_text(int(data_for_table[list(data_for_table)[12]]), tag=f"row{bmk}_{12}")
    with dpg.table_row(parent= f"MT_{bmk}"):
        dpg.add_text("Давление ступени 3,5 (кПа):")
        dpg.add_text(int(data_for_table[list(data_for_table)[13]]), tag=f"row{bmk}_{13}")
    with dpg.table_row(parent= f"MT_{bmk}"):
        dpg.add_text("Напряжение питания:")
        dpg.add_text(str(int(data_for_table[list(data_for_table)[15]])) + "B", tag=f"row{bmk}_{15}")
    with dpg.table_row(parent= f"MT_{bmk}"):
        dpg.add_text("Температура для вкл. обогрева:")
        dpg.add_text(data_for_table[list(data_for_table)[16]][0] + str(int(data_for_table[list(data_for_table)[16]][1:])), tag=f"row{bmk}_{16}")
    with dpg.table_row(parent= f"MT_{bmk}"):
        dpg.add_text("Время работы (C):")
        dpg.add_text(int(data_for_table[list(data_for_table)[17]]), tag=f"row{bmk}_{17}")
    with dpg.table_row(parent= f"MT_{bmk}"):
        dpg.add_text("Калибровка первого датчика:")
        dpg.add_text(data_for_table[list(data_for_table)[18]], tag=f"row{bmk}_{18}")
    with dpg.table_row(parent= f"MT_{bmk}"):
        dpg.add_text("Калибровка второго датчика:")
        dpg.add_text(data_for_table[list(data_for_table)[19]], tag=f"row{bmk}_{19}")
    with dpg.table_row(parent= f"MT_{bmk}"):
        dpg.add_text("Код ступени:")
        dpg.add_text(styp_torm(data_for_table[list(data_for_table)[20]]), tag=f"row{bmk}_{20}")
    with dpg.table_row(parent= f"MT_{bmk}"):
        dpg.add_text("Состояние управляющих цепей:")
        dpg.add_text(state_l(data_for_table[list(data_for_table)[21]]), tag=f"row{bmk}_{21}")
    with dpg.table_row(parent= f"MT_{bmk}"):
        dpg.add_text("Температура от второго датчика:")
        dpg.add_text(data_for_table[list(data_for_table)[22]][0] + str(data_for_table[list(data_for_table)[22]])[1:-1] +'.'+str(data_for_table[list(data_for_table)[22]])[3:], tag=f"row{bmk}_{22}")
    with dpg.table_row(parent= f"MT_{bmk}"):
        dpg.add_text("Общее время работы (Часы):")
        dpg.add_text(int(data_for_table[list(data_for_table)[23]]), tag=f"row{bmk}_{23}")
    





def print_real_time() ->None:
    c_t = datetime.datetime.now()
    time_str = c_t.strftime("%H:%M:%S")
    dpg.set_value(item="time_tag", value = time_str)




def create_theme_imgui_light():
    with dpg.theme() as theme_id:
        with dpg.theme_component(0):
            dpg.add_theme_color(dpg.mvThemeCol_WindowBg               , (191, 191, 191, 255))
            dpg.add_theme_color(dpg.mvThemeCol_Button                 , (1 * 255, 1 * 255, 1 * 255, 1 * 255))
            dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered          , (0 * 255, 1 * 255, 0 * 255, 1 * 255))
            dpg.add_theme_color(dpg.mvThemeCol_Text                   , (int(0.00 * 255), int(0.00 * 255), int(0.00 * 255), int(1.00 * 255)))
            dpg.add_theme_color(dpg.mvThemeCol_TextDisabled           , (int(0.60 * 255), int(0.60 * 255), int(0.60 * 255), int(1.00 * 255)))
            dpg.add_theme_color(dpg.mvThemeCol_ChildBg                , (int(0.00 * 255), int(0.00 * 255), int(0.00 * 255), int(0.00 * 255)))
            dpg.add_theme_color(dpg.mvThemeCol_PopupBg                , (int(1.00 * 255), int(1.00 * 255), int(1.00 * 255), int(0.98 * 255)))
            dpg.add_theme_color(dpg.mvThemeCol_Border                 , (int(0), int(0), int(0), int(191)))
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
            dpg.add_theme_color(dpg.mvPlotCol_PlotBg        , (int(0.0 * 255), int(0.0 * 255), int(0.00 * 255), int(1 * 255)), category=dpg.mvThemeCat_Plots)
            dpg.add_theme_color(dpg.mvPlotCol_PlotBorder    , (int(0.00 * 255), int(0.00 * 255), int(0.00 * 255), int(0.00 * 255)), category=dpg.mvThemeCat_Plots)
            dpg.add_theme_color(dpg.mvPlotCol_LegendBg      , (int(0.00 * 255), int(0.00 * 255), int(0.00 * 255), int(0 * 255)), category=dpg.mvThemeCat_Plots)
            dpg.add_theme_color(dpg.mvPlotCol_LegendBorder  , (int(0 * 255), int(0 * 255), int(0 * 255), int(1 * 255)), category=dpg.mvThemeCat_Plots)
            dpg.add_theme_color(dpg.mvPlotCol_LegendText    , (int(1.00 * 255), int(1.00 * 255), int(1.00 * 255), int(1.00 * 255)), category=dpg.mvThemeCat_Plots)
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
