# code up from kinetamtic
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


def parameter(
    x0: float = 0.0, v0: float = 0.5, a: float = 1, t_end: float = 10, fps: int = 60
) -> tuple:
    dt = 1.0 / fps
    t = np.arange(0, t_end + dt, dt)
    x = x0 + v0 * t + (1 / 2) * a * t**2
    return t, x, fps


def create_plot(axis) -> tuple:
    (line_obj,) = axis[0].plot([], [], "o", markersize=10)
    (trail_line,) = axis[0].plot([], [], "-", linewidth=1.5)
    (pos_line,) = axis[1].plot([], [], "-", linewidth=1.5)
    (dot,) = axis[1].plot([], [], "ro")
    return line_obj, trail_line, pos_line, dot


def setup_plot(axis, x) -> tuple:
    axis[0].set_xlim(np.min(x) - 0.2, np.max(x) + 0.2)
    axis[0].set_ylim(-1, 1)
    axis[1].set_xlim(0, 10)
    axis[1].set_ylim(np.min(x) - 0.5, np.max(x) + 0.5)
    axis[0].grid()
    axis[1].grid()
    return axis


def update(i, fps, x, line_obj, pos_line, dot, trail_line, t):
    train_len = int((1 / 2) * fps)
    s = max(0, i - train_len)
    xi = x[i]
    trail_x = x[s : i + 1]
    trail_y = np.zeros_like(trail_x)
    line_obj.set_data([xi], [0])
    trail_line.set_data(trail_x, trail_y)
    pos_line.set_data(t[: i + 1], x[: i + 1])
    dot.set_data([t[i]], [xi])
    return line_obj, trail_line, pos_line, dot


if __name__ == "__main__":
    fig, axis = plt.subplots(1, 2)
    t, x, fps = parameter()
    axis = setup_plot(axis, t)
    line_obj, trail_line, pos_line, dot = create_plot(axis)

    def init():
        line_obj.set_data([], [])
        trail_line.set_data([], [])
        pos_line.set_data([], [])
        dot.set_data([], [])
        return line_obj, trail_line, pos_line, dot

    ani = FuncAnimation(
        fig=fig,
        frames=len(t),
        func=update,
        fargs=(fps, x, line_obj, pos_line, dot, trail_line, t),
        init_func=init,
        blit=True,
        interval=1000 * (1.0 / fps),
    )

plt.show()
