import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.patches import ConnectionPatch

m = 1
k = 1
d = 0.2

t = np.linspace(0,40,501)
w_d = np.sqrt((4*m*k - d**2)/(4*m**2))
x = np.exp(-d/(2*m)*t)*np.cos(w_d * t)


fig,axis = plt.subplots(1,2)

animated_mass, = axis[0].plot([],[],'-o',markersize=20,color='red')
animated_spring, = axis[0].plot([],[],color='blue')

axis[0].set_xlim([-2,2])
axis[0].set_ylim([-2,2])
axis[0].grid()

animated_func, = axis[1].plot([],[],color='blue')
axis[1].set_xlim([min(t),max(t)])
axis[1].set_ylim([-2,2])
axis[1].grid()



def update(frame):

    animated_spring.set_data([0,0],[2,x[frame]])
    animated_mass.set_data([0],[x[frame]])

    animated_spring.set_linewidth(int(abs(x[frame]-2)*2))

    animated_func.set_data(t[:frame],x[:frame])

    con = ConnectionPatch(
        xyA=(0,x[frame]),
        xyB=(t[frame],x[frame]),
        coordsA=axis[0].transData,
        coordsB=axis[1].transData,
        arrowstyle='-'
    )

    con.set_animated(True)
    axis[0].add_artist(con)

    return animated_mass,animated_spring,animated_func,con



animation = FuncAnimation(
    fig=fig,
    func=update,
    frames=len(t),
    interval=25,
    blit=True
)

plt.show()


    # updating the data across [frame]
    # animated_spring.set_data(spring_x,spring_y)
    # animated_spring.set_data([-2,x[frame]],[0,0])