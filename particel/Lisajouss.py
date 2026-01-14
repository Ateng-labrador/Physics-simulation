# Yuliani Saputri
# https://en.wikipedia.org/wiki/Lissajous_curve
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# parameter
A = 1.5
B = 1.0
wx = 3
wy = 2
delta = np.pi / 3

t = np.linspace(0, 10, 1000)

# Persamaan Lissajous
x = A * np.sin(wx * t + delta)
y = B * np.sin(wy * t)


fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_aspect("equal")
ax.set_title("Animasi Kurva Lissajous (Superposisi Gerak Harmonik 2D)")
ax.set_xlabel("x(t)")
ax.set_ylabel("y(t)")

(point,) = ax.plot([], [], "ro", ms=8)
(trail,) = ax.plot([], [], "-", lw=1)


def update(frame):
    point.set_data([x[frame]], [y[frame]])
    trail.set_data(x[:frame], y[:frame])
    return point, trail


ani = animation.FuncAnimation(fig, update, frames=len(t), interval=10)
plt.show()
