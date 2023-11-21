import dearpygui.dearpygui as dpg
import math
dpg.create_context()

Pi = math.pi
n = 7  # параметр для поворота вправо ветви (чем он больше, тем угол меньше)
m = 5  # параметр для поворота влево ветви (чем он больше, тем угол меньше)
min = 5  # минимальная длина ветви
t = 200  # длина ствола


def Draw(x, y, t, a, drawlist):
    if t > min:
        t *= 0.75  # уменьшаем длину ветви
        dpg.draw_line((x, y), (x + t * math.cos(a), y - t * math.sin(a)), color=(255, 255, 255))
        x = x + t * math.cos(a)
        y = y - t * math.sin(a)
        Draw(x, y, t, a + Pi / n, drawlist)
        Draw(x, y, t, a - Pi / m, drawlist)


dpg.create_viewport(width=800, height=700, title='The Pythagoras tree')
with dpg.window(label="Дерево", tag='Window', width=800, height=700):
    with dpg.drawlist(width=800, height=680) as drawlist:
        Draw(375, 600, t, Pi / 2, drawlist)

dpg.set_primary_window("Window", True)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
