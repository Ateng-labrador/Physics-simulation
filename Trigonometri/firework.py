# etna triyanti Pyhsics UNY 24
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig = plt.figure(figsize=(6, 6))
ax = plt.axes(xlim=(-1.5, 1.5), ylim=(0, 2.5))


fig.patch.set_facecolor("black")
ax.set_facecolor("black")


N_FIREWORKS = 3

main_colors = [
    "#ff0000", "#ff7300","#ffe600", "#33ff00", "#00eaff", "#0095ff",  "#ae00ff",
    "#ff00d4"   ]

tail_colors = ["#ff0000", "#ff7300","#ffe600", "#33ff00", "#00eaff", "#0095ff",  "#ae00ff",
    "#ff00d4"   ]

fireworks = []
start_times = [10, 45, 90]


for i in range(N_FIREWORKS):

    center = np.array([
        np.random.uniform(-1.0, 1.0),
        np.random.uniform(1.0, 2.4)
    ])

    n_main = np.random.randint(35, 55)
    n_tails = np.random.randint(12, 18)

    ang_main = np.linspace(0, 2*np.pi, n_main)
    np.random.shuffle(ang_main)

    ang_tail = np.linspace(-np.pi/2 - 0.6, -np.pi/2 + 0.6, n_tails)

    speed_main = np.random.uniform(0.01, 0.03, n_main)
    speed_tail = np.random.uniform(0.015, 0.03, n_tails)

    color_main = np.random.choice(main_colors, n_main)
    color_tail = np.random.choice(tail_colors, n_tails)

    L_main = []
    for _ in range(n_main):
        line, = ax.plot([], [], lw=2.3, alpha=1)
        L_main.append(line)

    L_tail = []
    for _ in range(n_tails):
        line, = ax.plot([], [], lw=1.8, alpha=1)
        L_tail.append(line)

    fireworks.append({
        "center": center,
        "ang_main": ang_main,
        "ang_tail": ang_tail,
        "speed_main": speed_main,
        "speed_tail": speed_tail,
        "color_main": color_main,
        "color_tail": color_tail,
        "L_main": L_main,
        "L_tail": L_tail,
        "start": start_times[i]
    })


def update(frame):

    for fw in fireworks:

        if frame < fw["start"]:
            continue

        f = frame - fw["start"]

        cx, cy = fw["center"]
        ang_m = fw["ang_main"]
        ang_t = fw["ang_tail"]
        spd_m = fw["speed_main"]
        spd_t = fw["speed_tail"]
        col_m = fw["color_main"]
        col_t = fw["color_tail"]

        # MAIN STREAKS
        for i, line in enumerate(fw["L_main"]):

            length = f * spd_m[i]

            x2 = cx + np.cos(ang_m[i]) * length
            y2 = cy + np.sin(ang_m[i]) * length

            line.set_data([cx, x2], [cy, y2])
            line.set_color(col_m[i])

            if f > 60:
                alpha = max(0, 1 - (f - 60) / 40)
                line.set_alpha(alpha)

        # FALLING SPARK TAILS
        for j, line in enumerate(fw["L_tail"]):

            length = f * spd_t[j]

            x2 = cx + np.cos(ang_t[j]) * (length * 0.5)
            y2 = cy + np.sin(ang_t[j]) * (length * 1.3)

            line.set_data([cx, x2], [cy, y2])
            line.set_color(col_t[j])

            if f > 55:
                alpha = max(0, 1 - (f - 55) / 35)
                line.set_alpha(alpha)

    lines = []
    for fw in fireworks:
        lines.extend(fw["L_main"])
        lines.extend(fw["L_tail"])
    return lines


ani = FuncAnimation(fig, update, frames=150, interval=30, blit=True)

plt.show()
