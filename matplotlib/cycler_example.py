import matplotlib.pyplot as plt
from cycler import cycler

# create one cycler
cycle_color = cycler('color', ['b', 'm', 'c', 'orange'])
assert len(cycle_color) == 4

# create two cyclers and combine them with "+"
cycle_marker = cycler('marker', ['o', 'x']) + cycler('s', [30, 200])
assert len(cycle_marker) == 2

# combine two cyclers with "*"
styles = cycle_marker * cycle_color
assert len(styles) == len(cycle_marker) * len(cycle_color)

styles = iter(styles)
x = range(10)
for i in xrange(8):
    y = range(2 * i, 10 + 2 * i)
    plt.scatter(x, y, **styles.next())
plt.show()
