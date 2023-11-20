import dearpygui.dearpygui as dpg


WW, WH = 1000, 1000

dpg.create_context()
dpg.create_viewport(title='Vicsek fractal', width=WW, height=WH)


def draw_vicsek_fractal(level=4, x=0, y=0, size=100, vertical=False, fill=True, fill_color=[255,255,255], color=[255,255,255]):
    if level == 0:
        if fill:
            dpg.draw_rectangle([x, y], [x+size, y+size], parent="root node", fill=fill_color, color=color, thickness=2)
        else:
            dpg.draw_rectangle([x, y], [x+size, y+size], parent="root node", color=color, thickness=2)

    else:
        size3 = size / 3
        for i in range(3):
            for j in range(3):
                if (((i + j) % 2 == 0) and not vertical) or ((i == 1 or j == 1) and vertical):
                    draw_vicsek_fractal(level - 1, x + i * size3, y + j * size3, size3, vertical=vertical, fill=fill, fill_color=fill_color, color=color)


def draw_fractal():
    dpg.delete_item("root node", children_only=True)
    draw_vicsek_fractal(
        level=dpg.get_value("levels"), 
        x=0, y=0, 
        size=600,
        vertical=dpg.get_value("orientation")=="vertical",
        fill=dpg.get_value("rect_fill"), 
        fill_color=dpg.get_value("fill color"),
        color=dpg.get_value("border color")
    )


def scale_fractal():
    s = dpg.get_value("fractal size")
    dpg.apply_transform("root node", dpg.create_scale_matrix([s]*2))
    dpg.configure_item("canvas", width=600*s, height=600*s)


with dpg.window(tag="controls", label="controls", pos=(500,700), width=400):
    dpg.add_text("Fractal settings:")
    dpg.add_slider_int(tag="levels", label="levels", default_value=3, max_value=6, callback=draw_fractal)
    dpg.add_slider_float(tag="fractal size", label="fractal size", default_value=1, max_value=4, min_value=0.1, callback=scale_fractal)
    dpg.add_checkbox(tag="rect_fill", label="fill rectangles", callback=draw_fractal)
    dpg.add_radio_button(tag="orientation", label="orientation", items=["vertical", "diagonal"], horizontal=True, default_value="vertical", callback=draw_fractal)
    dpg.add_color_edit(tag="border color", label="fractal border color", default_value=[255,255,255], callback=draw_fractal)
    dpg.add_color_edit(tag="fill color", label="fill color", default_value=[255,255,255], callback=draw_fractal)

    dpg.configure_item("controls", no_close=True)


with dpg.window(tag="main window"):
    dpg.add_text("This is Vicsek fractal")

    with dpg.drawlist(tag="canvas", width=600, height=600):
        with dpg.draw_node(tag="root node"):
            draw_fractal()


dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("main window", True)


while dpg.is_dearpygui_running():
    dpg.render_dearpygui_frame()

dpg.destroy_context()


if __name__ == "__main__":
	print("xd")
