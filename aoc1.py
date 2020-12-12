# Challenge 1 O(n)

seen = set()

with open('./aoc1.in') as f:
    for line in f:
        x = int(line)
        if 2020 - x in seen:
            print(x * (2020 - x))
        seen.add(x)

# Challenge 2 O(n^2)

seen = set()

with open('./aoc1.in') as f:
    for line in f:
        x = int(line)
        for i in range(2020-x):
            if i in seen and (2020-x)-i in seen:
                print(x * i * (2020 - x - i))
        seen.add(x)
