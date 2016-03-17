'''
program: gridspec_with_mixed_2d_3d_subplots.py
author: tc
created: 2016-03-04 -- 18 CEST
'''

import numpy
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from mpl_toolkits.mplot3d import Axes3D

# generate some data to plot
N = 15
x = numpy.linspace(-0.5, 0.5, N)
y = x + 0.2 * (numpy.random.uniform(0.0, 1.0, N) - 0.5)
z = x + 0.2 * (numpy.random.uniform(0.0, 1.0, N) - 0.5)

# define the subplots grid, choose the axis
gs = gridspec.GridSpec(2, 3, width_ratios=[1, 2, 1], height_ratios=[1, 1])
ax_left_top = plt.subplot(gs[0, 0], projection='3d')
ax_left_bottom = plt.subplot(gs[1, 0])
ax_center = plt.subplot(gs[:, 1])
ax_right_bottom = plt.subplot(gs[1, 2])
ax_right_top = plt.subplot(gs[0, 2])

# set some options for the 3d subplot
ax_left_top.set_aspect(1)
ax_left_top.set_xlim3d(-1, 1)
ax_left_top.set_ylim3d(-1, 1)
ax_left_top.set_zlim3d(-1, 1)
ax_left_top.set_xticks([])
ax_left_top.set_yticks([])
ax_left_top.set_zticks([])

ax_left_bottom.set_aspect(1)
ax_right_bottom.set_aspect(1)
ax_right_top.set_aspect(1)
ax_center.set_aspect(1)

# plot data
ax_left_top.scatter(x, y, z)
ax_left_bottom.plot(x, y, 'ko-')
ax_center.plot(z, y, 'ko-')
ax_right_bottom.plot(y, x, 'ko-')
ax_right_top.plot(x, z, 'ko-')

plt.tight_layout()

plt.savefig('a.png', bbox_inches='tight')
plt.show()
