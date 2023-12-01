import dearpygui.dearpygui as dpg
import math
from timeit import default_timer as timer

start_time = timer()

def dragon(x1, y1, x2, y2, depth, canvas):
    def paint(x1, y1, x2, y2, k):
        if k == 0:
            dpg.draw_line([x1, y1], [x2, y2], parent=canvas, color=[255, 255, 255])
        else:
            tx = (x1 + x2) // 2 + (y2 - y1) // 2
            ty = (y1 + y2) // 2 - (x2 - x1) // 2
            paint(x2, y2, tx, ty, k - 1)
            paint(x1, y1, tx, ty, k - 1)

    paint(x1, y1, x2, y2, depth)

dpg.create_context()
dpg.create_viewport(title='Dragon Curve', width=750, height=750, vsync=False)

fps_text = dpg.generate_uuid()
dragon_depth = 14

with dpg.window(tag="Window"):
    dpg.add_text("FPS: ", tag=fps_text)
    with dpg.drawlist(width=750, height=750):
        dragon(50, 350, 650, 350, dragon_depth, dpg.last_item())

dpg.set_primary_window("Window", True)
dpg.setup_dearpygui()
dpg.show_viewport()

frame_count = 0
while dpg.is_dearpygui_running():
    dpg.render_dearpygui_frame()
    frame_count += 1
    elapsed_time = timer() - start_time
    if elapsed_time > 1.0:
        fps = frame_count / elapsed_time
        dpg.set_value(fps_text, f"FPS: {fps:.2f}")
        start_time = timer()
        frame_count = 0

dpg.destroy_context()
