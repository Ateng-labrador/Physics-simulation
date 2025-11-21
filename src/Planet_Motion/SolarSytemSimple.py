# https://en.wikipedia.org/wiki/Solar_System
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Muh Razan Physics UNY 24

fig, ax = plt.subplots(figsize=(6, 6))
fig.patch.set_facecolor('black')
ax.axis('off')
ax.set_facecolor("black")
ax.set_xlim(-12, 12)
ax.set_ylim(-12, 12)

# make the sun
sun = plt.Circle((0, 0), 0.8, color='yellow')
ax.add_patch(sun)

# planet data
planets = [
    {"color": "cyan",   "a": 3,  "b": 1, "speed": 0.005},
    {"color": "blue",   "a": 6,  "b": 2, "speed": 0.004},
    {"color": "lime",   "a": 9,  "b": 3, "speed": 0.003},
    {"color": "violet", "a": 12, "b": 4, "speed": 0.002},
]


# random position for planet
for p in planets:
    p["start"] = np.random.uniform(0, 2*np.pi)

# make the elips orbit
t = np.linspace(0, 2*np.pi, 500)
for p in planets:
    ax.plot(p["a"] * np.cos(t), p["b"] * np.sin(t),
            linestyle="--", linewidth=1, color=p["color"], alpha=0.5)

# make the planet
dots = []
for p in planets:
    dot, = ax.plot([], [], 'o', color=p["color"], markersize=8)
    dots.append(dot)


# animasi
def update(frame):
    for i, p in enumerate(planets):
        angle = p["start"] + frame * p["speed"]
        x = p["a"] * np.cos(angle)
        y = p["b"] * np.sin(angle)
        dots[i].set_data([x], [y])
    return dots


ani = animation.FuncAnimation(fig,
                              update,
                              frames=1000,
                              interval=16)
plt.show()
