with open('aoc9.in') as f:
    preamble = [int(next(f)) for i in range(25)]
    for line in f:
        z = int(line)
        if not any(x + y == z and x != y for x in preamble for y in preamble):
            print(z)
            break
        preamble.pop(0)
        preamble.append(z)

xs = list(map(int, open('aoc9.in')))

for i in range(len(xs)):
    j = 2
    while True:
        t = sum(xs[i:i+j])
        if t > z: break
        elif t == z:
            q = xs[i:i+j]
            print(min(q) + max(q))
        j += 1
