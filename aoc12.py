import math
import cmath
import collections
import functools

Ship = collections.namedtuple('Ship', 'pos dir')
lines = open('aoc12.in').read().splitlines()

def step(ship, line):
    return eval(f'lambda ship, x: ship._replace({ops[line[0]]})')(ship, int(line[1:]))

ops = {
    'N': 'pos=ship.pos+x*1j',
    'S': 'pos=ship.pos-x*1j',
    'E': 'pos=ship.pos+x',
    'W': 'pos=ship.pos-x',
    'L': 'dir=ship.dir*cmath.exp(math.radians(x)*1j)',
    'R': 'dir=ship.dir*cmath.exp(-math.radians(x)*1j)',
    'F': 'pos=ship.pos+ship.dir*x',
}
final = functools.reduce(step, lines, Ship(pos=0, dir=1))
print(round(abs(final.pos.real) + abs(final.pos.imag)))

ops.update({
    'N': 'dir=ship.dir+x*1j',
    'S': 'dir=ship.dir-x*1j',
    'E': 'dir=ship.dir+x',
    'W': 'dir=ship.dir-x',
})
final = functools.reduce(step, lines, Ship(pos=0, dir=10+1j))
print(round(abs(final.pos.real) + abs(final.pos.imag)))
