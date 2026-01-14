import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# mengunci urutan angka random
N = 100
frames = 240
dt = 0.05
times = np.arange(frames) * dt

# keadaan awal
r0 = np.random.uniform(-1,1,(N,2))

# besaran fisik setiap partikel
# np.random.uniform(star,finist,banyak)
# np.column_stack(())
# membuat matrik 1 dimesin menjadi 2 dimensi
s0 = np.random.uniform(0.2,1.8,size=N) # besar kecepatan
theta = np.random.uniform(0, 2*np.pi, size=N)
v0 = np.column_stack((s0 * np.cos(theta),s0 * np.sin(theta))) # menentukan arah
a_const = np.random.uniform(-0.2, 0.2, size=(N,2))

r = r0.copy()
v = v0.copy()

margin = 2.0
xmin = np.min(r0[:, 0]) - margin
xmax = np.max(r0[:,0]) + margin
ymin = np.min(r0[:,1]) - margin
ymax = np.max(r0[:,1]) + margin

r_det = np.zeros((frames, N, 2))
#ada N frame
#disetiap N
#masing masing punya 2 nilai
# matrik 3 dimensi
for i, t in enumerate(times):
    r_det[i] = r0 + v0 * t + 0.5 * a_const * t**2
    

fig, axis = plt.subplots()
scat = axis.scatter([],[])
axis.set_xlim(xmin, xmax)
axis.set_ylim(ymin, ymax)

restitution = 1.0

def animation(frame):
    global r, v
    v += a_const * dt

    r += v * dt

    # tumbukan pada x-min
    mask = r[:,0] < xmin
    if np.any(mask):
        r[mask,0] = xmin + (xmin - r[mask,0])
        v[mask,0] *= -restitution

    mask = r[:,0] > xmax
    if np.any(mask):
        r[mask,0] = xmax - (r[mask,0] - xmax)
        v[mask,0] *= -restitution

    mask = r[:,1] < ymin
    if np.any(mask):
        r[mask,1] = ymin + (ymin - r[mask,1])
        v[mask,1] *= -restitution

    mask = r[:,1] > ymax
    if np.any(mask):
        r[mask,1] = ymax - (r[mask,1] - ymax)
        v[mask,1] *= -restitution

    scat.set_offsets(r)
    return scat,

ani = FuncAnimation(
    fig=fig,
    func=animation,
    frames=240,
    interval=dt*1000
)

plt.show()

