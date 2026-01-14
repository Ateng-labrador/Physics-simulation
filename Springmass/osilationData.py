# Rahayu Widyasari physics UNY 24
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
import matplotlib.gridspec as gridspec

ydata = np.array(
    [
        -12.129,
        -12.129,
        -11.196,
        -9.874,
        -8.397,
        -6.609,
        -4.821,
        -2.799,
        -0.933,
        0.389,
        2.799,
        3.732,
        5.598,
        6.687,
        8.164,
        9.097,
        9.797,
        10.496,
        10.807,
        10.807,
        10.807,
        10.730,
        10.341,
        9.330,
        8.397,
        7.464,
        6.376,
        4.898,
        3.732,
        2.177,
        0.933,
        -0.078,
        -1.555,
        -2.644,
        -3.888,
        -4.587,
        -5.365,
        -5.831,
        -6.220,
        -5.987,
        -6.065,
        -5.520,
        -4.976,
        -4.276,
        -3.032,
        -2.099,
        -1.400,
        0.311,
        1.244,
        2.177,
        3.032,
        3.888,
        4.898,
        5.520,
        5.987,
        6.609,
        6.998,
        7.309,
        7.309,
        6.998,
        6.609,
        6.142,
        5.831,
        5.054,
        4.199,
        3.577,
        2.721,
        1.711,
        0.544,
        -0.311,
        -0.933,
        -1.866,
        -2.644,
        -3.421,
        -3.810,
        -4.121,
        -4.121,
        -4.043,
        -3.654,
        -3.499,
        -3.266,
        -2.566,
        -2.022,
        -1.166,
        -0.467,
        0.622,
        1.322,
        2.022,
        2.644,
        3.577,
        4.121,
        4.587,
        5.132,
        5.443,
        5.598,
        5.365,
        5.365,
        5.132,
        4.821,
        4.432,
        4.121,
        3.810,
        3.032,
        2.255,
        1.633,
        0.933,
        0.156,
        -0.544,
        -1.089,
        -1.711,
        -2.333,
        -2.255,
        -2.566,
        -2.721,
        -2.644,
        -2.566,
        -2.255,
        -1.944,
        -1.711,
        -1.089,
        -0.778,
        -0.311,
        0.544,
        0.855,
        1.477,
        2.177,
        2.644,
        2.955,
        3.499,
        3.732,
        3.732,
        3.732,
        3.810,
        3.810,
        3.499,
        3.188,
        2.955,
        2.488,
        2.022,
        1.500,
        0.778,
        0.311,
        -0.156,
        -0.622,
        -1.011,
        -1.244,
        -1.322,
        -1.166,
        -0.855,
        -0.467,
        0.000,
        0.389,
        0.700,
        0.933,
        1.089,
        1.166,
        1.089,
        0.855,
        0.544,
        0.156,
        -0.233,
        -0.622,
        -0.855,
        -0.933,
        -0.855,
        -0.700,
        -0.467,
        -0.233,
        -0.078,
        0.000,
    ]
)

dt = 1 / 30
t = np.arange(0, len(ydata) * dt, dt)

A = 11.129
m = 255.5
b = 162
u = b / (2 * m)
T = 1.265
Wd = (2 * np.pi) / T

y_theory = -A * np.exp(-u * t) * np.cos(Wd * t)


fig = plt.figure(figsize=(7, 6))
gs = gridspec.GridSpec(3, 2, width_ratios=[1, 2.5], height_ratios=[1, 1, 1])

ax_ball_prak = fig.add_subplot(gs[0, 0])
ax_graf_prak = fig.add_subplot(gs[0, 1])
ax_ball_theory = fig.add_subplot(gs[1, 0])
ax_graf_theory = fig.add_subplot(gs[1, 1])
ax_graf_combo = fig.add_subplot(gs[2, :])


def make_spring_line(y_pos, coils=10, amp=0.08):
    z = np.linspace(0, y_pos, coils * 2)
    x = np.zeros_like(z)
    x[1::2] = amp
    x[::2] = -amp
    return x, z


(ball1,) = ax_ball_prak.plot([0], [ydata[0]], "o", markersize=7, color="blue")
(spring1_line,) = ax_ball_prak.plot(*make_spring_line(ydata[0]), color="gray", lw=1)
ax_ball_prak.set_xlim(-0.4, 0.4)
ax_ball_prak.set_ylim(min(ydata) - 5, max(ydata) + 5)
ax_ball_prak.set_title("Bola Praktikum + Pegas", fontsize=9)


(line_prak,) = ax_graf_prak.plot([], [], lw=1, color="blue")
ax_graf_prak.set_xlim(0, t[-1])
ax_graf_prak.set_ylim(min(ydata) - 5, max(ydata) + 5)
ax_graf_prak.set_title("Grafik Real-Time Praktikum", fontsize=9)

(ball2,) = ax_ball_theory.plot([0], [y_theory[0]], "o", markersize=7, color="red")
(spring2_line,) = ax_ball_theory.plot(
    *make_spring_line(y_theory[0]), color="gray", lw=1
)
ax_ball_theory.set_xlim(-0.4, 0.4)
ax_ball_theory.set_ylim(min(y_theory) - 5, max(y_theory) + 5)
ax_ball_theory.set_title("Bola Teori + Pegas", fontsize=9)

(line_theory,) = ax_graf_theory.plot([], [], lw=1, color="red")
ax_graf_theory.set_xlim(0, t[-1])
ax_graf_theory.set_ylim(min(y_theory) - 5, max(y_theory) + 5)
ax_graf_theory.set_title("Grafik Real-Time Teori", fontsize=9)

(line_combo_prak,) = ax_graf_combo.plot(
    [], [], "o", markersize=2, color="blue", label="Praktikum"
)
(line_combo_theory,) = ax_graf_combo.plot([], [], lw=1, color="red", label="Teori")
ax_graf_combo.set_xlim(0, t[-1])
ax_graf_combo.set_ylim(
    min(min(ydata), min(y_theory)) - 5, max(max(ydata), max(y_theory)) + 5
)
ax_graf_combo.set_title("Grafik Gabungan", fontsize=9)
ax_graf_combo.legend(fontsize=8)


def update(frame):
    x1, y1_spring = make_spring_line(ydata[frame])
    spring1_line.set_data(x1, y1_spring)
    ball1.set_data([0], [ydata[frame]])

    x2, y2_spring = make_spring_line(y_theory[frame])
    spring2_line.set_data(x2, y2_spring)
    ball2.set_data([0], [y_theory[frame]])

    line_prak.set_data(t[:frame], ydata[:frame])
    line_theory.set_data(t[:frame], y_theory[:frame])
    line_combo_prak.set_data(t[:frame], ydata[:frame])
    line_combo_theory.set_data(t[:frame], y_theory[:frame])

    return (
        ball1,
        spring1_line,
        line_prak,
        ball2,
        spring2_line,
        line_theory,
        line_combo_prak,
        line_combo_theory,
    )


plt.subplots_adjust(top=0.70, bottom=0.08, hspace=0.6)


ani = animation.FuncAnimation(fig, update, frames=len(t), interval=80, blit=True)

plt.show()
