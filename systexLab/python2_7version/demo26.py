r1 = range(0, 10)
print type(r1), r1, len(r1)

r2 = range(0, 10, 2)
print type(r2), r2, len(r2)
r3 = range(0, 10, 3)
print type(r3), r3, len(r3)
import math

r4 = range(0, int(5 * math.pi))
print r4

import numpy as np

r5 = np.arange(0, 10)
print type(r5), r5, len(r5)
print r1 + r1
print r5 + r5
r6 = np.arange(0, math.pi, 0.05)
print r6

r7 = np.linspace(0, 100)
print type(r7), len(r7), r7
r8 = np.linspace(0, 100, 51)
print type(r8), len(r8), r8
r9 = np.linspace(0, np.pi)
print type(r9), len(r9), r9
