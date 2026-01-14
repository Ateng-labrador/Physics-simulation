import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

m = 1
k = 1
d = 0.2

# kecepatan terhadap simpangan

t = np.linspace(0, 40, 501)
w_d = np.sqrt((4 * m * k - d**2) / (4 * m**2))
x = np.exp(-d / (2 * m) * t) * np.cos(w_d * t)
v = np.exp(-d / (2 * m) * t) * (-d / (2 * m) * np.cos(w_d * t) - w_d * np.sin(w_d * t))

fig, axis = plt.subplots(1, 3)

(animated_x,) = axis[0].plot([], [], color="green")
axis[0].set_title("Simpangan")
axis[0].set_xlim([min(t), max(t)])
axis[0].set_ylim([-2, 2])
axis[0].grid()


(animated_v,) = axis[1].plot([], [], color="blue")
axis[1].set_title("Kecepatan")
axis[1].set_xlim([min(t), max(t)])
axis[1].set_ylim([-2, 2])
axis[1].grid()


(animated_v_x,) = axis[2].plot([], [], color="red")
axis[2].set_title("Kecepatan simpagan")
axis[2].set_xlim([-1.5, 1.5])
axis[2].set_ylim([-1.5, 1.5])
axis[2].grid()


def update(frame):
    animated_v.set_data(t[:frame], v[:frame])
    animated_x.set_data(t[:frame], x[:frame])
    animated_v_x.set_data(v[:frame], x[:frame])

    return animated_x, animated_v, animated_v_x


animation = FuncAnimation(
    fig=fig,
    func=update,
    frames=len(t),
    interval=25,
)
plt.show()
