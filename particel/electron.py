# Husein Muhammad Irsyad Physiscs UNY 24
# https://en.wikipedia.org/wiki/Electron
# belum di up
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


# Pengaturan awal
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.set_aspect("equal")
ax.axis("off")
ax.set_title("Simulasi Atom Perak (Ag)", color="white", fontsize=14)
ax.set_facecolor("black")

# Nukleus (inti atom)
rp = np.random.randn(29, 2) * 0.3
rn = np.random.randn(34, 2) * 0.3
proton = ax.plot(rp[:, 0], rp[:, 1], "o", color="yellow", markersize=6)
neutron = ax.plot(rn[:, 0], rn[:, 1], "o", color="cyan", markersize=6)

# elektron-elektron
jumlah_elektron_per_lintasan = [2, 8, 18, 1]
warna_lintasan = ["red", "red", "red", "red"]
jarak_lintasan = [2, 4, 6, 8]
kecepatan_lintasan = [0.24, 0.12, 0.06, 0.04]
garis_lintasan = [ax.plot([], [], "--", color=w, alpha=0.3)[0] for w in warna_lintasan]


elektron_points = []
for n, warna in zip(jumlah_elektron_per_lintasan, warna_lintasan):
    elektron_points.append(
        [ax.plot([], [], "o", color=warna, markersize=8)[0] for _ in range(n)]
    )


# inisialisasi awal animasi
def init():
    for group, garis in zip(elektron_points, garis_lintasan):
        for e in group:
            e.set_data([], [])
        garis.set_data([], [])
    return [e for group in elektron_points for e in group] + garis_lintasan


# Update frame
def update(frame):
    for i, (r, kecepatan, group, garis) in enumerate(
        zip(jarak_lintasan, kecepatan_lintasan, elektron_points, garis_lintasan)
    ):
        n = len(group)
        for j, e in enumerate(group):
            sudut = frame * kecepatan + 2 * np.pi * j / n
            x = r * np.cos(sudut)
            y = r * np.sin(sudut)
            e.set_data([x], [y])

        # Lintasan
        theta = np.linspace(0, 2 * np.pi, 100)
        lx = r * np.cos(theta)
        ly = r * np.sin(theta)
        garis.set_data(lx, ly)
    return [e for group in elektron_points for e in group] + garis_lintasan


# Animasi
ani = animation.FuncAnimation(
    fig, update, frames=1000, init_func=init, blit=True, interval=30
)

plt.show()
