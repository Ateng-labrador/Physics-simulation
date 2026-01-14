import numpy as np
import matplotlib.pyplot as plt
from io import BytesIO
import imageio

# code masih error

# Membuat Galaxy spiral
n_points = 2500  # Jumlah titik yang digunakan
t = np.linspace(0, 14 * np.pi, n_points)  # Rentang sudut
r = 0.8 * t  # Jarak radial dari pusat
x = r * np.cos(t) * 2.3  # Mengubah bentuk jadi elips
y = r * np.sin(t)  # Melebar secara horizontal
colors = t / t.max()  # Warna gradasi

# Buat bintang
n_stars = 90  # Jumlah bintangnya
star_x = np.random.uniform(-80, 90, n_stars)  # Posisi di sumbu x
star_y = np.random.uniform(-70, 70, n_stars)  # Posisi di sumbu y

# Menentukan batas tampilan, biar ngga nge zoom out tiba tiba
all_x = np.concatenate([x, star_x])
all_y = np.concatenate([y, star_y])
xlim = (all_x.min(), all_x.max())
ylim = (all_y.min(), all_y.max())

# Plot dasar
plt.style.use("dark_background")  # Warna baground hitam
fig, ax = plt.subplots(figsize=(8, 8))  # Ukuran gambar
ax.set_aspect("equal")  # Skala sumbunya sama
ax.axis("off")

# Membuat frame
frames = []
for frame in range(180):  # Total frame
    ax.clear()
    # Draw static stars
    ax.scatter(
        star_x, star_y, s=3, c="white", alpha=0.8
    )  # Ukuran bintang, warna putih sama transparasinya 0.8
    # Draw growing spiral
    k = max(5, int(frame / 130 * n_points))  # Kontrol kecepatan penggambaran
    ax.scatter(x[:k], y[:k], c=colors[:k], cmap="YlGnBu_r", s=1.3, alpha=0.9)

    # Kunci biar ngga zoom in zoom out
    ax.set_xlim(xlim)
    ax.set_ylim(ylim)

    # simpan ke memori
    buf = BytesIO()
    plt.savefig(buf, dpi=130, facecolor="black", bbox_inches="tight", pad_inches=0)
    buf.seek(0)
    frames.append(imageio.imread(buf))
