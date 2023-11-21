import dearpygui.dearpygui as dpg
from vector import Vector

dpg.create_context()
dpg.create_viewport(title="Fractals", width=700, height=700)
dpg.setup_dearpygui()

def draw():
    
    with dpg.drawlist(width=500, height=500, tag=Tag[1], parent="window", show=False):
        
        def coch(n):
            if n == 0:
                dpg.draw_line(P.toTuple(), P.sum(D).toTuple(),
                            color=(dpg.get_value("R"), dpg.get_value("G"), dpg.get_value("B"), 255),
                            thickness=dpg.get_value("thickness"), parent=Tag[1])
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

with dpg.window(label="Koch's snowflake", tag="window"):
    
    dpg.add_slider_int(label="Level", min_value=0, max_value=4, default_value=3, tag="level", callback=draw)
    dpg.add_slider_int(label="Size", min_value=50, max_value=400, default_value=300, tag="size", callback=draw)
    dpg.add_slider_float(label="Thickness", min_value=1, max_value=5, default_value=1, tag="thickness", callback=draw)
    dpg.add_slider_float(label="Red", min_value=0, max_value=255, default_value=255, tag="R", callback=draw)
    dpg.add_slider_float(label="Green", min_value=0, max_value=255, default_value=0, tag="G", callback=draw)
    dpg.add_slider_float(label="Blue", min_value=0, max_value=255, default_value=0, tag="B", callback=draw)
   
    Tag = [None, "drawlist"]
    draw()

dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()