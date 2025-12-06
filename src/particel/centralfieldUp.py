import string
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


state = {
    'x' : 4.0,
    'y' : 0.0,
    'vx' : 0.0,
    'vy' : 1.4
}


trail_x = []
trail_y = []

def random_hex() -> str:
    """
    Fungsi untuk membuat warna
    """
    hex_value = "".join(
        np.random.choice(
            list(string.hexdigits),
            6
        )
    )
    return f"#{hex_value}"


def setup_axis(axis):
    axis.set_xlim(-8, 8)
    axis.set_ylim(-8, 8)
    axis.set_aspect("equal")
    axis.axis("off")
    return axis


def setup_plot(axis):
    particle = axis.scatter([], [], s=60, color=random_hex())
    track, = axis.plot([], [], color=random_hex(), linewidth=2)
    return particle, track


def update(i, particel, track):
    m = 1.0
    dt = 0.05
    k = 5.0
    r = np.sqrt(state['x']**2 + state['y']**2)
    Fx = -k * state['x'] / (r + 1e-6)
    Fy = -k * state['y'] / (r + 1e-6)

    state['vx'] += (Fx / m) * dt
    state['vy'] += (Fy / m) * dt
    state['x'] += state['vx'] * dt
    state['y'] += state['vy'] * dt

    trail_x.append(state['x'])
    trail_y.append(state['y'])
    
    particel.set_offsets([[state['x'], state['y']]])
    track.set_data(trail_x, trail_y)
    return (particel, track)


if __name__ == "__main__":
    fig, axis = plt.subplots(figsize=(7, 7))
    axis = setup_axis(axis)
    particel, track = setup_plot(axis)

    def init():
        particel.set_offsets(np.empty((0, 2)))
        track.set_data([], [])
        return (particel, track)

    ani = FuncAnimation(
        fig=fig,
        func=update,
        fargs=(particel, track),
        init_func=init,
        frames=1000,
        interval=20,
        blit=True
    )

    plt.show()