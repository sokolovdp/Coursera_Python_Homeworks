import sys


def draw_ladder(total_steps: "int", current_steps: "int"):
    out_line = " " * (total_steps - current_steps) + "#" * current_steps
    print(out_line)
    if current_steps < total_steps:
        draw_ladder(total_steps, current_steps + 1)


if __name__ == '__main__':
    steps_number = int(sys.argv[1])
    draw_ladder(steps_number, 1)
