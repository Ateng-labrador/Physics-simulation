import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

q = 1.0
m = 1.0
B = 0.8
dt = 0.02
n = 400


def setup_axis(axis):
    axis.set_xlim([-6, 6])
    axis.set_ylim([-6, 6])
    axis.aspect("equal")
    axis.tick_params(colors="white")
    axis.grid(True)
    return axis


if __name__ == "__main__":
    fig, axis = plt.subplots(figsize=(10, 10))
    axis.set_facecolor("black")
    fig.patch.set_facecolor("black")
