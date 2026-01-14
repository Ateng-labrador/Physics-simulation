# https://en.wikipedia.org/wiki/Oscillation
# Maria Riani Putri Widyastuti Physics UNY 24
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Parameter fisika
A = 1.0
gamma = 0.10
omega = 2.5
y0 = -0.5


def y(t):
    return y0 + A*np.exp(-gamma*t) * np.cos(omega*t)


t_vals = np.linspace(0, 20, 1000)
fig, ax = plt.subplots(figsize=(6, 7))
ax.set_ylim(-2, 1)
ax.set_title("Gelombang Sinkron dari Gerak Osilator Teredam")
ax.set_xlabel("x")
ax.set_ylabel("y")


ball, = ax.plot([], [], 'o', color='red', markersize=25)


spring, = ax.plot([], [], color='black')


wave_line, = ax.plot([], [], color='blue', linewidth=2)

# List gelombang
x_wave = []
y_wave = []


anchor_x, anchor_y = 0, 1
ax.plot(anchor_x, anchor_y, 'ks', markersize=10)

scroll_speed = 0.05
center_x = 0


def update(t):

    ypos = y(t)

    ball.set_data([0], [ypos])

    spring_y = np.linspace(anchor_y, ypos, 60)
    spring_x = 0.15 * np.sin(12 * np.linspace(0, np.pi*4, 60))
    spring.set_data(spring_x, spring_y)

    x_wave.append(center_x)
    y_wave.append(ypos)

    x_wave[:] = [x - scroll_speed for x in x_wave]

    left_bound = x_wave[0] - 1
    right_bound = x_wave[-1] + 1
    ax.set_xlim(left_bound, right_bound)

    wave_line.set_data(x_wave, y_wave)

    return ball, spring, wave_line


ani = FuncAnimation(fig,
                    update,
                    frames=t_vals,
                    interval=30)

plt.show()
