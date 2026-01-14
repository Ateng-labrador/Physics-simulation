# Up version from damped_oscillations
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


def parameter(A: float = 1, w: float = 6,
              b1: float = 0.15, b2: float = 0.40) -> float:
    """
    Fuction fot make parameter
    """
    t = np.linspace(0, 10, 400)
    x1 = A * np.exp(-b1 * t) * np.cos(w * t)
    x2 = A * np.exp(-b2 * t) * np.cos(w * t)
    return x1, x2, t, b1, b2


def setup_axis(axis):
    """
    Fuction for make setup axis
    """
    axis.set_xlim([0, 10])
    axis.set_ylim([-1.2, 1.2])
    axis.set_xlabel("t (s)")
    axis.set_ylabel("x(t)")
    axis.set_title("Perbandingan Osilasi Teredam")
    return axis


def setup_plot(axis, b1, b2):
    """
    fuction for setup plot
    """
    scat1 = axis.scatter([], [], s=15, label=f"b={b1}")
    line2, = axis.plot([], [], c="r", label=f"b={b2}")
    return scat1, line2


def update(frame, t, x1, x2, scat1, line2):
    """ Fuction make frame to frame """
    data1 = np.column_stack((t[:frame], x1[:frame]))
    scat1.set_offsets(data1)
    line2.set_xdata(t[:frame])
    line2.set_ydata(x2[:frame])
    return scat1, line2


if __name__ == "__main__":
    fig, axis = plt.subplots()
    axis = setup_axis(axis)
    x1, x2, t, b1, b2 = parameter()
    scat1, line2 = setup_plot(axis, b1, b2)
    axis.legend()

    def init():
        """ initial parameter """
        scat1.set_offsets(np.empty((0, 2)))
        line2.set_xdata([])
        line2.set_ydata([])
        return scat1, line2

    ani = FuncAnimation(
        fig=fig,
        func=update,
        fargs=(t, x1, x2, scat1, line2),
        init_func=init,
        frames=len(t),
        interval=30,
        blit=True
    )

    plt.show()
