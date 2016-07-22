import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
from matplotlib.ticker import MaxNLocator
from matplotlib.ticker import AutoMinorLocator
from matplotlib.ticker import NullLocator
import numpy


fig, axs = plt.subplots(2, 2)
axs = axs.flatten()
x = numpy.linspace(0.0, 6.28, 100)
for a in axs:
    a.plot(x, numpy.sin(x))

axs[0].xaxis.set_major_locator(MultipleLocator(2.5))
axs[1].xaxis.set_major_locator(MaxNLocator(10))
axs[2].xaxis.set_minor_locator(AutoMinorLocator(4))
axs[3].xaxis.set_major_locator(NullLocator())


plt.tight_layout()
plt.show()
