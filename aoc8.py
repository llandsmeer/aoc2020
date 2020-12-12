from typing import Set

program = []

with open('aoc8.in') as f:
    for line in f:
        op, raw_arg = line.split()
        program.append((op, int(raw_arg)))

def run(program):
    ip = 0
    acc = 0
    seen: Set[int] = set()
    while True:
        if ip == len(program):
            return True, acc
        op, arg = program[ip]
        if ip in seen:
            return False, acc
        seen.add(ip)
        if op == 'acc':
            acc += arg
            ip += 1
        elif op == 'jmp':
            ip += arg
        elif op == 'nop':
            ip += 1

for i, (op, arg) in enumerate(program):
    orig = op, arg
    if op == 'jmp':
        program[i] = 'nop', arg
    elif op == 'nop':
        program[i] = 'jmp', arg
    else:
        continue
    halts, acc = run(program)
    if halts:
        print(acc)
    program[i] = orig
