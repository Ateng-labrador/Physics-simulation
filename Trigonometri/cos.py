import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


def parameter(t=np.linspace(0, 10, 100)):
    """Fungsi untuk Parameter"""
    y = np.cos(t)
    return y, t


def setup_axis(t, axis):
    """Fungsi untuk setup axis"""
    axis.set_xlim([min(t), max(t)])
    axis.set_ylim([-2, 2])
    return axis


def setup_plot(axis):
    """Fungsi untuk setup plot"""
    (animation_plot,) = axis.plot([], [])
    return animation_plot


def animation(i, t, y, animation_plot):
    """Fungsi untuk membuat frame to frame"""
    animation_plot.set_data(t[:i], y[:i])
    return animation_plot


if __name__ == "__main__":
    fig, axis = plt.subplots()
    y, t = parameter()
    axis = setup_axis(t, axis)
    animation_plot = setup_plot(axis)

    def init():
        """Animasi awal"""
        animation_plot.set_data([], [])
        return (animation_plot,)

    _ani = FuncAnimation(
        fig=fig,
        func=animation,
        fargs=(t, y, animation_plot),
        init_func=init,
        frames=len(t),
        interval=30,
        blit=False,
    )
    plt.show()
