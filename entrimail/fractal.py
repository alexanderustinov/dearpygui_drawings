import dearpygui.dearpygui as dpg
import numpy as np


def julia_fractal(z, c):
    for i in range(100):
        z = z * z + c
        if abs(z) > 2.0:
            return i
    return 100


dpg.create_context()


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

                
                dpg.draw_circle((x, y), 1,  color=color)


dpg.create_viewport(title='Julia Fractal', width=800, height=600)

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()


dpg.destroy_context()
