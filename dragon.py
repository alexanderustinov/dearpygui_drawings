import dearpygui.dearpygui as dpg


def dragon(x1, y1, x2, y2, depth, canvas):
    def paint(x1, y1, x2, y2, k):
        if k == 0:
            dpg.draw_line([x1, y1], [x2, y2], parent=canvas, color=[255, 255, 255])
        else:
            tx = (x1 + x2) // 2 + (y2 - y1) // 2
            ty = (y1 + y2) // 2 - (x2 - x1) // 2
            paint(x2, y2, tx, ty, k - 1)
            paint(x1, y1, tx, ty, k - 1)

    paint(x1, y1, x2, y2, depth)


dpg.create_context()
dpg.create_viewport()
dpg.setup_dearpygui()

with dpg.window(label="Dragon Curve", width=750, height=750):
    with dpg.drawlist(width=700, height=700):
        dragon(50, 350, 650, 350, 14, dpg.last_item())

dpg.show_viewport()
while dpg.is_dearpygui_running():
    dpg.render_dearpygui_frame()

dpg.destroy_context()