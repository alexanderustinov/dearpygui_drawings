import dearpygui.dearpygui as dpg
import numpy as np

MAX_ITER = 50
TOLERANCE = 1e-6
ROOTS = [1, np.exp(2j * np.pi / 3), np.exp(4j * np.pi / 3)]


def newton_fractal(x, y, max_iter=MAX_ITER, tolerance=TOLERANCE):
    z = complex(x, y)

    for i in range(max_iter):
        derivative = 3 * z ** 2 - 1
        z = z - (z ** 3 - 1) / derivative
        for j, root in enumerate(ROOTS):
            if abs(z - root) < tolerance:
                return j

    return -1


def calculate_pixel_color(x, y, width, height):
    normalized_x = (x - width / 2) / (width / 4)
    normalized_y = (y - height / 2) / (height / 4)
    color_index = newton_fractal(normalized_x, normalized_y)
    return color_index


def draw_fractal(width, height):
    for x in range(width):
        for y in range(height):
            color_index = calculate_pixel_color(x, y, width, height)
            if color_index != -1:
                color = [(255 if i == color_index else 0) for i in range(3)]
                dpg.draw_circle((x, y), 1, color=color)


dpg.create_context()

with dpg.window(label='Newton Fractal', width=800, height=600):
    with dpg.drawlist(width=800, height=600):
        draw_fractal(800, 600)

dpg.create_viewport(title='Newton Fractal', width=800, height=600)

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()

dpg.destroy_context()
