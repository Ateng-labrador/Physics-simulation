import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def koch_snowflake(order, scale=10):
    
    def _koch_snowflake_complex(order):
        if order == 0:
            angles = np.array([0,120,240]) + 90
            return  scale / np.sqrt(3) * np.exp(np.deg2rad(angles) * 1j)
        else:
            zr = 0.5 - 0.5j * np.sqrt(3) / 3

            p1 = _koch_snowflake_complex(order - 1)
            p2 = np.roll(p1, shift=-1)
            dp = p2 - p1

            new_points = np.empty(len(p1) * 4, dtype=np.complex128)
            new_points[::4] = p1
            new_points[1::4] = p1 + dp / 3
            new_points[2::4] = p1 + dp * zr
            new_points[3::4] = p1 + dp / 3 * 2
            return new_points
    points = _koch_snowflake_complex(order)
    x,y = points.real, points.imag
    return x, y

# plt.fill() fungsi matplotlub yang digunakna untuk mengarsir
# megisi di bawah kurva dalam bentuk polygpn tertup
x,y = koch_snowflake(3)


fig,axis = plt.subplots()

margin = 1
axis.set_xlim([min(x) - margin,max(x) + margin])
axis.set_ylim([min(y) - margin,max(y) + margin])
axis.grid()
animated_plot, = axis.plot([],[])

def animation(frame):
    animated_plot.set_data(x[:frame],y[:frame])
    return animated_plot,

animation = FuncAnimation(
    fig=fig,
    func=animation,
    frames=len(y),
    interval=25
)

plt.show()



