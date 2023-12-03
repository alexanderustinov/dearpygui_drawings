import dearpygui.dearpygui as dpg
from vector import Vector
from timeit import default_timer as timer
from time import sleep

dpg.create_context()
dpg.create_viewport(title="Fractals", width=700, height=700, vsync=False)
dpg.setup_dearpygui()

def draw():

    with dpg.drawlist(width=500, height=500, tag=Tag[1], parent="window", show=False):

        def coch(n):
            if n == 0:
                dpg.draw_line(P.toTuple(), P.sum(D).toTuple(),
                            color=(255, 0, 0, 255),
                            thickness=1)
            else:
                for angle in [0, 60, -120, 60]:
                    D.turn(angle)
                    coch(n - 1)

        level = dpg.get_value("level")
        size = dpg.get_value("size")
        P = Vector((500 - size) / 2, 250 + size * (3) ** (1/2) / 6)
        D = Vector(size / (3 ** level), 0)

        for i in range(3):
            coch(level)
            D.turn(-120)

    if Tag[0] is not None:
        dpg.delete_item(Tag[0])

    dpg.show_item(Tag[1])
    Tag[0] = Tag[1]
    Tag[1] = dpg.generate_uuid()

def on_render():
    if dpg.does_item_exist("time_report"):
        dpg.delete_item("time_report")
    delta_time = dpg.get_delta_time()
    
    if delta_time == 0:
        delta_time = 0.001
    dpg.add_text(f"FPS: {1 / delta_time:.2f}", tag="time_report", parent="window")

with dpg.window(label="Koch's snowflake", tag="window"):

    on_render()
    dpg.add_slider_int(label="Level", min_value=0, max_value=5, default_value=3, tag="level")
    dpg.add_slider_int(label="Size", min_value=50, max_value=400, default_value=300, tag="size")

    Tag = [None, "drawlist"]
    draw()

dpg.show_viewport()

while dpg.is_dearpygui_running():
    on_render()
    draw()
    dpg.render_dearpygui_frame()

dpg.start_dearpygui()
dpg.destroy_context()