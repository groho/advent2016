import re

copy = re.compile('cpy ([abcd0-9]+) ([abcd0-9]+)')
inc = re.compile('inc ([abcd]+)')
dec = re.compile('dec ([abcd]+)')
jnz = re.compile('jnz ([0-9abcd]+) ([0-9\-]+)')

regs = 'abcd'

reg = {'a':0, 'b':0, 'c':0, 'd':0}
inst = []

file = open('input.txt', 'r')
for line in file:
    line.rsplit(' \n')
    inst.append(line)

ip = 0
while True:
    line = inst[ip]
    print('ip={}, inst={}'.format(ip, inst[ip]))
    match = copy.search(line)   
    if match: 
        if match.group(1) in regs:
            reg[match.group(2)] = reg[match.group(1)]
        else:
            reg[match.group(2)] = int(match.group(1))
        ip += 1
        continue

    match = inc.search(line)
    if (match):
        reg[match.group(1)] += 1
        ip += 1
        continue
    
    match = dec.search(line)
    if (match):
        reg[match.group(1)] -= 1
        ip += 1
        continue

    match = jnz.search(line)
    if (match):
        if match.group(1) in regs:
            if reg[match.group(1)] != 0:
                ip += int(match.group(2))
            else:
                ip += 1
            continue
        else:
            if match.group(1) != 0:
                ip += int(match.group(2))
            else:
                ip += 1
            continue
          
print('a = {}'.format(reg[a]))