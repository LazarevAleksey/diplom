import dearpygui.dearpygui as dpg
from .misc import *
def draw_scheme_at_run_time() -> None:
    windows_bmk_pos: list[list[int]] = []
    for bmk in list_of_bmk.keys():
        windows_bmk_pos.append(dpg.get_item_pos(f"BMK:{bmk}"))
    w, h, c, d = dpg.load_image('./img/post.png')
    with dpg.texture_registry(show=False):
        dpg.add_static_texture(width=w, height=h, default_value=d, tag="post_tag")

    dpg.add_text(parent="Main window", pos=(
        470, 40), default_value="СТП АРС-4",       color=(0, 0, 0, 255), tag="Main lable")
    with dpg.window(tag=f"TIME", pos=(480, 60), no_background=True, no_resize=True, no_close=True, no_title_bar=True, min_size=(60, 60), height=60, no_move=True):
        dpg.add_text(tag='time_tag', pos=(15, 3),
                     default_value="TIME", color=(0, 0, 0, 255))
    dpg.draw_line(parent="Main window", p1=(480, 42), p2=(570, 42), thickness=20, color=(
        int(0.70 * 255), int(1.00 * 255), int(0.70 * 255), int(1.00 * 255)))

    dpg.add_image(parent="Main window", texture_tag='post_tag',
                  pos=(350, 570), width=300, height=200)
    dpg.add_text(parent="Main window", pos=(180, 60),
                 default_value="МОСКВА",          color=(0, 0, 0, 255))
    dpg.add_text(parent="Main window", pos=(740, 60),
                 default_value="САНКТ-ПЕТЕРБУРГ", color=(0, 0, 0, 255))
    dpg.add_text(parent="Main window", pos=(
        180, windows_bmk_pos[2][1] - 20), default_value="107СПУ")
    dpg.add_text(parent="Main window", pos=(
        280, windows_bmk_pos[2][1] + 5), default_value="107")
    dpg.add_text(parent="Main window", pos=(
        100, windows_bmk_pos[7][1] - 20), default_value="106-119СПУ")
    dpg.add_text(parent="Main window", pos=(
        210, windows_bmk_pos[7][1] - 20), default_value="119-120АПУ")
    dpg.add_text(parent="Main window", pos=(
        280, windows_bmk_pos[7][1] + 5), default_value="120")
    dpg.add_text(parent="Main window", pos=(
        140, windows_bmk_pos[7][1] + 5), default_value="119")
    dpg.draw_arrow(parent="Main window", p1=(100, 50), p2=(
        300, 50), thickness=3, color=(0, 0, 0, 255))
    dpg.draw_arrow(parent="Main window", p1=(900, 50), p2=(
        700, 50), thickness=3, color=(0, 0, 0, 255))
    dpg.draw_line(parent="Main window", p1=(90,  windows_bmk_pos[2][1] - 25), p2=(
        300, windows_bmk_pos[2][1] - 25), thickness=4, color=(0, 0, 0, 255))
    dpg.draw_line(parent="Main window", p1=(300, windows_bmk_pos[2][1] - 25), p2=(
        windows_bmk_pos[0][0], windows_bmk_pos[0][1] + 29), thickness=4, color=(0, 0, 0, 255))
    dpg.draw_line(parent="Main window", p1=(300, windows_bmk_pos[2][1] - 25), p2=(
        windows_bmk_pos[2][0], windows_bmk_pos[2][1] + 30), thickness=4, color=(0, 0, 0, 255))
    dpg.draw_line(parent="Main window", p1=(300, windows_bmk_pos[7][1] - 25), p2=(
        windows_bmk_pos[4][0], windows_bmk_pos[4][1] + 29), thickness=4, color=(0, 0, 0, 255))
    dpg.draw_line(parent="Main window", p1=(300, windows_bmk_pos[7][1] - 25), p2=(
        windows_bmk_pos[7][0], windows_bmk_pos[7][1] + 29), thickness=4, color=(0, 0, 0, 255))
    dpg.draw_line(parent="Main window", p1=(160, windows_bmk_pos[7][1] - 25), p2=(
        windows_bmk_pos[10][0], windows_bmk_pos[10][1] + 29), thickness=4, color=(0, 0, 0, 255))
    dpg.draw_line(parent="Main window", p1=(90,  windows_bmk_pos[7][1] - 25), p2=(
        300, windows_bmk_pos[7][1] - 25), thickness=4, color=(0, 0, 0, 255))
    for i in range(len(windows_bmk_pos)):
        if i == 1 or i == 3 or i == 6 or i == 9 or i == 11:
            dpg.draw_line(parent="Main window", p1=(400, windows_bmk_pos[i][1] + 29), p2=(
                900, windows_bmk_pos[i][1] + 29), thickness=4, color=(0, 0, 0, 255))

