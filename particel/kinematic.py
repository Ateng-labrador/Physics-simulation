# Akbar Huda Febriyanto Physics uny 24
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


# Parameter
x_0 = 0.0
fps = 60
dt = 1.0 / fps
t = np.arange(0, 10 + dt, dt)

# GLBB equation
v0 = 0.5
a = 0.8
x = x_0 + v0 * t + (1 / 2) * a * t**2

fig, (axis_1, axis_2) = plt.subplots(1, 2)
(line_obj,) = axis_1.plot([], [], "o", markersize=10)
(trail_line,) = axis_1.plot([], [], "-", linewidth=1.5)
axis_1.set_ylim(-1, 1)
axis_1.set_yticks([])
axis_1.grid(True)
(pos_line,) = axis_2.plot([], [], "-", linewidth=1.5)
(dot,) = axis_2.plot([], [], "ro")
axis_2.set_xlim(0, 10)
axis_2.set_ylim(np.min(x) - 0.5, np.max(x) + 0.5)
axis_2.grid(True)

axis_1.set_xlim(np.min(x) - 0.2, np.max(x) + 0.2)
trail_len = int(0.5 * fps)


def init():
    line_obj.set_data([], [])
    trail_line.set_data([], [])
    pos_line.set_data([], [])
    dot.set_data([], [])
    return line_obj, trail_line, pos_line, dot


def update(i):
    xi = x[i]
    s = max(0, i - trail_len)
    trail_x = x[s : i + 1]
    trail_y = np.zeros_like(trail_x)
    line_obj.set_data([xi], [0])
    trail_line.set_data(trail_x, trail_y)

    pos_line.set_data(t[: i + 1], x[: i + 1])
    dot.set_data([t[i]], [xi])

    return line_obj, trail_line, pos_line, dot


ani = FuncAnimation(
    fig, update, frames=len(t), init_func=init, blit=True, interval=1000 * dt
)

plt.show()
