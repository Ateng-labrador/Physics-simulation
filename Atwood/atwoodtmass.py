# https://en.wikipedia.org/wiki/Swinging_Atwood%27s_machine
# upgrade code atwoodtwomass
# code ini tidak efisien
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


def parameter(
    mA: float = 6.0,
    mB: float = 2.0,
    g: float = 9.8,
    px: float = 0.0,
    py: float = 0.0,
    yA0: float = -1.0,
    xB0: float = -4.0,
) -> tuple:
    """
    Membuat parameter
    """
    a = (mA * g) / (mA + mB)
    L = (px - xB0) + (yA0 - py) + 5
    s = 0.5 * a
    return a, L, s, px, py


def step_frame(a: float, px: float = 0.0, xB0: float = -4.0) -> tuple:
    """
    Membuat frame
    """
    x_stop = px - 0.4
    max_s = x_stop - xB0
    dt = 0.03
    t_stop = np.sqrt(2 * max_s / a)
    frames = int(t_stop / dt)
    return x_stop, max_s, dt, t_stop, frames


def setup_plot(axis, px: float = 0.0, py: float = 0.0, R: float = 0.2):
    """
    Setup untuk plot
    """
    theta = np.linspace(0, 2 * np.pi, 200)
    (blockB,) = axis.plot([], [], lw=4, color="blue")
    (blockA,) = axis.plot([], [], lw=4, color="red")

    (rope_h,) = axis.plot([], [], color="saddlebrown", lw=3)
    (rope_v,) = axis.plot([], [], color="saddlebrown", lw=3)

    labelB = axis.text(0, 0, "", fontsize=14, color="blue", weight="bold")
    labelA = axis.text(0, 0, "", fontsize=14, color="red", weight="bold")

    axis.plot(px + R * np.cos(theta), py + R * np.sin(theta), color="black", lw=3)
    time_text = axis.text(0.02, 0.05, "", transform=axis.transAxes)
    return blockA, blockB, rope_h, rope_v, labelA, labelB, time_text


def setup_axis(axis):
    """
    Setup untuk axis
    """
    axis.set_xlim(-5, 1.5)
    axis.set_ylim(-5, 2)
    return axis


def update(
    i,
    dt,
    s,
    xB0,
    yA0,
    px,
    blockA,
    blockB,
    rope_h,
    rope_v,
    labelB,
    labelA,
    mA,
    mB,
    time_text,
):
    """
    Pembuatan frame to frame
    """
    t = i * dt
    s_new = s * t**2

    xB = xB0 + s_new
    yA = yA0 - s_new

    if xB >= px - 0.2:
        xB = px - 0.2
        yA = yA0 - ((xB - xB0))

    size = 0.25
    blockB.set_data(
        [xB - size, xB + size, xB + size, xB - size, xB - size],
        [0 - size, 0 - size, 0 + size, 0 + size, 0 - size],
    )

    blockA.set_data(
        [-size, +size, +size, -size, -size],
        [yA - size, yA - size, yA + size, yA + size, yA - size],
    )

    rope_h.set_data([xB + size, px], [0, 0])
    rope_v.set_data([px, 0], [0, yA + size])

    labelA.set_position((0.4, yA))
    labelA.set_text(f"m = {mA} kg")

    labelB.set_position((xB, 0.4))
    labelB.set_text(f"m = {mB} kg")
    time_text.set_text(f"t = {t:.2f} s")
    return blockB, blockA, rope_h, rope_v, labelB, labelA, time_text


if __name__ == "__main__":
    mA: float = 6.0
    mB: float = 2.0
    yA0: float = -1.0
    xB0: float = -4.0
    fig, axis = plt.subplots()
    axis.set_aspect("equal")
    axis.axis("off")
    a, L, s, px, py = parameter()
    axis = setup_axis(axis)
    x_stop, max_s, dt, t_stop, frames = step_frame(a, px, xB0)
    blockA, blockB, rope_v, rope_h, labelA, labelB, time_text = setup_plot(axis)

    def init():
        """
        Kondisi awal
        """
        blockA.set_data([], [])
        blockB.set_data([], [])
        rope_h.set_data([], [])
        rope_v.set_data([], [])
        labelA.set_text("")
        labelB.set_text("")
        time_text.set_text("")
        return blockA, blockB, rope_h, rope_v, labelA, labelB, time_text

    ani = FuncAnimation(
        fig=fig,
        func=update,
        fargs=(
            dt,
            s,
            xB0,
            yA0,
            px,
            blockA,
            blockB,
            rope_h,
            rope_v,
            labelB,
            labelA,
            mA,
            mB,
            time_text,
        ),
        init_func=init,
        frames=frames,
        blit=False,
        repeat=False,
    )

    plt.show()
