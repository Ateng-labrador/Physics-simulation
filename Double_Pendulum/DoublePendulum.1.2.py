# https://en.wikipedia.org/wiki/Double_pendulum
# DoublePendulum version 1.2
import numpy as np
import string
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


L1: float = 2
L2: float = 1
m1: float = 1
m2: float = 1
g: float = 9.8
w1: float = 0
w2: float = 0
dt: float = 0.005
th1: float = np.pi / 2
th2: float = np.pi / 2 + 0.005


def parameter(th1: float, th2: float, w1: float, w2: float) -> tuple:
    """
    Membuat parameter untuk step
    """
    d = th2 - th1
    s, c = np.sin(d), np.cos(d)
    D = (m1 + m2) * L1 - m2 * L1 * c * c
    D2 = D * ((L2 / L1))

    a1 = (
        m2 * (L1 * w1 * w1 * s * c + L2 * w2 * w2 * s + g * np.sin(th2) * c)
        - (m1 + m2) * g * np.sin(th1)
    ) / D

    a2 = (
        ((m1 + m2) * (g * (np.sin(th1) * c - np.sin(th2)) - L1 * w1 * w1 * s))
        - m2 * L2 * w2 * w2 * s * c
    ) / D2

    w1 += a1 * dt
    w2 += a2 * dt
    return th1 + w1 * dt, th2 + w2 * dt, w1, w2


def setup_axis(axis):
    """
    membuat setup axis
    """
    axis.set_xlim(-4, 4)
    axis.set_ylim(-4, 4)
    axis.set_facecolor("black")
    return axis


def random_hex() -> str:
    """
    membuat random color
    """
    hex_value = "".join(np.random.choice(list(string.hexdigits), 6))
    return f"#{hex_value}"


def setup_plot(axis):
    """Fungsi untuk membuat setting plot"""
    (line,) = axis.plot([], [], lw=2, color="white")
    m1p = axis.scatter([], [], s=80, color=random_hex())
    m2p = axis.scatter([], [], s=80, color=random_hex())
    (trace,) = axis.plot([], [], "-", color=random_hex(), alpha=0.7)
    return line, m1p, m2p, trace


def update(i, x1, y1, x2, y2, line, m1p, m2p, trace):
    """
    Fungsi untuk membuat frame
    """
    line.set_data([0, x1[i], x2[i]], [0, y1[i], y2[i]])
    m1p.set_offsets([[x1[i], y1[i]]])
    m2p.set_offsets([[x2[i], y2[i]]])
    trace.set_data(x2[:i], y2[:i])
    return line, m1p, m2p, trace


if __name__ == "__main__":
    steps = 10000
    x1 = np.zeros(steps)
    y1 = np.zeros(steps)
    x2 = np.zeros(steps)
    y2 = np.zeros(steps)

    for i in range(steps):
        x1[i], y1[i] = L1 * np.sin(th1), -L1 * np.cos(th1)
        x2[i], y2[i] = x1[i] + L2 * np.sin(th2), y1[i] - L2 * np.cos(th2)
        th1, th2, w1, w2 = parameter(th1, th2, w1, w2)

    fig, axis = plt.subplots(figsize=(5, 5))
    fig.patch.set_facecolor("black")
    axis.axis("off")
    axis = setup_axis(axis)
    line, m1p, m2p, trace = setup_plot(axis)

    def init():
        line.set_data([], [])
        m1p.set_offsets(np.empty((0, 2)))
        m2p.set_offsets(np.empty((0, 2)))
        trace.set_data([], [])
        return line, m1p, m2p, trace

    ani = FuncAnimation(
        fig=fig,
        func=update,
        fargs=(x1, y1, x2, y2, line, m1p, m2p, trace),
        init_func=init,
        frames=steps,
        interval=10,
    )

plt.show()
