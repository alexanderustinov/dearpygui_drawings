import numpy as np
import dearpygui.dearpygui as dpg

from timeit import default_timer as timer

start_time = timer()

def is_correct(num, num__of_iterations=20):
    z = 0

    for _ in range(num__of_iterations):
        z = z ** 2 + num
        if abs(z) > 2:
            return False
    return True


def candidate_values(xmin, xmax, ymin, ymax, pixel_density):

    real = np.linspace(xmin, xmax, num=int((xmax - xmin) * pixel_density))
    imag = np.linspace(ymin, ymax, num=int((ymax - ymin) * pixel_density))

    xx, yy = np.meshgrid(real, imag)
    matrix = xx + 1j * yy

    return matrix


c = candidate_values(-2, 0.7, -1.2, 1.2, pixel_density=128)

dpg.create_context()

with dpg.window(label="Fractal"):
    fps_count = dpg.add_text("FPS: ")
    # create plot
    with dpg.plot(label="Mandelbrot set", height=600, width=700):

        for elem in c:
            for idx in elem:
                if is_correct(idx) is True:
                    dpg.add_plot_annotation(default_value=(idx.real, idx.imag), color=[255, 255, 255])
                if is_correct(idx) is False:
                    dpg.add_plot_annotation(default_value=(idx.real, idx.imag), color=[0, 0, 0])


dpg.create_viewport(title='HW7', width=700, height=650, vsync=False)
dpg.setup_dearpygui()
dpg.show_viewport()

frame_count = 0
while dpg.is_dearpygui_running():
    dpg.render_dearpygui_frame()
    frame_count += 1
    elapsed_time = timer() - start_time
    if elapsed_time > 1.0:
        fps = frame_count / elapsed_time
        dpg.set_value(fps_count, f"FPS: {fps:.2f}")
        start_time = timer()
        frame_count = 0

dpg.destroy_context()
