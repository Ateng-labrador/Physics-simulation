# Septi Nur Hidayah Physics UNY 24
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter

# Parameter GHS
A = 1.0
omega = 2 * np.pi
phi = 0
t_max = 6
dt = 0.02

t = np.arange(0, t_max, dt)
x = A * np.cos(omega * t + phi)

# Membuat lintasan 3D (bolak-balik pada sumbu x, y & z)
y = 0.3 * np.sin(omega * t)
z = 0.3 * np.sin(2 * omega * t)

# Setup figure
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection="3d")
ax.set_title("Simulasi Gerak Harmonik Sederhana")
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-0.5, 0.5)
ax.set_zlim(-0.5, 0.5)
ax.set_xlabel("X (m)")
ax.set_ylabel("Y")
ax.set_zlabel("Z")

# Objek bola GHS
(ball,) = ax.plot([], [], [], "o", markersize=12, color="red")

(trail,) = ax.plot([], [], [], lw=1, color="blue")


# Fungsi update animasi
def update(frame):
    ball.set_data([x[frame]], [y[frame]])
    ball.set_3d_properties([z[frame]])
    trail.set_data(x[:frame], y[:frame])
    trail.set_3d_properties(z[:frame])
    return ball, trail


anim = FuncAnimation(fig, update, frames=len(t), interval=20, blit=True)

gif_writer = PillowWriter(fps=40)

plt.show()
