# https://en.wikipedia.org/wiki/Central_force
# Keisya Latifa Physics UNY 24
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


# SETUP FIGURE
fig, ax = plt.subplots(figsize=(7, 7))
fig.patch.set_facecolor("#F8F1FF")
ax.set_facecolor("#F8F1FF")
ax.set_xlim(-8, 8)
ax.set_ylim(-8, 8)
ax.set_aspect("equal")
ax.axis("off")
ax.set_title(
    "Gerak Partikel dalam Medan Gaya Sentral", color="#7A77B9", fontsize=15, pad=15
)

# Parameter
k = 5.0
dt = 0.05
m = 1.0

x, y = 4.0, 0.0
vx, vy = 0.0, 1.4


# warna
particle_color = "#48b05b"
trail_color = "#e028d4"
center_color = "#2712e6"

# particel dan jejak
particle = ax.scatter([], [], s=60, color=particle_color)
(track,) = ax.plot([], [], color=trail_color, linewidth=2)

# pusat gaya
ax.scatter(0, 0, s=150, color=center_color)


# Gaya sentral
def central_force(x, y):
    r = np.sqrt(x**2 + y**2)
    Fx = -k * x / (r + 1e-6)
    Fy = -k * y / (r + 1e-6)

    return Fx, Fy


trail_x = []
trail_y = []


def update(frame):

    global x, y, vx, vy
    Fx, Fy = central_force(x, y)

    vx += (Fx / m) * dt
    vy += (Fy / m) * dt

    x += vx * dt
    y += vy * dt

    trail_x.append(x)
    trail_y.append(y)

    particle.set_offsets([x, y])
    track.set_data(trail_x, trail_y)

    return particle, track


# ANIMASI
ani = animation.FuncAnimation(fig, update, frames=1000, interval=20)


plt.show()
