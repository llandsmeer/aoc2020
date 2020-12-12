def assemble(program):
    import struct
    import ctypes
    import mmap

    buf = mmap.mmap(-1, 100*mmap.PAGESIZE, prot=mmap.PROT_READ | mmap.PROT_WRITE | mmap.PROT_EXEC)

    ftype = ctypes.CFUNCTYPE(ctypes.c_int)
    fpointer = ctypes.c_void_p.from_buffer(buf)

    f = ftype(ctypes.addressof(fpointer))

    buf.write(b'\x48\x31\xc0') # xor rax, rax

    labels = {}
    for ip, (op, arg) in enumerate(program):
        if op == 'jmp':
            labels[ip+arg] = None

    jmps = {}
    for ip, (op, arg) in enumerate(program):
        if ip in labels:
            labels[ip] = buf.tell()
        if op == 'acc':
            cmd = b'\x48\x05' + struct.pack('i', arg)
        elif op == 'jmp':
            cmd = b'\xe9\0\0\0\0'
            jmps[ip+arg] = buf.tell()
        elif op == 'nop':
            cmd = b'\x90'
        buf.write(cmd)
    eob = buf.tell()

    for target in jmps:
        if labels[target] is None:
            labels[target] = eob
        d = struct.pack('i', labels[target] - jmps[target] - 5)
        assert buf[jmps[target]+1:jmps[target]+5] == b'\x00\x00\x00\x00'
        buf[jmps[target]+1:jmps[target]+5] = d

    buf.write(b'\xc3')

    r = f()
    print('//', r)

    del fpointer
    buf.close()


def state_diagram(program):
    import collections

    # build graph
    fwd = {}
    bwd = collections.defaultdict(list)
    for ip, (op, arg) in enumerate(program):
        next = ip + (arg if op == 'jmp' else 1)
        fwd[ip] = next
        bwd[next].append(ip)

    # calculate halting states
    queue = [len(program)]
    halt = set()
    while queue:
        x = queue.pop()
        if x not in halt:
            queue.extend(bwd[x])
        halt.add(x)

    # calculate loop state & needed change
    loop = set()
    ip = 0
    while ip not in loop:
        op, arg = program[ip]
        if op == 'jmp' and ip+1 in halt:
            mod = ip, ip+1, 'nop'
        elif op == 'nop' and ip+arg in halt:
            mod = ip, ip+arg, 'jmp'
        loop.add(ip)
        ip = fwd[ip]

    print('digraph Q {')
    for i in range(len(program)+1):
        label = f'{program[i][0]} {program[i][1]}' if i < len(program) else 'HALT'
        if i in loop:
            print('   ', i, f'[style=bold,label="{label}"]')
        elif i in halt:
            print('   ', i, f'[label="{label}"]')
        else:
            print('   ', i, f'[style=dotted,label="{label}"]')
    for k, v in fwd.items():
        print('   ', k, '->', v)
    print('   ', mod[0], '->', mod[1], '[style=dashed,color=red]')
    print('}')

    return mod


program = []

with open('aoc8.in') as f:
    for line in f:
        op, raw_arg = line.split()
        program.append((op, int(raw_arg)))

mod = state_diagram(program)
program[mod[0]] = mod[2], program[mod[0]][1]
assemble(program)
