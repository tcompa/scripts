import matplotlib.pyplot as plt


shift = iter(range(10))
for d in [(5, 1), (1, 5), (5, 10), (10, 5), (10, 10)]:
    y0 = shift.next()
    plt.plot([0, 1], [y0, y0 + 1], ls='--', lw=2, dashes=d, label='(%i, %i)' % (d[0], d[1]))

plt.xlim(0, 1)
plt.ylim(0, shift.next())
plt.legend(loc='best')
plt.show()
