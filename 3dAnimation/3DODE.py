# Ismail Rijal Robbani physics UNY
# https://en.wikipedia.org/wiki/Attractor
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.colors import ListedColormap
from mpl_toolkits.mplot3d.art3d import Line3DCollection

# Parameter Aizawa Attractor
alpha = 0.95
beta = 0.70
delta = 3.50
eps = 0.25
gamma = 0.60
zeta = 0.10


# Persamaan diferensial Atraktor Aizawa
def aizawa_deriv(state):
    x, y, z = state
    M = np.array(
        [
            [z - beta, -delta, 0],
            [delta, z - beta, 0],
            [
                -x * (eps * z + 1),
                -y * (eps * z + 1),
                zeta * x**3 - (1 / 3) * z**2 + alpha,
            ],
        ]
    )
    vec = np.array([x, y, z])
    bias = np.array([0, 0, gamma])
    return M @ vec + bias


dt = 0.005
steps = 20000
state = np.array([0.1, 0.0, 0.0])

xs, ys, zs = [], [], []

for _ in range(steps):
    k1 = aizawa_deriv(state)
    k2 = aizawa_deriv(state + 0.5 * dt * k1)
    k3 = aizawa_deriv(state + 0.5 * dt * k2)
    k4 = aizawa_deriv(state + dt * k3)
    state = state + (dt / 6) * (k1 + 2 * k2 + 2 * k3 + k4)

    xs.append(state[0])
    ys.append(state[1])
    zs.append(state[2])

xs = np.array(xs)
ys = np.array(ys)
zs = np.array(zs)


cmap_line = ListedColormap(
    ["aqua", "midnightblue", "purple", "royalblue", "violet", "fuchsia", "plum"]
)
colors_line = cmap_line(np.linspace(0, 1, len(xs) - 1))

segments = np.array(
    [
        [[xs[i], ys[i], zs[i]], [xs[i + 1], ys[i + 1], zs[i + 1]]]
        for i in range(len(xs) - 1)
    ]
)


fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection="3d")


padding = 0.5
ax.set_xlim(xs.min() - padding, xs.max() + padding)
ax.set_ylim(ys.min() - padding, ys.max() + padding)
ax.set_zlim(zs.min() - padding, zs.max() + padding)
ax.set_title("Aizawa Attractor - Artistic Animation")


lc = Line3DCollection(segments[:1], colors=colors_line[:1], linewidths=0.5, alpha=0.6)
ax.add_collection3d(lc)


num_points = 80
offset_scale = 0.2
rand_idx = np.random.choice(len(xs), num_points)
points = np.vstack([xs[rand_idx], ys[rand_idx], zs[rand_idx]]).T
point_offsets = (np.random.rand(num_points, 3) - 0.5) * offset_scale


colors_points = np.random.choice(
    ["aqua", "midnightblue", "purple", "royalblue", "violet", "fuchsia", "plum"],
    size=num_points,
)
scatter = ax.scatter(
    points[:, 0], points[:, 1], points[:, 2], c=colors_points, s=15, alpha=0.4
)

frames = 500
skip = max(len(segments) // frames, 1)


def update(frame):
    idx = frame * skip
    lc.set_segments(segments[:idx])
    lc.set_color(colors_line[:idx])

    lag = 0.3
    t_idx = (rand_idx + int(frame * skip * lag)) % len(xs)
    new_points = np.vstack(
        [
            xs[t_idx] + point_offsets[:, 0],
            ys[t_idx] + point_offsets[:, 1],
            zs[t_idx] + point_offsets[:, 2],
        ]
    ).T
    scatter._offsets3d = (new_points[:, 0], new_points[:, 1], new_points[:, 2])

    if frame > 0.3 * frames:
        progress = (frame - 0.3 * frames) / (0.7 * frames)
        elev = 10 + progress * 50
        azim = progress * 360
        ax.view_init(elev=elev, azim=azim)

    return lc, scatter


# Animasi
anim = FuncAnimation(fig, update, frames=frames, interval=20, blit=False)

plt.show()

if __name__ == "__main__":
    pass
