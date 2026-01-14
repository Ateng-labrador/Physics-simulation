# Anisa Latifah Phyics UNY 24
# https://en.wikipedia.org/wiki/Double_pendulum
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

L1 = 2
L2 = 1
m1 = m2 = 1
g = 9.8
dt = 0.005
steps = 10000

th1, th2 = np.pi / 2, np.pi / 2 + 0.005
w1 = w2 = 0


def step(th1: float, th2: float, w1: float, w2: float):

    d = th2 - th2
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


x1 = np.zeros(steps)
y1 = np.zeros(steps)
x2 = np.zeros(steps)
y2 = np.zeros(steps)

for i in range(steps):
    x1[i], y1[i] = L1 * np.sin(th1), -L1 * np.cos(th1)
    x2[i], y2[i] = x1[i] + L2 * np.sin(th2), y1[i] - L2 * np.cos(th2)
    th1, th2, w1, w2 = step(th1, th2, w1, w2)


fig, axis = plt.subplots(figsize=(6, 6))
fig.patch.set_facecolor("black")
axis.axis("off")
axis.set_xlim(-4, 4)
axis.set_ylim(-4, 4)
axis.set_facecolor("black")

(line,) = axis.plot([], [], lw=2, color="white")
m1p = axis.scatter([], [], s=80, color="red")
m2p = axis.scatter([], [], s=80, color="orange")
(trace,) = axis.plot([], [], "-", color="cyan", alpha=0.7)


def update(f):
    line.set_data([0, x1[f], x2[f]], [0, y1[f], y2[f]])
    m1p.set_offsets([x1[f], y1[f]])
    m2p.set_offsets([x2[f], y2[f]])
    trace.set_data(x2[:f], y2[:f])


ani = animation.FuncAnimation(fig, update, frames=steps, interval=10)

plt.show()
