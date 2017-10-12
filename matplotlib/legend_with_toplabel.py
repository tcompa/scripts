import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

def legend_with_toplabel(_ax, toplabel='', props={}):
    h, l = _ax.get_legend_handles_labels()
    extra = Rectangle((0, 0), 1, 1, fc='w', fill=False, edgecolor='none', linewidth=0)
    h = [extra] + h[:]
    l = [toplabel] + l[:]
    legend = _ax.legend(h, l, **props)


plt.plot([1, 2], [3, 4], label='1.2')
plt.plot([1, 2], [4, 3], label='2.4')

legend_with_toplabel(plt.gca(), 'top', props=dict(frameon=False))
plt.show()
