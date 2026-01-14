# https://en.wikipedia.org/wiki/Spirograph
# Upgrade code from Spirograph
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


def calculation_math(r1: float, r2: float, r3: float, w1: float, w2: float, w3: float):
    """
    function Calculation math equation

    return :

    x(real)
    y(imag)
    """
    theta = np.linspace(0, 2 * np.pi, 1000)
    z = (
        r1 * np.exp(1j * w1 * theta)
        + r2 * np.exp(1j * w2 * theta)
        + r3 * np.exp(1j * w3 * theta)
    )
    x = np.real(z)
    y = np.imag(z)
    return x, y


def setup_axis(axis) -> tuple:
    """
    function for setup_axis
    """
    axis.set_xlim(-10, 10)
    axis.set_ylim(-10, 10)
    axis.axis("off")
    axis.set_aspect("equal")
    return axis


def create_plot(axis) -> tuple:
    """
    Function for make the figure line
    """
    (line,) = axis.plot([], [], lw=1.5, color="white")
    return line


def update(frame, x, y, line) -> tuple:
    """
    function for make frame to frame
    """
    line.set_data(x[:frame], y[:frame])
    return line


if __name__ == "__main__":
    fig, axis = plt.subplots()
    x, y = calculation_math(4, 4, 1.3, 44, -17, -54)
    fig.patch.set_facecolor("pink")
    axis = setup_axis(axis)
    plt.axis("off")
    line = create_plot(axis)

    def init() -> tuple:
        """
        Intial contional
        """
        line.set_data([], [])
        return line

    ani = FuncAnimation(
        fig=fig,
        func=update,
        fargs=(x, y, line),
        init_func=init,
        frames=len(x),
        interval=5,
    )

    plt.show()
