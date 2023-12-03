import dearpygui.dearpygui as dpg
import math
from timeit import default_timer as timer


start_time = timer()

dpg.create_context()

Pi = math.pi
n = 8  # параметр для поворота вправо ветви (чем он больше, тем угол меньше)
m = 5  # параметр для поворота влево ветви (чем он больше, тем угол меньше)
min = 5  # минимальная длина ветви
t = 250  # длина ствола

def Draw(x, y, t, a, drawlist, thik):
    if t > min:
        t *= 0.75  # уменьшаем длину ветви
        thik *= 0.8
        dpg.draw_line((x, y), (x + t * math.cos(a), y - t * math.sin(a)), color=(255, 255, 255), thickness=thik)
        x = x + t * math.cos(a)
        y = y - t * math.sin(a)
        Draw(x, y, t, a + Pi / n, drawlist, thik),
        Draw(x, y, t, a - Pi / m, drawlist, thik)

fps_text = dpg.generate_uuid()

dpg.create_viewport(width=1000, height=900, title='The Pythagoras tree', vsync=False)
with dpg.window(label="Дерево", tag='Window', width=800, height=700):
    dpg.add_text("FPS: ", tag=fps_text)
    with dpg.drawlist(width=1000, height=850) as drawlist:
        Draw(450, 750, t, Pi / 2, drawlist, 20)

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
