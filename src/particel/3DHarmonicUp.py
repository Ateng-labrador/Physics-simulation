import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


def parameter(A: float = 1.0, w: float = 2*np.pi,
              phi: float = 0, t_max: float = 6,
              dt: float = 0.02) -> tuple:
    """
    Fungsi untuk membuat parameter
    """
    t = np.arange(0, t_max, dt)
    x = A * np.cos(w * t + phi)
    y = 0.3 * np.sin(w * t)
    z = 0.3 * np.sin(2 * w * t)
    return x, y, z, t


def setup_axis(axis):
    """
    Fungsi untuk membuat axis
    """
    axis.set_xlim(-1.5, 1.5)
    axis.set_ylim(-0.5, 0.5)
    axis.set_zlim(-0.5, 0.5)
    axis.axis('off')
    axis.set_facecolor('black')
    axis.set_aspect('equal')
    return axis


def setup_plot(axis):
    """
    Fungsi untuk membuat plot
    """
    ball, = axis.plot([], [], [], 'o', markersize=12, color='red')
    trail, = axis.plot([], [], [], lw=1, color='blue')
    return ball, trail


def update(i, ball, trail, x, y, z):
    """
    Fungsi untuk membuat frame to frame
    """
    ball.set_data([x[i]], [y[i]])
    ball.set_3d_properties([z[i]])
    trail.set_data(x[:i], y[:i])
    trail.set_3d_properties(z[:i])
    return ball, trail


if __name__ == "__main__":
    fig = plt.figure(figsize=(8, 6))
    axis = fig.add_subplot(111, projection='3d')
    fig.patch.set_facecolor('black')
    axis = setup_axis(axis)
    x, y, z, t = parameter()
    ball, trail = setup_plot(axis)

    def init():
        # parameter init harus sama
        # dengan yang di update
        """
        Fungsi untuk membuat frame
        """
        ball.set_data([], [])
        ball.set_3d_properties([])
        trail.set_data([], [])
        trail.set_3d_properties([])
        return ball, trail

    ani = FuncAnimation(
        fig=fig,
        func=update,
        fargs=(ball, trail, x, y, z),
        init_func=init,
        frames=len(t),
        interval=20,
        blit=True
    )

    plt.show()
