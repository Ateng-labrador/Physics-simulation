# https://en.wikipedia.org/wiki/Projectile_motion
# Upgrade from ProjectileMotion
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


def parameter(v0: float = 30, theta: float = 45,
              g: float = 9.8) -> tuple:
    """
    Fungsi untuk membuat parameter
    """
    theta = np.radians(theta)
    t = np.linspace(0, 2*v0*np.sin(theta)/g, 300)
    x = v0 * np.cos(theta) * t
    y = v0 * np.sin(theta) * t - 0.5 * g * t**2
    return x, y, t


def setup_axis(axis, x, y):
    """
    Fungsi untuk membuat axis
    """
    axis.set_xlim(0, max(x)*1.1)
    axis.set_ylim(0, max(y)*1.1)
    axis.axis('off')
    axis.set_facecolor("black")
    return axis


def setup_plot(axis):
    """
    Fungsi untuk membuat plot
    """
    point, = axis.plot([], [], 'o', markersize=10, color='red')
    trail, = axis.plot([], [], '-', linewidth=2, color='blue')
    return point, trail


def update(i, point, trail, x, y):
    """
    Fungsi untuk membuat frame to frame
    """
    point.set_data([x[i]], [y[i]])
    trail.set_data(x[:i], y[:i])
    return point, trail


if __name__ == "__main__":
    fig, axis = plt.subplots(figsize=(8, 4))
    fig.patch.set_facecolor("black")
    x, y, t = parameter()
    fig.patch.set_facecolor("black")
    axis = setup_axis(axis, x, y)
    point, trail = setup_plot(axis)

    def init():
        point.set_data([], [])
        trail.set_data([], [])
        return point, trail
    
    ani = FuncAnimation(fig=fig,
                        frames=len(t),
                        func=update,
                        fargs=(point, trail, x, y),
                        init_func=init,
                        blit=True,
                        interval=20
                        )
    
    plt.show()

