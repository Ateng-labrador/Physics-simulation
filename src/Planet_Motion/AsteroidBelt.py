# https://en.wikipedia.org/wiki/Asteroid
# Yasintia Auliasari physics UNY 24
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# SETUP FIGURE
fig, ax = plt.subplots(figsize=(6, 6))
fig.patch.set_facecolor('black')
ax.set_facecolor('black')
ax.axis('off')
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.set_aspect("equal")
ax.set_title("Animasi Asteroid Belt", color='white', pad=15, fontsize=15)

# MATAHARI
sun = ax.scatter(0, 0, s=300, c='yellow', label="Matahari")

# ASTEROID BELT
N = 450
a = np.random.uniform(4.5, 7.5, N)
e = np.random.uniform(0.0, 0.35, N)
b = a * np.sqrt(1 - e**2)

theta0 = np.random.uniform(0, 2*np.pi, N)
kepler_speed = 1 / a**3/2

colors = np.random.choice(['white', 'silver', 'gray'], N)

x = a * np.cos(theta0)
y = b * np.sin(theta0)
asteroids = ax.scatter(x, y, s=4, c=colors, label="Asteroid")

# PLANET MARS
a_mars = 3.0
theta_mars_0 = np.random.uniform(0, 2*np.pi)
speed_mars = 0.02
mars_dot = ax.scatter(a_mars*np.cos(theta_mars_0),
                      a_mars*np.sin(theta_mars_0),
                      s=80, c='red', label="Mars")

# PLANET JUPITER
a_jupiter = 8.0
theta_jupiter_0 = np.random.uniform(0, 2*np.pi)
speed_jupiter = 0.005
jupiter_dot = ax.scatter(a_jupiter*np.cos(theta_jupiter_0),
                         a_jupiter*np.sin(theta_jupiter_0),
                         s=150, c='orange', label="Jupiter")

# LEGEND
ax.legend(loc="upper left", facecolor="lightgray")

# UPDATE ANIMASI
def update(frame):
    # asteroids
    theta = theta0 + kepler_speed * frame
    x = a * np.cos(theta)
    y = b * np.sin(theta)
    asteroids.set_offsets(np.c_[x, y])

    # mars
    theta_m = theta_mars_0 + speed_mars * frame
    mars_dot.set_offsets([a_mars * np.cos(theta_m),
                          a_mars * np.sin(theta_m)])

    # jupiter
    theta_j = theta_jupiter_0 + speed_jupiter * frame
    jupiter_dot.set_offsets([a_jupiter * np.cos(theta_j),
                             a_jupiter * np.sin(theta_j)])

    return asteroids, mars_dot, jupiter_dot

# ANIMASI
ani = animation.FuncAnimation(fig, update, frames=1000, interval=20)

plt.show()
