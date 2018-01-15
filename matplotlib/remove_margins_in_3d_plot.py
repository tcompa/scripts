import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# from http://stackoverflow.com/a/16496436
# patch start
from mpl_toolkits.mplot3d.axis3d import Axis
if not hasattr(Axis, "_get_coord_info_old"):
    def _get_coord_info_new(self, renderer):
        tmp = self._get_coord_info_old(renderer)
        mins, maxs, centers, deltas, tc, highs = tmp[:]
        mins += deltas / 4
        maxs -= deltas / 4
        return mins, maxs, centers, deltas, tc, highs
    Axis._get_coord_info_old = Axis._get_coord_info
    Axis._get_coord_info = _get_coord_info_new
# patch end


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.plot([0, 0, 1, 3, 2, 3],
        [3, 0, 4, 2, 3, 1],
        [1, 3, 4, 2, 1, 3],
        lw=2, c='k')

ax.set_xlim3d(0, 4)
ax.set_ylim3d(0, 4)
ax.set_zlim3d(0, 4)
plt.show()
