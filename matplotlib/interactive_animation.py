'''
program: interactive_animation.py
created: 2016-06-03 -- 17 CEST
authors: tc, dc
'''

import numpy
import matplotlib.pyplot as plt


plt.ion()
fig = plt.figure()
ax = plt.gca()
line, = plt.plot([], [])

for i in xrange(1000):
    # calculations
    x = numpy.arange(0.0, i * 2.0 * numpy.pi / 100.0, 2.0 * numpy.pi / 100.0)
    y = numpy.cos(x) * numpy.exp(-0.1*x)
    # plotting
    line.set_data(x, y)
    ax.autoscale_view()
    ax.relim()
    plt.draw()
    plt.pause(0.01)
