# up version Oscillations
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


x_wave = []
y_wave = []
anchor_x = 0
anchor_y = 1


def y(
    t, y0: float = -0.5, w: float = 2.5, gamma: float = 0.10, A: float = 1.0
) -> tuple:
    return y0 + A * np.exp(-gamma * t) * np.cos(w * t)


def setup_plot(axis):
    (ball,) = axis.plot([], [], "o", color="red", markersize=25)
    (spring,) = axis.plot([], [], color="black")
    (wave_line,) = axis.plot([], [], color="blue", linewidth=2)
    return ball, spring, wave_line


def setup_axis(axis):
    axis.set_ylim(-2, 1)
    axis.axis("off")
    axis.plot(anchor_x, anchor_y, "ks", markersize=10)
    axis.set_aspect("equal")
    return axis


def update(i, ball, spring, wave_line, axis):
    dt = 20 / 1000
    scroll_speed = 0.05
    center_x = 0
    ypos = y(i * dt)
    ball.set_data([0], [ypos])
    spring_y = np.linspace(anchor_y, ypos, 60)
    spring_x = 0.15 * np.sin(12 * np.linspace(0, np.pi * 4, 60))
    spring.set_data(spring_x, spring_y)

    x_wave.append(center_x)
    y_wave.append(ypos)

    x_wave[:] = [x - scroll_speed for x in x_wave]

    if len(x_wave) > 0:
        left_bound = x_wave[0] - 1
        right_bound = x_wave[-1] + 1
        axis.set_xlim(left_bound, right_bound)
    wave_line.set_data(x_wave, y_wave)
    return ball, spring, wave_line


if __name__ == "__main__":
    t_vals = np.linspace(0, 20, 1000)
    fig, axis = plt.subplots(figsize=(6, 7))
    axis = setup_axis(axis)
    ball, spring, wave_line = setup_plot(axis)

    def init():
        spring.set_data([], [])
        wave_line.set_data([], [])
        ball.set_data([], [])
        return ball, spring, wave_line

    ani = FuncAnimation(
        fig=fig,
        func=update,
        fargs=(ball, spring, wave_line, axis),
        init_func=init,
        frames=len(t_vals),
        interval=30,
    )
    plt.show()
