import dearpygui.dearpygui as dpg
import math

dpg.create_context()

golden_ratio = (1 + 5**0.5) / 2
r1 = r = (1 / golden_ratio)**(1 / golden_ratio)
r2 = r1**2
angle1 = math.acos((1 + r**2 - r**4) / (2 * r))
angle2 = math.acos((1 + r**4 - r**2) / (2 * r**2))

def golden_dragon(drawlist, x1, y1, x2, y2, turn, n):
    if n == 1:
        dpg.draw_line((x1, y1), (x2, y2), color=(255, 255, 255, 255), thickness=1)
    else:
        dist = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
        
        if dist < 1:
            dpg.draw_line((x1, y1), (x2, y2), color=(255, 255, 255, 255), thickness=1)
        else:
            angle = math.atan2(y2 - y1, x2 - x1)
            
            if turn:
                px = x1 + dist * r1 * math.cos(angle + angle1)
                py = y1 + dist * r1 * math.sin(angle + angle1)
            else:
                px = x1 + dist * r2 * math.cos(angle - angle2)
                py = y1 + dist * r2 * math.sin(angle - angle2)
                
            golden_dragon(drawlist, x1, y1, px, py, True, n - 1)
            golden_dragon(drawlist, px, py, x2, y2, False, n - 1)

dpg.create_viewport(title='The Golden Dragon', width=1280, height=720)

with dpg.window(tag="Window"):
    with dpg.drawlist(width=1280, height=720):
        golden_dragon(dpg.drawlist, 300, 300, 700, 200, True, 100)

dpg.set_primary_window("Window", True)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()