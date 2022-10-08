import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
#plt.rcParams['text.usetex'] = True

# -------------- User Inputs --------------
R=42 # radius of orbit of sun
h=10 # sun height from ground
m=35 # x-offset of orbit of sun
n=35 # y-offset of orbit of sun
# -----------------------------------------

# Setup 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

theta = np.linspace(0, 2 * np.pi, 201)
x_sun = m+R*np.cos(theta)
y_sun = n+R*np.sin(theta)
z_sun = np.linspace(h,h,201)
ax.plot(x_sun,y_sun,z_sun)

# calculate shortest distance to sun as function of theta
theta_smin = np.pi + np.arctan2(n,m) # theta where shortest distance occurs
x_smin = m+R*np.cos(theta_smin)
y_smin = n+R*np.sin(theta_smin)
z_smin = h
ax.text(x_smin/2, y_smin/2, (z_smin/2)+0.6, "S", color='red')
ax.quiver(0, 0, 0, x_smin, y_smin, z_smin, arrow_length_ratio=0.04)
ax.quiver(x_smin, y_smin, 0, 0, 0, z_smin, arrow_length_ratio=0, linestyle='dashed')
ax.quiver(0, 0, 0, x_smin, y_smin, 0, arrow_length_ratio=0, linestyle='dashed')

# Plot display settings
ax.set_xlim([0, 10])
ax.set_ylim([0, 10])
ax.set_zlim([0, 10])
ax.set_xlabel('x', fontsize=15)
ax.set_ylabel('y', fontsize=15)
ax.set_zlabel('z', fontsize=15)

plt.show()