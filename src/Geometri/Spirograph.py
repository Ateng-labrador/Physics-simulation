# https://en.wikipedia.org/wiki/Spirograph
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anim

# Ikhsan Fahrizal Nurfarid Pyhsics UNY 24

# initial parameter
r1, r2, r3 = 4, 4, 1.3
w1, w2, w3 = 44, -17, -54
theta = np.linspace(0, 2*np.pi, 1000)
z = (r1*np.exp(1j*w1*theta) +
     r2*np.exp(1j*w2*theta) +
     r3*np.exp(1j*w3*theta))
x = np.real(z)
y = np.imag(z)

# Make the canvas
fig, ax = plt.subplots(figsize=(5, 5))
fig.patch.set_facecolor('pink')

ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.set_aspect('equal')
ax.axis('off')

# make the figure
line, = ax.plot([], [], lw=1.5, color="white")


# make frame to frame
def update(frame):
    """
    fuction for make frame to animation
    figure.
    """
    line.set_data(x[:frame], y[:frame])
    return line,


ani = anim.FuncAnimation(fig,
                         update,
                         frames=len(x),
                         interval=5,
                         blit=True)


plt.show()
