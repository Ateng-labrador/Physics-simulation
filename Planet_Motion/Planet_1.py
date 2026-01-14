# https://en.wikipedia.org/wiki/Orbital_mechanics
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation


# Dea Ananta Sari Physics UNY 2024


# intial parameter
t = np.linspace(0, 2 * np.pi, 200)
r = 3
x = r * np.cos(t)
y = r * np.sin(t)

# figure for animation
fig, ax = plt.subplots()
sun = ax.scatter(0, 0, c="yellow", s=200, label="Matahari")
planet = ax.scatter(x[0], y[0], c="blue", s=40, label="Planet")
orbit = ax.plot(x[0], y[0], "--", color="white", linewidth=1)[0]

# make the canvas
fig.patch.set_facecolor("black")
plt.axis("off")
ax.set(
    xlim=[-7, 7], ylim=[-7, 7], xlabel="x", ylabel="y", title="Animasi Rotasi Planet"
)
ax.set_aspect("equal")
ax.grid(False)
leg = ax.legend()
leg.get_frame().set_facecolor("white")
leg.get_frame().set_edgecolor("white")
for txt in leg.get_texts():
    txt.set_color("black")


# make frame for frame
def update(frame):
    planet.set_offsets([x[frame], y[frame]])
    orbit.set_xdata(x[:frame])
    orbit.set_ydata(y[:frame])


ani = animation.FuncAnimation(fig=fig, func=update, frames=len(t), interval=30)

plt.show()
