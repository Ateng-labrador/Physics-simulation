# Mifta Nur'aini physics UNY 24
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

planets = {
    "Merkurius": {"r": 0.4, "w": 0.04, "color": "orange"},
    "Venus":     {"r": 0.7, "w": 0.03, "color": "gold"},
    "Bumi":      {"r": 1.0, "w": 0.02, "color": "cyan"},
    "Mars":      {"r": 1.5, "w": 0.015, "color": "red"},
}

fig, ax = plt.subplots(figsize=(6, 6))
ax.set_facecolor("black")
fig.patch.set_facecolor("black")
ax.set_aspect("equal")
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_xticks([])
ax.set_yticks([])

sun = ax.plot(0, 0, "o", color="yellow", markersize=14)[0]

planet_dots = {}
orbit_lines = {}

theta = np.linspace(0, 2*np.pi, 300)

for name, p in planets.items():
    r = p["r"]
    color = p["color"]

    orbit_lines[name] = ax.plot(r*np.cos(theta), r*np.sin(theta),
                                linestyle="--", color=color, alpha=0.3)[0]

    planet_dots[name] = ax.plot([], [], "o", color=color, markersize=7)[0]


def update(frame):
    for name, p in planets.items():
        r = p["r"]
        w = p["w"]

        x = r * np.cos(w * frame)
        y = r * np.sin(w * frame)

        planet_dots[name].set_data([x], [y])

    return list(planet_dots.values())


ani = FuncAnimation(fig, update, frames=1000, interval=20, blit=True)
plt.show()
