# upgrade code
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


def parameter(
    m1: float = 2.0,
    m2: float = 1.0,
    v1: float = 1.4,
    v2: float = -1.2,
    x1: float = -4.0,
    x2: float = 4.0,
    dt: float = 0.02,
    t_max: float = 10,
):
    """
    Fungsi untuk membuat parameter
    """
    times = np.arange(0, t_max, dt)
    x1_list = []
    x2_list = []
    collided = False
    for t in times:
        x1 += v1 * dt
        x2 += v2 * dt

        if not collided and abs(x1 - x2) <= 0.5:
            # persamaan tumbukan elastis
            v1_new = ((m1 - m2) / (m1 + m2)) * v1 + ((2 * m2) / (m1 + m2)) * v2
            v2_new = ((2 * m1) / (m1 + m2)) * v1 + ((m2 - m1) / (m1 + m2)) * v2
            v1, v2 = v1_new, v2_new
            collided = True

        x1_list.append(x1)
        x2_list.append(x2)
    return x1_list, x2_list, times


def setup_axis(axis):
    """
    Fungsi untuk membuat axis
    """
    axis.set_xlim(-8, 8)
    axis.set_ylim(-1, 1)
    axis.set_aspect("equal")
    axis.axis("off")
    axis.set_facecolor("black")
    return axis


def setup_plot(axis):
    """
    Fungsi untuk membuat axis
    """
    (obj1,) = axis.plot([], [], "bo", markersize=22)
    (obj2,) = axis.plot([], [], "ro", markersize=22)
    return obj1, obj2


def update(i, obj1, obj2, x1_list, x2_list):
    """
    Fungsi untuk membuat frame to frame
    """
    obj1.set_data([x1_list[i]], [0])
    obj2.set_data([x2_list[i]], [0])
    return obj1, obj2


if __name__ == "__main__":
    fig, axis = plt.subplots(figsize=(8, 3))
    fig.patch.set_facecolor("black")
    axis = setup_axis(axis)
    obj1, obj2 = setup_plot(axis)
    x1_list, x2_list, times = parameter()

    def init():
        obj1.set_data([], [])
        obj2.set_data([], [])
        return obj1, obj2

    ani = FuncAnimation(
        fig=fig,
        func=update,
        fargs=(obj1, obj2, x1_list, x2_list),
        init_func=init,
        frames=len(times),
        interval=20,
    )

    plt.show()
