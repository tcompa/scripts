import matplotlib.pyplot as plt


def f(x):
    return 0.0001 * x ** 2

fig, ax = plt.subplots(1, 1)

X = range(1000)
Y = map(f, X)
ax.plot(X, Y)

for x_lab, y_lab in [(0.2, 0.3), (0.5, 0.5), (0.6, 0.8)]:
    label = 'text at (%s,%s)' % (x_lab, y_lab)
    ax.text(x_lab, y_lab, label,
            transform=ax.transAxes, ha='center', va='center')
plt.show()
