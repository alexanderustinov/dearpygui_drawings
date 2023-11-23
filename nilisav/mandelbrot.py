import numpy as np
import dearpygui.dearpygui as dpg


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
    # create plot
    with dpg.plot(label="Mandelbrot set", height=600, width=700):

        for elem in c:
            for idx in elem:
                if is_correct(idx) is True:
                    dpg.add_plot_annotation(default_value=(idx.real, idx.imag), color=[255, 255, 255])
                if is_correct(idx) is False:
                    dpg.add_plot_annotation(default_value=(idx.real, idx.imag), color=[0, 0, 0])


dpg.create_viewport(title='HW7', width=700, height=650)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
