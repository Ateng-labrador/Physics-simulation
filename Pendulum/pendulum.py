import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.patches import ConnectionPatch


def simple_pendulum(theta_0, omega, t, phi):
    return theta_0 * np.cos(omega * t + phi)


theta_0 = np.radians(15)

g = 9.8
l = 1.0
omega = np.sqrt(g / l)


phi = 0
time_span = np.linspace(0, 20, 300)
theta = simple_pendulum(theta_0, omega, time_span, phi)

x = l * np.sin(theta)
y = -l * np.cos(theta)

fig, axis = plt.subplots()

axis.set_xlim(-l - 0.2, l + 0.2)
axis.set_ylim(-l - 0.2, 0.2)


(rod_line,) = axis.plot([], [], lw=2)
(mass_point,) = axis.plot([], [], marker="o", markersize=10)
(trace,) = axis.plot([], [], "-", lw=1, alpha=0.6)


def animate(frame):

    rod_line.set_data([0, x[frame]], [0, y[frame]])
    mass_point.set_data([x[frame]], [y[frame]])
    trace.set_data(x[:frame], y[:frame])

    return rod_line, mass_point, trace


animation = FuncAnimation(
    fig=fig, func=animate, frames=len(time_span), interval=25, blit=True
)

plt.show()
