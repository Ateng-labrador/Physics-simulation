# Fairuz Athar S Physics UNY 24
# https://en.wikipedia.org/wiki/Fractal
import numpy as np
import matplotlib.pylab as plt
import matplotlib.animation as anim


def rotate_line(line: float, angle_deg: float, center=[0, 0]) -> float:
    """
    Equation Rotation
    """
    angle_rad = np.radians(angle_deg)
    p1_translated = [line[0][0] - center[0], line[0][1] - center[1]]
    p2_translated = [line[1][0] - center[0], line[1][1] - center[1]]

    rotated_p1_x = (center[0] + np.cos(angle_rad) *
                    p1_translated[0] - np.sin(angle_rad)
                    * p1_translated[1])
    rotated_p1_y = (center[1] + np.sin(angle_rad) *
                    p1_translated[0] + np.cos(angle_rad) *
                    p1_translated[1])
    rotated_p2_x = (center[0] + np.cos(angle_rad) *
                    p2_translated[0] - np.sin(angle_rad) *
                    p2_translated[1])
    rotated_p2_y = (center[1] + np.sin(angle_rad) *
                    p2_translated[0] + np.cos(angle_rad) *
                    p2_translated[1])

    return [[rotated_p1_x, rotated_p1_y], [rotated_p2_x, rotated_p2_y]]


# rotating point
def rotate_point(point: float, angle_deg: float, center=[0, 0]) -> float:
    """
    Rotation Point
    """
    angle_rad = np.radians(angle_deg)
    p_translated = [point[0] - center[0], point[1] - center[1]]

    rotated_x = (center[0] + np.cos(angle_rad) *
                 p_translated[0] - np.sin(angle_rad) *
                 p_translated[1])
    rotated_y = (center[1] + np.sin(angle_rad) *
                 p_translated[0] + np.cos(angle_rad) *
                 p_translated[1])

    return [rotated_x, rotated_y]

glow_layers = []
point_layers = []
border_layers = []

# animate section
def animate(frame):
    for i in range(10):
        # make x and y
        x, y = rotate_point(
            [-0.9 * np.sin(0.1 * frame + i * 0.31415), 0],
            i * 18
        )
        # neon efect
        glow_layers[i].set_data([x], [y])
        # Point
        point_layers[i].set_data([x], [y])
        # Circe border
        border_layers[i].set_data([x], [y])

    return glow_layers + point_layers + border_layers

if __name__ == "__main__":
    fig, ax = plt.subplots()
    fig.patch.set_facecolor('black')
    ax.axis("off")
    ax.patch.set_facecolor('black')
    ax.set_aspect('equal')

    plt.xlim(-1, 1)
    plt.ylim(-1, 1)
    # rotate
    for i in range(10):

        rotated_line = rotate_line([[-0.9, 0], [0.9, 0]], i * 18)

        # Background line
        ax.plot([rotated_line[0][0], rotated_line[1][0]],
                [rotated_line[0][1], rotated_line[1][1]],
                color='white', alpha=0.3, linewidth=2)

        # Core dot
        point, = ax.plot([], [], 'o', markersize=5, color='white')
        point_layers.append(point)
        # Outline of the circle

        border, = ax.plot([], [], 'o', markersize=20,
                        markerfacecolor='none', markeredgecolor='cyan',
                        markeredgewidth=1.5)
        border_layers.append(border)

        # Neon effect
        glow, = ax.plot([], [], 'o', markersize=17, color='cyan', alpha=0.25)
        glow_layers.append(glow)

    ani = anim.FuncAnimation(fig,
                            animate,
                            frames=1000,
                            interval=12,
                            blit=False)
    plt.show()
