import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

m = 0.05
g = 9.81
k = 1500.0
c = 1.0
radius = 0.12
vy0 = 0.0
dt = 0.002
t_max = 8.0
y0 = 5

n_steps = int(t_max / dt) + 1
t = np.linspace(0, t_max, n_steps)
y = np.zeros(n_steps)
vy = np.zeros(n_steps)
y[0] = y0
vy[0] = vy0

for i in range(n_steps - 1):
    Fg = -m * g
    penetration = radius - y[i]

    if penetration > 0:
        Fk = k * penetration
        Fc = -c * vy[i]
        Fnet = Fg + Fk + Fc
    else:
        Fnet = Fg

    a = Fnet / m
    vy[i + 1] = vy[i] + a * dt
    y[i + 1] = y[i] + vy[i + 1] * dt

    if y[i + 1] < -1.0:
        y[i + 1] = radius
        vy[i + 1] = 0.0

# Buat animasi
max_frames = 400
indices = np.linspace(0, n_steps - 1, max_frames).astype(int)

fig, ax = plt.subplots(figsize=(4, 6))

ax.set_xlim(-0.5, 0.5)
ax.set_ylim(-0.05, max(y0 + 0.5, y0 * 1.2))
ax.set_aspect("equal")
ax.set_xlabel("x (m)")
ax.set_ylabel("y (m)")
ax.set_title("Bekel: Jatuh & Osilasi Teredam")
ax.plot([-1, 1], [0, 0], linewidth=2)

ball = plt.Circle((0, y[0]), radius=radius)

ax.add_patch(ball)

time_text = ax.text(0.02, 0.95, "", transform=ax.transAxes)

plt.close(fig)
fig2, ax2 = plt.subplots(figsize=(4, 6))
ax2.plot([-1, 1], [0, 0], linewidth=2)
circ = plt.Circle((0, y[-1]), radius=radius)
ax2.add_patch(circ)
ax2.set_xlim(-0.5, 0.5)
ax2.set_ylim(-0.05, max(y0 + 0.5, y0 * 1.2))
ax2.set_aspect("equal")
ax2.set_title("Preview frame terakhir")


def init():
    ball.center = (0, y[0])
    time_text.set_text("t = 0.00 s")
    return (ball, time_text)


def animate(frame_i):
    i = indices[frame_i]
    ball.center = (0, y[i])
    time_text.set_text(f"t = {t[i]:.3f} s")
    return (ball, time_text)


anim = animation.FuncAnimation(
    fig, animate, frames=len(indices), init_func=init, blit=True, interval=25
)

plt.show()
