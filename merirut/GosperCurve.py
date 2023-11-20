import dearpygui.dearpygui as dpg
import math


def apply_rules(ch):
    if ch == 'A':
        return 'A-B--B+A++AA+B-'
    elif ch == 'B':
        return '+A-BB--B-A++A+B'
    else:
        return ch


def generate_gosper(axiom, iterations):
    result = axiom
    for _ in range(iterations):
        result = ''.join(apply_rules(c) for c in result)
    return result


def draw_gosper(drawlist, instructions, length, angle, start_x, start_y):
    x, y = start_x, start_y
    direction = 90
    stack = []

    for command in instructions:
        if command == 'A' or command == 'B':
            new_x = x + length * math.cos(math.radians(direction))
            new_y = y + length * math.sin(math.radians(direction))
            dpg.draw_line([x, y], [new_x, new_y], parent=drawlist, 
color=[255, 255, 255])
            x, y = new_x, new_y
        elif command == '+':
            direction -= angle
        elif command == '-':
            direction += angle
        elif command == '[':
            stack.append((x, y, direction))
        elif command == ']':
            x, y, direction = stack.pop()


def main():
    axiom = 'A'
    iterations = 4
    length = 10
    angle = 60
    start_x = 650
    start_y = 450

    instructions = generate_gosper(axiom, iterations)

    dpg.create_context()
    dpg.create_viewport()

    with dpg.window(label="Gosper Curve", width=800, height=800):
        with dpg.drawlist(width=700, height=700):
            draw_gosper(dpg.last_item(), instructions, length, angle, 
start_x, start_y)

    dpg.show_viewport()
    dpg.setup_dearpygui()
    while dpg.is_dearpygui_running():
        dpg.render_dearpygui_frame()

    dpg.destroy_context()


if __name__ == "__main__":
    main()

