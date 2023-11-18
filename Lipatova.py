import dearpygui.dearpygui as dpg

dpg.create_context()
def draw_sierpinski(drawlist, level, x1, y1, x2, y2, x3, y3):
    if level == 0:
        dpg.draw_triangle((x1, y1), (x2, y2), (x3, y3),  fill=(255, 255, 255))
    else:
        mid_x1 = (x1 + x2) / 2
        mid_y1 = (y1 + y2) / 2
        mid_x2 = (x2 + x3) / 2
        mid_y2 = (y2 + y3) / 2
        mid_x3 = (x3 + x1) / 2
        mid_y3 = (y3 + y1) / 2

        draw_sierpinski(drawlist, level - 1, x1, y1, mid_x1, mid_y1, mid_x3, mid_y3)
        draw_sierpinski(drawlist, level - 1, mid_x1, mid_y1, x2, y2, mid_x2, mid_y2)
        draw_sierpinski(drawlist, level - 1, mid_x3, mid_y3, mid_x2, mid_y2, x3, y3)

dpg.create_viewport(title='The Sierpinski triangle', width=600, height=750)

with dpg.window(tag="Primary Window"):
    with dpg.drawlist(width=600, height=730):
        draw_sierpinski(dpg.drawlist, 3, 100, 200, 500, 200, 300, 550) # You can change the depth here

dpg.set_primary_window("Primary Window", True)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()