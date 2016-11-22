#!/usr/bin/env python

import itertools
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


plt.figure(figsize=(8.27, 11.69))
image = mpimg.imread('test_image.png')

Lx = 1.2
Ly = 1.6
Nx = 6
Ny = 8
eps = 1.0 / 20.0
dx = Lx / Nx
dy = Ly / Ny
for ix, iy in itertools.product(range(Nx), range(Ny)):
    left = (ix + eps) * dx
    right = (ix + 1 - eps) * dx
    bottom = (iy + eps) * dy
    top = (iy + 1 - eps) * dy
    plt.imshow(image, origin='upper', extent=[left, right, bottom, top])
plt.xlim(0, Lx)
plt.ylim(0, Ly)
plt.gca().axis('off')
plt.savefig('fig_a4.pdf')
