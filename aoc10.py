import functools
import numpy as np

input = [int(x) for x in open('aoc10.in').read().splitlines()]
input = np.sort([0] + input + [max(input) + 3])

# A
deltas = np.diff(input)
print((deltas == 1).sum() * (deltas == 3).sum())

# B
@functools.lru_cache(maxsize=None)
def go(i=0):
    return 1 if i == len(input) - 1 else sum(
            go(j)
            for j in range(i+1, min(i+4, len(input)))
            if 1 <= input[j]-input[i] <= 3)


print(go())

