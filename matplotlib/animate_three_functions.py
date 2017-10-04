import numpy
import matplotlib.pyplot as plt
import matplotlib.animation as animation


fig, ax = plt.subplots()
line1, = ax.plot([], [], lw=2, c='C0')
line2, = ax.plot([], [], lw=2, c='C1')
line3, = ax.plot([], [], lw=2, c='C2')
ax.set_xlim(0, 10)
ax.set_ylim(-2, 7)
ax.grid()
xdata, ydata = [], []


def update(step):
    x = numpy.linspace(0, 10)
    y1 = numpy.cos(x + step * 0.05)
    y2 = numpy.cos(x + step * 0.10) + 2.5
    y3 = numpy.cos(x + step * 0.15) + 5
    step += 1
    line1.set_data(x, y1)
    line2.set_data(x, y2)
    line3.set_data(x, y3)
    return line1, line2, line3


A = animation.FuncAnimation(fig, update, interval=50)
plt.show()
