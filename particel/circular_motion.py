# Husnul khatimah physics UNY 24
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


R = 5

theta0 = np.array([0, np.pi/2, np.pi, 3*np.pi/2])

fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.set_xlim(-6, 6)
ax.set_ylim(-6, 6)

# Gambar lingkaran garis saja
theta = np.linspace(0, 2*np.pi, 500)
ax.plot(R*np.cos(theta), R*np.sin(theta), 'k', linewidth=2)

# Objek titik
points, = ax.plot([], [], 'ro', markersize=10)

# Objek panah (4 panah)
arrows = [ax.arrow(0, 0, 0, 0, color='red', head_width=0.25, head_length=0.4)
          for _ in range(4)]


def init():
    points.set_data([], [])
    return [points] + arrows


def update(frame):
    angle = frame * 0.05  # Kecepatan angular

    # Hitung posisi titik
    x = R * np.cos(theta0 + angle)
    y = R * np.sin(theta0 + angle)
    points.set_data(x, y)

    # Update panah ke empat titik (panjang dipanjangin)
    for i, arrow in enumerate(arrows):
        arrow.remove()  # hapus panah lama
    arrows.clear()

    for i in range(4):
        vx = -np.sin(theta0[i] + angle) * 2
        vy = np.cos(theta0[i] + angle) * 2

        new_arrow = ax.arrow(x[i], y[i], vx, vy, color='red',
                             head_width=0.25, head_length=0.4)
        arrows.append(new_arrow)
    return [points] + arrows


# Membuat animasi
anim = FuncAnimation(fig,
                     update,
                     frames=1000,
                     interval=30,
                     init_func=init)

plt.show()
