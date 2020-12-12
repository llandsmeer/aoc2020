import functools

print(sum(
    len(set(group.replace('\n','')))
    for group in open('./aoc6.in').read().split('\n\n')
    ))

print(sum(
    len(functools.reduce(lambda a, b: set(a) & set(b), group))
    for group in map(str.splitlines, open('./aoc6.in').read().split('\n\n'))
    ))


