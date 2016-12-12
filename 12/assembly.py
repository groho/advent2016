import re

copy = re.compile('cpy ([abcd0-9]+) ([abcd0-9]+)')
inc = re.compile('inc ([abcd]+)')
dec = re.compile('dec ([abcd]+)')
jnz = re.compile('jnz ([0-9abcd]+) ([0-9\-]+)')

regs = 'abcd'

reg = {'a':0, 'b':0, 'c':1, 'd':0}
inst = []

file = open('input.txt', 'r')
for line in file:
    line.rsplit(' \n')
   
    match = copy.search(line)   
    if match: 
        if match.group(1) in regs:
            inst.append(['copy_reg', match.group(2), match.group(1)])
        else:
            inst.append(['copy_int', match.group(2), int(match.group(1))])

    match = inc.search(line)
    if (match):
        inst.append(['inc', match.group(1)])
    
    match = dec.search(line)
    if (match):
        inst.append(['dec', match.group(1)])

    match = jnz.search(line)
    if (match):
        if match.group(1) in regs:
            inst.append(['jnz_reg', match.group(1), int(match.group(2))])
        else:
            inst.append(['jnz_int', int(match.group(1)), int(match.group(2))])

ip = 0
while True:

    if ip >= len(inst): 
        break

    line = inst[ip]

    if line[0] == 'copy_reg':
        reg[line[1]] = reg[line[2]]
    elif line[0] == 'copy_int':
        reg[line[1]] = line[2]
    elif line[0] == 'inc':
        reg[line[1]] += 1
    elif line[0] == 'dec':
        reg[line[1]] -= 1
    elif line[0] == 'jnz_reg':
        if reg[line[1]] != 0:
            ip += line[2]
        else:
            ip += 1
        continue
    elif line[0] == 'jnz_int':
        if line[1] != 0:
            ip += line[2]
        else:
            ip+= 1
        continue

    ip += 1
            
print('a = {}'.format(reg['a']))
