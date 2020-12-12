passwds = open('aoc4.in').read().split('\n\n')

fs = 'byr iyr eyr hgt hcl ecl pid'.split()

valid = 0

for p in passwds:
    p = p.replace('\n', ' ').split()
    ok = 1
    seen = set(fs)
    for part in p:
        a, b = part.split(':')
        if a in seen:
            seen.remove(a)
        if a == 'hgt':
            if b.endswith('cm'):
                check = 150 <= int(b[:-2]) <= 193
            elif b.endswith('in'):
                check = 59 <= int(b[:-2]) <= 76
            else:
                check = False
        if a == 'byr':
            check = b.isdigit() and int(b) >= 1920 and int(b) <= 2002
        if a == 'iyr':
            check = b.isdigit() and int(b) >= 2010 and int(b) <= 2020
        if a == 'eyr':
            check = b.isdigit() and int(b) >= 2020 and int(b) <= 2030
        if a == 'hcl':
            check = b[0] == '#' and len(b) == 7 and all(x in '0123456789abcdef' for x in b[1:])
        if a == 'ecl':
            check = b in 'amb blu brn gry grn hzl oth'.split()
        if a == 'pid':
            check = b.isdigit() and len(b) == 9
        if a == 'cid':
            check = True
        if not check:
            ok = 0
    valid += ok and not seen



print(valid)
