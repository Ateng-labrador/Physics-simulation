# Fellycia Putri Suntoyo Physics UNY 24
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


g = 9.8
v0 = 20
theta = 45

theta_rad = np.deg2rad(theta)

v0x = v0 * np.cos(theta_rad)
v0y = v0 * np.sin(theta_rad)

t_flight = 2 * v0y / g
t = np.linspace(0, t_flight, 400)


x = v0x * t
y = v0y * t - 0.5 * g * t**2


fig, ax = plt.subplots()
ax.set_xlim(0, float(x.max()) * 1.1)
ax.set_ylim(0, float(y.max()) * 1.2)
ax.set_xlabel("x (m)")
ax.set_ylabel("y (m)")
ax.set_title("Animasi Gerak Parabola")

ax.grid(True)


ax.plot(x, y, linestyle="--", color="purple")


(point,) = ax.plot([], [], "o", markersize=10, color="red")


def init():
    point.set_data([], [])
    return (point,)


def update(frame):
    point.set_data([x[frame]], [y[frame]])
    return (point,)


ani = FuncAnimation(fig, update, frames=len(t), init_func=init, blit=True, interval=40)

plt.show()
