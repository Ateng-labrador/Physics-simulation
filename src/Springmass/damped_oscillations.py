# Annisa Ulkhotimah Physics UNY 24
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


A, w, b1, b2 = 1, 6, 0.15, 0.40
t = np.linspace(0, 10, 400)

# Make math equations
x1 = A * np.exp(-b1 * t) * np.cos(w * t)
x2 = A * np.exp(-b2 * t) * np.cos(w * t)


fig, ax = plt.subplots()

scat1 = ax.scatter(t[0], x1[0], c="b", s=15, label=f"b={b1}")
line2, = ax.plot(t[0], x2[0], c="r", label=f"b={b2}")

ax.set(xlim=[0,10],
       ylim=[-1.2,1.2],
       xlabel="t (s)",
       ylabel="x(t)",
       title="Perbandingan Osilasi Teredam")
ax.legend()


def update(frame):
    """
    Make frame to frame
    """
    data1 = np.stack((t[:frame], x1[:frame]))
    scat1.set_offsets(data1)

    line2.set_xdata(t[:frame])
    line2.set_ydata(x2[:frame])

    return scat1, line2

ani = animation.FuncAnimation(fig,
                              update,
                              frames=len(t),
                              interval=30,
                              blit=True)


plt.tight_layout()
plt.show()
