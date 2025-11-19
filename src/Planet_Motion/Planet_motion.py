# https://en.wikipedia.org/wiki/Orbital_mechanics
# Upgrade Version from code Planet_1
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

# intial parameter
t = np.linspace(0, 2*np.pi, 200)
r = 3
x = r * np.cos(t)
y = r * np.sin(t)


def create_plot(axis) -> tuple:
    """
    Make Figure to plot
    """
    sun = axis.scatter(0, 0, c="yellow", s=200, label="sun")
    planet = axis.scatter(x[0], y[0], c="blue", s=40, label="Planet")
    orbit = axis.plot(x[0], y[0], '--', color="white", linewidth=1)[0]
    return sun, planet, orbit


def setup_axis(axis) -> tuple:
    """
    Setup for axis figure
    """
    axis.set_xlim(-7, 7)
    axis.set_ylim(-7, 7)
    axis.set_aspect("equal")
    return axis


def animation(frame, x, y, planet, orbit) -> tuple:
    """
    Make frame to frame
    """
    planet.set_offsets([[x[frame], y[frame]]])
    orbit.set_xdata(x[:frame])
    orbit.set_ydata(y[:frame])
    return planet, orbit


if __name__ == "__main__":
    fig, axis = plt.subplots()
    fig.patch.set_facecolor('black')
    axis = setup_axis(axis)
    plt.axis('off')
    sun, planet, orbit = create_plot(axis)

    # for the label
    leg = axis.legend()
    leg.get_frame().set_facecolor('white')
    leg.get_frame().set_edgecolor('white')
    for txt in leg.get_texts():
        txt.set_color('black')

    def init() -> tuple:
        """
        Make initial condition
        """
        planet.set_offsets(np.empty((0, 2)))
        orbit.set_xdata([])
        orbit.set_ydata([])
        return planet, orbit

    anim = FuncAnimation(
        fig=fig,
        func=animation,
        fargs=(x, y, planet, orbit),
        init_func=init,
        frames=len(t),
        interval=25,
        blit=True
    )

    plt.show()
