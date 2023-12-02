import dearpygui.dearpygui as dpg
import time


def julia_fractal(z, c):
    for i in range(100):
        z = z * z + c
        if abs(z) > 2.0:
            return i
    return 100

dpg.create_context()
dpg.create_viewport(title='Julia Fractal', width=800, height=600)
dpg.set_viewport_vsync(False)
dpg.setup_dearpygui()
dpg.show_viewport()


frame_count = 0
last_fps_update_time = time.time()

with dpg.window(label="Julia Fractal", width=800, height=600):
    with dpg.drawlist(width=800, height=600):
        for x in range(800):
            for y in range(600):
                zx = (x - 400) / 200.0
                zy = (y - 300) / 200.0
                c = complex(-0.8, 0.156)
                z = complex(zx, zy)
                value = julia_fractal(z, c)
                color_value = int(value / 100 * 255)
                color = (color_value, color_value, color_value, 255)
                dpg.draw_circle((x, y), 1, color=color)

def on_render():
    global frame_count, last_fps_update_time
    frame_count += 1
    current_time = time.time()
    if current_time - last_fps_update_time > 1.0: 
        fps = frame_count / (current_time - last_fps_update_time)
        dpg.set_viewport_title(f'Julia Fractal,   {fps:.2f}')
        frame_count = 0
        last_fps_update_time = current_time





while dpg.is_dearpygui_running():
    on_render()
    dpg.render_dearpygui_frame()

dpg.destroy_context()