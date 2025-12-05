# Upgrade code from bouncingball
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


state = {
    'x': 2.0,
    'y': 5.0,
    'vx': 0.1,
    'vy': 0.07
}


def setup_axis(axis):
    axis.set_xlim(0, 10)
    axis.set_ylim(0, 10)
    axis.set_aspect('equal')
    return axis


def setup_plot(axis):
    ball, = axis.plot([], [], 'o', markersize=20)
    return ball


def update(frame, ball):
    state['x'] += state['vx']
    state['y'] += state['vy']

    if state['x'] <= 0 or state['x'] >= 10:
        state['vx'] = -state['vx']

    if state['y'] <= 0 or state['y'] >= 10:
        state['vy'] = -state['vy']

    ball.set_data([state['x']], [state['y']])
    return (ball,)

if __name__ == "__main__":
    fig, axis = plt.subplots(figsize=(5, 5))
    ball = setup_plot(axis)
    axis = setup_axis(axis)

    def init():
        ball.set_data([], [])
        return (ball,)

    ani = FuncAnimation(
        fig=fig,
        func=update,
        init_func=init,
        fargs=(ball,),
        blit=True,
        interval=20
    )

    plt.show()
