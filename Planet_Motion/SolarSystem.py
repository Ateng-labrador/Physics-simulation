# https://en.wikipedia.org/wiki/Solar_System
# Upgrade version from SolarSytemSimple
import numpy as np
import string
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


def random_hex() -> str:
    """
    Fuction for make random color
    """
    hex_value = "".join(
        np.random.choice(
            list(string.hexdigits),
            6
        )
    )
    return f"#{hex_value}"


# data planet
planets = [
    {"color": random_hex(), "a": 3, "b": 1, "speed": 0.005},
    {"color": random_hex(), "a": 6, "b": 2, "speed": 0.004},
    {"color": random_hex(), "a": 9, "b": 3, "speed": 0.003},
    {"color": random_hex(), "a": 12, "b": 4, "speed": 0.002},
]


def create_plot(axis, planets=planets) -> tuple:
    """
    Make plot sun, planet, orbit
    """
    t = np.linspace(0, 2*np.pi, 500)
    planet_dots = []
    orbit_paths = []
    sun = axis.scatter(0, 0, c="yellow", s=200, label="sun")
    for p in planets:
        # equation of elips here a*cos b*sin
        orbit, = axis.plot(
                        p["a"] * np.cos(t), p["b"] * np.sin(t),
                        linestyle="--", linewidth=1,
                        color=p["color"], alpha=0.5)
        dot = axis.scatter([], [], marker='o', s=36, color=p["color"])
        orbit_paths.append(orbit)
        planet_dots.append(dot)
    return sun, planet_dots, orbit_paths


def create_axis(axis) -> None:
    """
    Make the axis
    """
    axis.set_xlim(-13, 13)
    axis.set_ylim(-13, 13)
    axis.set_facecolor("black")
    axis.set_aspect("equal")
    axis.axis('off')
    return axis


def random_motion() -> float:
    """
    Make random position for planet
    """
    postion = np.random.uniform(0, 2 * np.pi)
    return postion


def update(frame, planets, planet_dots) -> tuple:
    """
    make frame to frame
    """
    artis = []
    for i, p in enumerate(planets):
        phase = p.get("phase", 0.0)
        angle = phase + frame * p["speed"]
        x = p["a"] * np.cos(angle)
        y = p["b"] * np.sin(angle)
        planet_dots[i].set_offsets([[x, y]])
        artis.append(planet_dots[i])
    return tuple(artis)


if __name__ == "__main__":
    fig, axis = plt.subplots()
    fig.patch.set_facecolor('black')
    axis = create_axis(axis)

    for p in planets:
        p["phase"] = random_motion()

    sun, planet_dots, orbit_paths = create_plot(axis, planets)

    def init() -> tuple:
        for dot in planet_dots:
            dot.set_offsets(np.empty((0, 2)))
        return tuple(planet_dots)

    ani = FuncAnimation(
        fig=fig,
        func=update,
        fargs=(planets, planet_dots),
        init_func=init,
        frames=1000,
        interval=16,
        blit=True
    )

    plt.show()
