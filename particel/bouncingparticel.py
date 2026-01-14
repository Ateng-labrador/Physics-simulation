# https://en.wikipedia.org/wiki/Elasticity_(physics)
# Rifdah Aalyah Zukhuf physics UNY 24
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


# Parameter benda
m1 = 2.0
m2 = 1.0
v1 = 1.4
v2 = -1.2

# Posisi awal
x1 = -4.0
x2 = 4.0

# Simulasi waktu
dt = 0.02
t_max = 10
times = np.arange(0, t_max, dt)

# Menyimpan posisi untuk animasi
x1_list = []
x2_list = []

collided = False

for t in times:
    x1 += v1 * dt
    x2 += v2 * dt

    if not collided and abs(x1 - x2) <= 0.5:
        v1_new = ((m1 - m2) / (m1 + m2)) * v1 + ((2 * m2) / (m1 + m2)) * v2
        v2_new = ((2 * m1) / (m1 + m2)) * v1 + ((m2 - m1) / (m1 + m2)) * v2
        v1, v2 = v1_new, v2_new
        collided = True

    x1_list.append(x1)
    x2_list.append(x2)

# Membuat animasi
fig, ax = plt.subplots(figsize=(8, 3))
ax.set_xlim(-8, 8)
ax.set_ylim(-1, 1)
ax.set_title("Tumbukan Dua Benda (Elastis)")

(obj1,) = ax.plot([], [], "bo", markersize=22)
(obj2,) = ax.plot([], [], "ro", markersize=22)


def update(frame):
    obj1.set_data([x1_list[frame]], [0])
    obj2.set_data([x2_list[frame]], [0])
    return obj1, obj2


anim = FuncAnimation(fig, update, frames=len(times), interval=20)

plt.show()
