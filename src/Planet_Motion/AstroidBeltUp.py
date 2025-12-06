# # https://en.wikipedia.org/wiki/Asteroid
# upgrde code 
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# jalur planet
a_jupiter = 8.0
a_mars = 3.0


def parameter(N: float = 450):
    """
    Fungsi untuk membuat parameter
    """
    a = np.random.uniform(4.5, 7.5, N)
    e = np.random.uniform(0.0, 0.35, N)
    colors = np.random.choice(['white', 'silver', 'gray'], N)
    b = a * np.sqrt(1 - e**2)
    theta0 = np.random.uniform(0, 2*np.pi, N)
    kepler_speed = 1 / a**3/2
    x = a * np.cos(theta0)
    y = b * np.sin(theta0)
    return a, b, x, y, theta0, kepler_speed, colors


def setup_asteroids(axis, colors, x, y):
    """
    Fungsi untuk membuat asteroids
    """
    asteroids = axis.scatter(x, y, s=4, c=colors, label="Asteroid")
    return asteroids


def setup_mars(axis):
    """
    Fungsi untuk membuat mars
    """
    theta_mars_0 = np.random.uniform(0, 2*np.pi)
    mars_dot = axis.scatter(a_mars*np.cos(theta_mars_0),
                            a_mars*np.sin(theta_mars_0),
                            s=80, c='red', label="Mars")
    return mars_dot, theta_mars_0


def setup_jupiter(axis):
    """
    Fungsi untuk membuata jupiter
    """
    theta_jupiter_0 = np.random.uniform(0, 2*np.pi)
    jupiter_dot = axis.scatter(a_jupiter*np.cos(theta_jupiter_0),
                               a_jupiter*np.sin(theta_jupiter_0),
                               s=150, c='orange', label="Jupiter")
    return jupiter_dot, theta_jupiter_0


def setup_sun(axis):
    """
    Fungsi untuk membuat matahari
    """
    sun = axis.scatter(0, 0, s=300, c='yellow', label="Matahari")
    return sun


def setup_axis(axis):
    """
    Fungsi untuk setup axis
    """
    axis.set_xlim(-10, 10)
    axis.set_ylim(-10, 10)
    axis.axis('off')
    axis.set_aspect("equal")
    return axis


def update(i, a, b, theta0, asteroids,
           mars_dot, jupiter_dot, kepler_speed,
           theta_mars_0, theta_jupiter_0):
    """
    Fungsi untuk membuat frame to frame
    """
    speed_jupiter = 0.005
    speed_mars = 0.02

    theta = theta0 + kepler_speed * i
    x = a * np.cos(theta)
    y = b * np.sin(theta)
    asteroids.set_offsets(np.c_[x, y])

    # mars
    theta_m = theta_mars_0 + speed_mars * i
    mars_dot.set_offsets([a_mars * np.cos(theta_m),
                          a_mars * np.sin(theta_m)])

    # jupiter
    theta_j = theta_jupiter_0 + speed_jupiter * i
    jupiter_dot.set_offsets([a_jupiter * np.cos(theta_j),
                             a_jupiter * np.sin(theta_j)])

    return asteroids, mars_dot, jupiter_dot


if __name__ == "__main__":
    fig, axis = plt.subplots(figsize=(6, 6))
    fig.patch.set_facecolor('black')
    axis = setup_axis(axis)
    a, b, x, y, theta0, kepler_speed, colors = parameter()
    asteroids = setup_asteroids(axis, colors, x, y)
    sun = setup_sun(axis)
    mars_dot, theta_mars_0 = setup_mars(axis)
    jupiter_dot, theta_jupiter_0 = setup_jupiter(axis)

    def init():
        """
        Fungsi parameter awal
        """
        asteroids.set_offsets(np.empty((0, 2)))
        mars_dot.set_offsets(np.empty((0, 2)))
        jupiter_dot.set_offsets(np.empty((0, 2)))
        return asteroids, mars_dot, jupiter_dot

    ani = FuncAnimation(
          fig=fig,
          func=update,
          fargs=(
                 a, b,
                 theta0, asteroids,
                 mars_dot, jupiter_dot,
                 kepler_speed, theta_mars_0,
                 theta_jupiter_0),
          init_func=init,
          frames=1000,
          interval=20
    )

    plt.show()
