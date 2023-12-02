import dearpygui.dearpygui as dpg
from timeit import default_timer as timer

start_time = timer()

dpg.create_context()
def draw_sierpinski(drawlist, level, x1, y1, x2, y2, x3, y3):
    if level > 0:
        mid_x1 = (x1 + x2) / 2
        mid_y1 = (y1 + y2) / 2
        mid_x2 = (x2 + x3) / 2
        mid_y2 = (y2 + y3) / 2
        mid_x3 = (x3 + x1) / 2
        mid_y3 = (y3 + y1) / 2
        dpg.draw_triangle((mid_x1, mid_y1), (mid_x2, mid_y2), (mid_x3, mid_y3), fill=(0, 0, 0))
        draw_sierpinski(drawlist, level - 1, x1, y1, mid_x1, mid_y1, mid_x3, mid_y3)
        draw_sierpinski(drawlist, level - 1, mid_x1, mid_y1, x2, y2, mid_x2, mid_y2)
        draw_sierpinski(drawlist, level - 1, mid_x3, mid_y3, mid_x2, mid_y2, x3, y3)


fps_text = dpg.generate_uuid()

dpg.create_viewport(title='The Sierpinski triangle', width=1960, height=1080, vsync=False)

with dpg.window(tag="Primary Window"):
    text_container = dpg.add_text("FPS: ")
    with dpg.drawlist(width=1960, height=1000):
        dpg.draw_triangle((200, 50), (1000, 50), (600, 800), fill=(255, 255, 255))
        draw_sierpinski(dpg.drawlist, 6, 200, 50, 1000, 50, 600, 800) # You can change the depth here

dpg.set_primary_window("Primary Window", True)
dpg.setup_dearpygui()
dpg.show_viewport()

frame_count = 0
while dpg.is_dearpygui_running():
    dpg.render_dearpygui_frame()
    frame_count += 1
    elapsed_time = timer() - start_time
    if elapsed_time > 1.0:
        fps = frame_count / elapsed_time
        dpg.set_value(text_container, f"FPS: {fps:.2f}")
        start_time = timer()
        frame_count = 0

dpg.destroy_context()
