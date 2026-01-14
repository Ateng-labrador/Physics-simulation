import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


t = np.linspace(0, 10, 100)
x_1 = np.cos(t)
x_2 = np.sin(t)
x_3 = np.tan(t)

fig, axis = plt.subplots()

axis.set_xlim([min(t), max(t)])
axis.set_ylim([-2, 2])
(animated_cos,) = axis.plot([], [], color="red")
(animated_sin,) = axis.plot([], [], color="blue")
(animated_tan,) = axis.plot([], [], color="green")

plt.grid()


def update_data(frame):
    animated_cos.set_data(t[:frame], x_1[:frame])
    animated_sin.set_data(t[:frame], x_2[:frame])
    animated_tan.set_data(t[:frame], x_3[:frame])
    return animated_cos, animated_sin, animated_tan


animation = FuncAnimation(fig=fig, func=update_data, frames=len(t), interval=25)

plt.show()
