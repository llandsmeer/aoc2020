import time
import numpy as np
import itertools
from scipy.signal import convolve

STAMP = np.array([[1,1,1], [1,0,1], [1,1,1]])

lines = open('aoc11.in').read().splitlines()
floor = np.array(lines, dtype='c') == b'.'

x = np.zeros_like(floor, dtype=bool)
while True:
    nn = convolve(x, STAMP, mode='same')
    x, y = ~floor & ((~x & (nn==0)) | (x & (nn<4))), x
    if (x == y).all(): break
print(x.sum())

def nn2():
    nn = np.zeros_like(x, dtype=int)
    (I, J), D = x.shape, [-1, 0, 1]
    for i, j, di, dj in itertools.product(range(I), range(J), D, D):
        if floor[i,j] or (di == 0 and dj == 0):
            continue
        ii, jj = i + di, j + dj
        while 0 <= ii < I and 0 <= jj < J:
            if not floor[ii, jj]:
                nn[i,j] += x[ii, jj]
                break
            ii, jj = ii + di, jj + dj
    return nn

x = np.zeros_like(floor, dtype=bool)
while True:
    nn = nn2()
    x, y = ~floor & ((~x & (nn==0)) | (x & (nn<5))), x
    if (x == y).all(): break

print(x.sum())
