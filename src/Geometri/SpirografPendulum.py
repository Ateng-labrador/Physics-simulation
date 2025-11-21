# Nabila Khoiriah Amanda Physics UNY 24
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

# Initial Parameter spirograf
speed_profile = -2
repetitions = 25
r1 = 4
r2 = 2

w1 = 1
w2 = speed_profile + 1 / repetitions

p1 = 0
p2 = 0

# Variabel sudut dari awal hingga akhir animasi
theta = np.linspace(0, 2 * repetitions * np.pi, 1500)

# Posisi kompleks lengan spirograf
z1_raw = r1 * np.exp(1j * (w1 * theta + p1))
z2_raw = z1_raw + r2 * np.exp(1j * (w2 * theta + p2))
z_final_raw = z2_raw
frame_count = len(theta)

# Pendulum
A = 3
wp = 0.5
L = 6

x_ball = A * np.sin(wp * theta)
y_ball = -np.sqrt(L**2 - x_ball**2)
z_ball = x_ball + 1j * y_ball

# arm + bandul
z1 = z1_raw + z_ball
z2 = z2_raw + z_ball
z_final = z2

# Plot
fig, ax = plt.subplots()
fig.set_size_inches(5, 5)

ax.set_xlim(-12, 12)
ax.set_ylim(-14, 2)
ax.patch.set_facecolor('lightyellow')
fig.patch.set_facecolor('black')
ax.axis('off')


# Elemen animasi
trace, = ax.plot([], [], color='white', linewidth=1)
arm1, = ax.plot([], [], color='blue', linewidth=2)
arm2, = ax.plot([], [], color='blue', linewidth=2)
string_line, = ax.plot([], [], color='blue', linewidth=3)
ball, = ax.plot([], [], 'o', color='blue', markersize=15)


def update(frame):
    """
    make frame to frame
    """
    # trace spirograf
    trace.set_data(np.real(z_final[:frame]),
                   np.imag(z_final[:frame]))
    # line
    string_line.set_data([0, x_ball[frame]],
                         [0, y_ball[frame]])
    # ball
    ball.set_data([x_ball[frame]], [y_ball[frame]])
    # line red
    arm1.set_data([x_ball[frame], np.real(z1[frame])],
                  [y_ball[frame], np.imag(z1[frame])])
    # line green
    arm2.set_data([np.real(z1[frame]), np.real(z2[frame])],
                  [np.imag(z1[frame]), np.imag(z2[frame])])

    return trace, arm1, arm2, string_line, ball

anim = FuncAnimation(fig, update, frames=frame_count, blit=True)

plt.show()
