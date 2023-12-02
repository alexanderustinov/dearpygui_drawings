import dearpygui.dearpygui as dpg
import math
from timeit import default_timer as timer


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


def draw_gosper(drawlist, instructions, length, angle, start_x, start_y, text_container, frame_count):
    x, y = start_x, start_y
    direction = 90
    stack = []

    for command in instructions:
        if command == 'A' or command == 'B':
            new_x = x + length * math.cos(math.radians(direction))
            new_y = y + length * math.sin(math.radians(direction))

            dpg.draw_line([x, y], [new_x, new_y], parent=drawlist, color=[255, 255, 255])

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
    dpg.set_viewport_vsync(False)
    dpg.show_viewport()
    dpg.setup_dearpygui()

    frame_count = 0
    start_time = timer()

    with dpg.window(label="Gosper Curve", width=800, height=800):
        text_container = dpg.add_text("FPS: ")

        with dpg.drawlist(width=700, height=700):
            draw_gosper(dpg.last_item(), instructions, length, angle, start_x, start_y, text_container, frame_count)

    while dpg.is_dearpygui_running():
        dpg.render_dearpygui_frame()
        frame_count += 1
        elapsed_time = timer() - start_time
        if elapsed_time > 1.0:
            fps = frame_count / elapsed_time
            dpg.set_value(text_container, f"FPS: {fps:.2f}")
            start_time = timer()
            frame_count = 0

    dpg.destroy_context()


if __name__ == "__main__":
    main()
