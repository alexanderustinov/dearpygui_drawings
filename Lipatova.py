import dearpygui.dearpygui as dpg

dpg.create_context()
def draw_sierpinski(drawlist, level, x1, y1, x2, y2, x3, y3):
    if level > 0:
        mid_x1 = (x1 + x2) / 2
        mid_y1 = (y1 + y2) / 2
        mid_x2 = (x2 + x3) / 2
        mid_y2 = (y2 + y3) / 2
        mid_x3 = (x3 + x1) / 2
        mid_y3 = (y3 + y1) / 2
        dpg.draw_triangle((mid_x1, mid_y1), (mid_x2, mid_y2), (mid_x3, mid_y3), fill=(0, 0, 0))
        draw_sierpinski(drawlist, level - 1, x1, y1, mid_x1, mid_y1, mid_x3, mid_y3)
        draw_sierpinski(drawlist, level - 1, mid_x1, mid_y1, x2, y2, mid_x2, mid_y2)
        draw_sierpinski(drawlist, level - 1, mid_x3, mid_y3, mid_x2, mid_y2, x3, y3)

dpg.create_viewport(title='The Sierpinski triangle', width=1960, height=1080)

with dpg.window(tag="Primary Window"):
    with dpg.drawlist(width=1960, height=1080):
        dpg.draw_triangle((200, 50), (1000, 50), (600, 800), fill=(255, 255, 255))
        draw_sierpinski(dpg.drawlist, 6, 200, 50, 1000, 50, 600, 800) # You can change the depth here

dpg.set_primary_window("Primary Window", True)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
