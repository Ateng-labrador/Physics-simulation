# https://en.wikipedia.org/wiki/Lissajous_curve
# Upgrade from Lisajouss
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


def parameter(A: float = 1.5, B: float = 1.0,
              wx: float = 3, wy: float = 2) -> tuple:
    """
    Fungsi untuk membuat parameter
    """
    delta = np.pi/3
    t = np.linspace(0, 10, 1000)
    x = A * np.sin(wx * t + delta)
    y = B * np.sin(wy * t)
    return x, y, t


def setup_plot(axis):
    """
    Fungsi untuk membuat plot
    """
    point, = axis.plot([], [], 'ro', ms=8)
    trail, = axis.plot([], [], '-', lw=1)
    return point, trail


def setup_axis(axis):
    """
    Fungsi untuk membuat axis
    """
    axis.set_xlim(-2, 2)
    axis.set_ylim(-2, 2)
    axis.axis('off')
    axis.set_facecolor("black")
    axis.set_aspect("equal")
    return axis


def update(i, point, trail, x, y):
    """
    Fungsi untuk membuat frame to
    frame
    """
    point.set_data([x[i]], [y[i]])
    trail.set_data(x[:i], y[:i])
    return point, trail


if __name__ == "__main__":
    fig, axis = plt.subplots(figsize=(6, 6))
    fig.patch.set_facecolor("black")
    x, y, t = parameter()
    point, trail = setup_plot(axis)
    axis = setup_axis(axis)

    def init():
        point.set_data([], [])
        trail.set_data([], [])
        return point, trail

    ani = FuncAnimation(fig=fig,
                        func=update,
                        fargs=(point, trail, x, y),
                        frames=len(t),
                        init_func=init,
                        blit=True,
                        interval=20
                        )

    plt.show()
