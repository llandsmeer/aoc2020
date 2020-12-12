import numpy as np

data = np.array(list(open('aoc5.in')), dtype='c').astype('U').T[-2::-1,:]


row = 2**np.arange(7) @ (data[3:] == 'B')
col = 2**np.arange(3) @ (data[:3] == 'R')

seat = np.sort(row*8 + col)
idx = np.where(np.diff(seat) == 2)
print(seat.max(), seat[idx] + 1)
