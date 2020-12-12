import re

# initialize correct password counts to 0
counts1 = counts2 = 0

for line in open('aoc2.in'):
    # match with regex to extract relevant parts
    m = re.match(r'(\d+)-(\d+) ([a-z]): ([a-z]+)', line)
    assert m

    # extract the 4 regex groups (...)
    l, r, char, passwd = m.groups()

    # convert to int
    left = int(l)
    right = int(r)

    # check requirements
    counts1 += left <= passwd.count(char) <= right
    counts2 += (char == passwd[left-1]) ^ (char == passwd[right-1])

print(counts1, counts2)

