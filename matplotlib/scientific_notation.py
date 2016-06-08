'''
program: scientific_notation.py
created: 2016-06-08 -- 19 CEST
author:  tc
'''

import matplotlib.pyplot as plt


plt.plot([0, 1, 2], [1e-5, 2e-5, 7e-5])
plt.ticklabel_format(style='sci', axis='y', scilimits=(0, 0))
plt.show()
