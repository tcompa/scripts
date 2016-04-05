'''
Program: broken_axis.py
Author: tc
Created: 2016-04-05 -- 10 CEST

Notes:
   1. I cannot use two different subplots, in my case.
   2. After calling add_line_and_break_axis(), yticks need to be set by
      hand.
   3. If minor yticks are set automatically (with AutoMinorLocator),
      they also show up where they should not.
'''

import sys

def add_line_and_break_axis(old_ax, new_x, new_y, eps=0.5, D=0, Draft=False):
    '''
    args:
      *old_ax* : Axis where previos data are already plotted.
      *new_x*  : x data to be plot on the new axis.
      *new_y*  : y data to be plot on the new axis.

    kwargs:
      *eps*    : Spacing between the two broken axis, between 0 (no
                 spacing) and 1 (spacing taking 1/3 of the y axis)
      *D*      : Margin to add when adding a white line on top of the
                 intersection between the two axis.
      *Draft*  : If True, keep the y-tick labels on the right, and
                 also show some lines separating the two axis.

    returns:
      *new_ax* : The secondary axis.
    '''

    # create and fill new axis
    new_ax = ax.twinx()
    new_ax.plot(new_x, new_y)

    # set ylim of the two axis
    old_ymin, old_ymax = old_ax.get_ylim()
    old_ax.set_ylim(old_ymin, old_ymax + (1 + eps) * (old_ymax - old_ymin))
    new_ymin, new_ymax = new_ax.get_ylim()
    new_ax.set_ylim(new_ymin - (1 + eps) * (new_ymax - new_ymin), new_ymax)
    if new_ymin <= old_ymax:
        sys.exit('[add_line_and_break_axis] ERROR:' +
                 ' the new axis should be above the old one.')

    # hide the y-axis line, for a given interval
    props_white = {'c': 'white', 'lw': 4, 'clip_on': False, 'zorder': 10}
    for x in old_ax.get_xlim():
        old_ax.plot([x, x],
                    [old_ymax + D, old_ymax + eps * (old_ymax - old_ymin) - D],
                    **props_white)
        new_ax.plot([x, x],
                    [new_ymin - eps * (new_ymax - new_ymin) + D, new_ymin - D],
                    **props_white)

    # move ylim of ax2 to the left
    if not Draft:
        new_ax.yaxis.set_ticks_position('left')

    # add lines
    if Draft:
        old_ax.axhline(old_ymax, c='k', ls='--', lw=2)
        old_ax.axhline(old_ymax + eps * (old_ymax - old_ymin), c='k', ls='--', lw=2)

    return new_ax


if __name__ == '__main__':

    import numpy
    import matplotlib.pyplot as plt

    numpy.random.seed(2212342587)
    x1 = numpy.linspace(0.0, 10.0, 100)
    y1 = numpy.random.normal(8.0, 10.0, size=x1.shape)
    x2 = numpy.linspace(5.0, 15.0, 100)
    y2 = numpy.random.normal(100.0, 20.0, size=x2.shape)

    fig, ax = plt.subplots(1, 1)
    ax.plot(x1, y1)
    eps = 0.2

    ax.set_yticks([-20, -10, 0, 10, 20, 30])

    ax2 = add_line_and_break_axis(ax, x2, y2, eps=eps, D=5, Draft=0)

    ax2.set_yticks([60, 90, 120, 150])

    plt.show()
