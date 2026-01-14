# Neni Sabrina Saekoko physics UNY 24
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

m = 0.05
r = 0.03
omega = 50.0
g = 9.8
theta0 = 1.0

Inersia = 0.5 * m * r**2
L = Inersia * omega

Omega_p = (m * g * r * np.sin(theta0)) / L


def generate_top_geometry():
    theta_circle = np.linspace(0, 2*np.pi, 30)
    x_circle = r * np.cos(theta_circle)
    y_circle = r * np.sin(theta_circle)
    z_circle = np.zeros_like(x_circle) + (r)

    x_line = [0, 0]
    y_line = [0, 0]
    z_line = [0, r * 2]
    return x_circle, y_circle, z_circle, x_line, y_line, z_line


def rotate_coordinates(x, y, z, angle_spin, angle_tilt, angle_precess):
    x1 = x * np.cos(angle_spin) - y * np.sin(angle_spin)
    y1 = x * np.sin(angle_spin) + y * np.cos(angle_spin)
    z1 = z

    x2 = x1 * np.cos(angle_tilt) + z1 * np.sin(angle_tilt)
    y2 = y1
    z2 = -x1 * np.sin(angle_tilt) + z1 * np.cos(angle_tilt)

    x3 = x2 * np.cos(angle_precess) - y2 * np.sin(angle_precess)
    y3 = x2 * np.sin(angle_precess) + y2 * np.cos(angle_precess)
    z3 = z2

    return x3, y3, z3


fig = plt.figure(figsize=(6, 6))
ax = fig.add_subplot(111, projection='3d')

ax.set_xlim(-0.1, 0.1)
ax.set_ylim(-0.1, 0.1)
ax.set_zlim(0, 0.15)
ax.set_title("Simulasi Gasing")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")


line_body, = ax.plot([], [], [], 'b-', lw=2)
line_disk, = ax.plot([], [], [], 'r-', lw=3)
point_tip, = ax.plot([], [], [], 'ko')


xc_raw, yc_raw, zc_raw, xl_raw, yl_raw, zl_raw = generate_top_geometry()


dt = 0.05
total_frames = 200


def update(frame):
    t = frame * dt

    current_spin = omega * t
    current_precess = Omega_p * t

    xc, yc, zc = rotate_coordinates(xc_raw, yc_raw, zc_raw,
                                    current_spin, theta0, current_precess)
    xl, yl, zl = rotate_coordinates(np.array(xl_raw), np.array(yl_raw),
                                    np.array(zl_raw), current_spin, theta0,
                                    current_precess)

    line_disk.set_data(xc, yc)
    line_disk.set_3d_properties(zc)

    line_body.set_data(xl, yl)
    line_body.set_3d_properties(zl)

    point_tip.set_data([0], [0])
    point_tip.set_3d_properties([0])

    return line_disk, line_body, point_tip


anim = FuncAnimation(fig, update, frames=total_frames, interval=40, blit=True)

plt.show()
