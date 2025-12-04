# Siti Salmah Putri Zahara Pyhsics UNY 24
# https://en.wikipedia.org/wiki/Love
# https://youtu.be/vGJTaP6anOU?si=uLgNkNqgNCiZUlWf&t=55
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# parameter
t = np.linspace(0, 2*np.pi, 500)
x = 16 * np.sin(t)**3
y = 13*np.cos(t) - 5*np.cos(2*t) - 2*np.cos(3*t) - np.cos(4*t)

# buat kanvas
fig, ax = plt.subplots(figsize=(6, 6))
fig.patch.set_facecolor("black")
ax.set_facecolor("black")
ax.axis("off")
line, = ax.plot([], [], color="red", linewidth=4)


# buat frame to frame
def animate(frame):
    ax.cla()
    ax.set_facecolor("black")
    ax.axis("off")

    scale = 1 + 0.25 * np.sin(frame * 0.5)

    pulse = (np.sin(frame*0.5) + 1) / 2
    color = (1, pulse, pulse)

    ax.plot(scale*x, scale*y, color=color, linewidth=4)

    ax.set_xlim(-20, 20)
    ax.set_ylim(-20, 20)


ani = FuncAnimation(fig,
                    animate,
                    frames=300,
                    interval=30)

plt.show()
