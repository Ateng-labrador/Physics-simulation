# zahwa irwan Physics UNY 24
import matplotlib.pyplot as plt
import matplotlib.animation as animation


fig, ax = plt.subplots(figsize=(5, 5))
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.set_aspect("equal")

(ball,) = ax.plot([], [], "o", markersize=20)


state = {"x": 2.0, "y": 5.0, "vx": 0.1, "vy": 0.07}


def init():
    ball.set_data([], [])
    return (ball,)


def update(frame):
    state["x"] += state["vx"]
    state["y"] += state["vy"]

    if state["x"] <= 0 or state["x"] >= 10:
        state["vx"] = -state["vx"]

    if state["y"] <= 0 or state["y"] >= 10:
        state["vy"] = -state["vy"]

    ball.set_data([state["x"]], [state["y"]])
    return (ball,)


ani = animation.FuncAnimation(
    fig, update, frames=200, init_func=init, blit=True, interval=20
)

plt.show()
