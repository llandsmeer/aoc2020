import numpy as np

lines = open('aoc3.in').read().splitlines()
trees = (np.array(lines, dtype='c') == b'#').astype(int)
nrows, ncols = trees.shape

product = 1
for right, down in zip([1,3,5,7,1], [1,1,1,1,2]):
    steps = np.arange(nrows//down)
    ntrees = trees[steps*down, steps*right % ncols].sum()
    print(f'right {right} down {down} trees {ntrees}')
    product *= ntrees

print(f'product: {product}')

