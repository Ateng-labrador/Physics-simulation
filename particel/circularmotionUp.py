import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

R = 5
theta0 = np.array([0, np.pi / 2, np.pi, 3 * np.pi / 2])


def setup_plot(axis):
    (points,) = axis.plot([], [], "ro", markersize=20)
    arrows = []
    for _ in range(4):
        arrow = axis.arrow(0, 0, 0, 0, color="red", head_width=0.25, head_length=0.4)
        arrows.append(arrow)
    return points, arrows


def setup_axis(axis):
    axis.set_xlim(-6, 6)
    axis.set_ylim(-6, 6)
    axis.axis("off")
    axis.set_aspect("equal")
    return axis


def update(frame, points, arrows, axis):
    angle = frame * 0.05
    x = R * np.cos(theta0 + angle)
    y = R * np.sin(theta0 + angle)
    points.set_data(x, y)

    for arrow in arrows:
        arrow.remove()
    arrows.clear()

    for i in range(4):
        vx = -np.sin(theta0[i] + angle) * 2
        vy = np.cos(theta0[i] + angle) * 2
        new_arrow = axis.arrow(
            x[i], y[i], vx, vy, color="red", head_width=0.25, head_length=0.4
        )
        arrow.append(new_arrow)
    return (points,) + tuple(arrow)


if __name__ == "__main__":
    fig, axis = plt.subplots()
    axis = setup_axis(axis)
    theta = np.linspace(0, 2 * np.pi, 500)
    axis.plot(R * np.cos(theta), R * np.sin(theta), "k", linewidth=2)
    points, arrows = setup_plot(axis)

    def init():
        points.set_data([], [])
        for arrow in arrows:
            arrow.remove()
        arrows.clear()
        return (points,)

    ani = FuncAnimation(
        fig=fig,
        func=update,
        fargs=(points, arrows, axis),
        init_func=init,
        frames=1000,
        interval=30,
        blit=False,
    )

    plt.show()
