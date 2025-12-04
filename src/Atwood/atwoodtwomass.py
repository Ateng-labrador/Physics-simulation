# Atika Rifa Amanih Physics UNY 24
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


mA = 6.0
mB = 2.0
g = 9.8
a = (mA * g) / (mA + mB)
yA0 = -1.0
xB0 = -4.0
px, py = 0.0, 0.0
L = (px - xB0) + (yA0 - py) + 5

x_stop = px - 0.4
max_s = x_stop - xB0
dt = 0.03
t_stop = np.sqrt(2 * max_s / a)
frames = int(t_stop / dt)

fig, axis = plt.subplots(figsize=(7, 6))
axis.set_xlim(-5, 1.5)
axis.set_ylim(-5, 2)
axis.set_aspect('equal')
axis.axis('off')

blockB, = axis.plot([], [], lw=4, color='blue')
blockA, = axis.plot([], [], lw=4, color='red')

rope_h, = axis.plot([], [], color='saddlebrown', lw=3)
rope_v, = axis.plot([], [], color='saddlebrown', lw=3)

labelB = axis.text(0, 0, "", fontsize=14, color="blue", weight="bold")
labelA = axis.text(0, 0, "", fontsize=14, color="red",  weight="bold")

theta = np.linspace(0, 2*np.pi, 200)
R = 0.2
axis.plot(px + R*np.cos(theta), py + R*np.sin(theta), color='black', lw=3)
time_text = axis.text(0.02, 0.05, "", transform=axis.transAxes)


def update(f):
    t = f * dt
    s = 0.5 * a * t**2
    xB = xB0 + s
    yA = yA0 - s
    if xB >= px - 0.2:
        xB = px - 0.2
        yA = yA0 - ((xB - xB0))

    size = 0.25
    blockB.set_data(
        [xB-size, xB+size, xB+size, xB-size, xB-size],
        [0-size,  0-size,  0+size,  0+size,  0-size]
    )
    blockA.set_data(
        [-size, +size, +size, -size, -size],
        [yA-size, yA-size, yA+size, yA+size, yA-size]
    )
    rope_h.set_data([xB+size, px], [0, 0])
    rope_v.set_data([px, 0], [0, yA+size])

    labelB.set_position((xB, 0.4))
    labelB.set_text(f"m = {mB} kg")

    labelA.set_position((0.4, yA))
    labelA.set_text(f"m = {mA} kg")

    time_text.set_text(f"t = {t:.2f} s")

    return blockB, blockA, rope_h, rope_v, labelB, labelA, time_text


ani = FuncAnimation(fig,
                    update,
                    frames=frames,
                    interval=40,
                    repeat=False)
plt.show()
