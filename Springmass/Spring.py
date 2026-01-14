# Spring and graph
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


def parameter(m: float = 1, k: float = 1, d: float = 0.2):
    """
    Function for make the parameter
    :param m: massa
    :type m: float
    :param k: constant
    :type k: float
    :param d: Damping
    :type d: float
    """
    t = np.linspace(0, 20, 501)
    w_d = np.sqrt((4 * m * k - d**2) / (4 * m**2))
    x = np.exp(-d / (2 * m) * t) * np.cos(w_d * t)
    return t, w_d, x


def setup_axis(axis, t):
    """
    Setup for axis
    """
    axis[0].set_xlim([-2, 2])
    axis[0].set_ylim([-2, 2])
    axis[1].set_xlim([min(t), max(t)])
    axis[1].set_ylim([-2, 2])
    axis[0].grid()
    axis[1].grid()
    return axis


def create_plot(axis):
    """
    Fuction for make the plot
    """
    (animated_mass,) = axis[0].plot([], [], "-o", markersize=20, color="red")
    (animated_spring,) = axis[0].plot([], [], color="blue")
    (animated_func,) = axis[1].plot([], [], color="blue")
    return animated_mass, animated_spring, animated_func


def update(frame, t, x, animated_mass, animated_spring, animated_func):
    """
    Fuction for make frame to frame

    :param frame
    :param t: time
    :param x: moving of pendulum
    :param animated_mass: Mass
    :param animated_spring: Spring
    :param animated_func: Graph
    """
    animated_spring.set_data([0, 0], [2, x[frame]])
    animated_mass.set_data([0], [x[frame]])
    animated_spring.set_linewidth(int(abs(x[frame] - 2) * 2))
    animated_func.set_data(t[:frame], x[:frame])
    return animated_mass, animated_spring, animated_func


if __name__ == "__main__":
    fig, axis = plt.subplots(1, 2)
    t, w_d, x = parameter()
    axis = setup_axis(axis, t)
    animated_mass, animated_spring, animated_func = create_plot(axis)

    def init():
        """Initial parameter"""
        animated_mass.set_data([], [])
        animated_spring.set_data([], [])
        animated_func.set_data([], [])
        return animated_mass, animated_spring, animated_func

    ani = FuncAnimation(
        fig=fig,
        func=update,
        fargs=(t, x, animated_mass, animated_spring, animated_func),
        init_func=init,
        frames=len(t),
        interval=25,
        blit=False,
    )

    plt.show()
