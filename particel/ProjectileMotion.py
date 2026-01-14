# https://en.wikipedia.org/wiki/Projectile_motion
# Zahwa Ayudia Physics UNY 24
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


v0 = 30
theta = 45
g = 9.8


theta = np.radians(theta)
t = np.linspace(0, 2 * v0 * np.sin(theta) / g, 300)

# persamaan lintasan
x = v0 * np.cos(theta) * t
y = v0 * np.sin(theta) * t - 0.5 * g * t**2


fig, ax = plt.subplots(figsize=(8, 4))
ax.set_xlim(0, max(x) * 1.1)
ax.set_ylim(0, max(y) * 1.1)
ax.set_xlabel("Jarak Horizontal (m)")
ax.set_ylabel("Ketinggian (m)")
ax.set_title("Animasi Gerak Parabola / Kuadratik")

# titik peluru
(point,) = ax.plot([], [], "o", markersize=10, color="red")

# jejak lintasan
(trail,) = ax.plot([], [], "-", linewidth=2, color="blue")


def update(i):
    # titik utama HARUS berupa list
    point.set_data([x[i]], [y[i]])

    # jejak lintasan berupa array
    trail.set_data(x[:i], y[:i])

    return point, trail


anim = FuncAnimation(fig, update, frames=len(t), interval=20)

plt.show()
