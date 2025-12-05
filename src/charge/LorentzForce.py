# https://en.wikipedia.org/wiki/Lorentz_force
# Anisa Rania Putri Physics UNY 24
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Setup figure
fig, ax = plt.subplots(figsize=(10, 10))
ax.set_facecolor('#0a0a0a')
fig.patch.set_facecolor('#0a0a0a')

# Parameter
q = 1.0
m = 1.0
B = 0.8
dt = 0.02
n = 400

# Kondisi awal 4 partikel: [x, y, vx, vy]
# Partikel bergerak melingkar karena gaya Lorentz F = q(v × B)
p1 = np.array([0., 0., 3., 0.])
p2 = np.array([0., 0., 2., 1.])
p3 = np.array([0., 0., 1.5, 1.5])
p4 = np.array([0., 0., -2., 0.5])

particles = [p1, p2, p3, p4]
colors = ['#00ff41', '#ff006e', '#00d9ff', '#ffbe0b']

# Simulasi gerak partikel dengan Gaya Lorentz
trajectories = []
for p in particles:
    traj = np.zeros((n, 2))
    r = p[:2].copy()
    v = p[2:].copy()

    for i in range(n):
        traj[i] = r
        # Gaya Lorentz 2D: F = q(v × B), untuk B searah Z
        # Fx = q*vy*B, Fy = -q*vx*B
        F = q * np.array([v[1]*B, -v[0]*B])
        a = F / m
        v = v + a * dt
        r = r + v * dt

    trajectories.append(traj)

# Jejak
lines = []
for i, traj in enumerate(trajectories):
    line = ax.plot([], [], color=colors[i], linewidth=2, alpha=0.8)[0]
    lines.append(line)

# Partikel
scatters = []
for i in range(len(trajectories)):
    scat = ax.scatter([], [], c=colors[i], s=150,
                      edgecolors='white',
                      linewidths=2,
                      zorder=10)
    scatters.append(scat)

# medan magnet lingkaran
circle = plt.Circle((0, 0), 5, color='purple',
                    fill=False, linewidth=2,
                    linestyle='--', alpha=0.3)
ax.add_patch(circle)

# label
info_text = ax.text(0.02,
                    0.98,
                    '',
                    transform=ax.transAxes,
                    color='white',
                    fontsize=11,
                    verticalalignment='top',
                    fontfamily='monospace')

# sumbu
ax.set(xlim=[-6, 6], ylim=[-6, 6], aspect='equal')
ax.set_xlabel('X (meter)', color='white', fontsize=12)
ax.set_ylabel('Y (meter)', color='white', fontsize=12)
ax.set_title('Partikel Bermuatan dalam Medan Magnetik\nF = q(v × B)',
             color='white',
             fontsize=14,
             fontweight='bold',
             pad=20)
ax.tick_params(colors='white')
ax.grid(True, alpha=0.2, color='gray')

# Hilangkan border
for spine in ax.spines.values():
    spine.set_edgecolor('#333333')


# Fungsi update untuk animasi
def update(frame):
    # Update jejak (trail effect - hanya 50 frame terakhir)
    for i, traj in enumerate(trajectories):
        start = max(0, frame - 50)
        lines[i].set_data(traj[start:frame, 0], traj[start:frame, 1])

        # Update posisi partikel
        if frame < n:
            scatters[i].set_offsets([traj[frame, 0], traj[frame, 1]])

    # Update info text
    info_text.set_text(f'Frame: {frame}/{n}\nB = {B} Tesla\nq = {q} C')

    return lines + scatters + [info_text]


# Buat animasi
ani = animation.FuncAnimation(fig=fig,
                              func=update,
                              frames=n,
                              interval=30,
                              blit=True,
                              repeat=True)


plt.tight_layout()
plt.show()
