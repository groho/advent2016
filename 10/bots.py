class Node:
    def __init__(self, bot, lo_type, lo, hi_type, hi):
        self.bot = bot
        self.lo_type = lo_type
        self.lo = lo
        self.hi_type = hi_type
        self.hi = hi
        self.chip0 = None
        self.chip1 = None
        print('Adding bot {} with lo {} and hi {}'.format(self.bot, self.lo, self.hi))

    def addChip(self, val):
        if (self.chip0 is None):
            self.chip0 = val
        elif (self.chip1 is None):
            self.chip1 = val
        else:
            print('Error adding {} to bot {} - already 2 chips ({} and {})'.format(val, self.bot, self.chip0, self.chip1))
            return

        # Propagate chips to bots
        if (self.chip0 is not None and self.chip1 is not None):
           
            if (self.chip0 > self.chip1):
                temp = self.chip0
                self.chip0 = self.chip1
                self.chip1 = temp

            if (self.chip0 == 17 and self.chip1 == 61):
                print('Part one answer - bot {} comparing chip-17 and chip-61'.format(self.bot))
                
            if (self.lo_type != 'output'):
                print('Bot {} giving bot {} -> chip {}'.format(self.bot, self.lo, self.chip0))
                nodes[self.lo].addChip(self.chip0)
            else:
                print('Bot {} giving output {} -> chip {}'.format(self.bot, self.lo, self.chip0))
                outputs[self.lo] = self.chip0
                
            if (self.hi_type != 'output'):
                print('Bot {} giving bot {} -> chip {}'.format(self.bot, self.hi, self.chip1))
                nodes[self.hi].addChip(self.chip1)
            else:
                print('Bot {} giving output {} -> chip {}'.format(self.bot, self.hi, self.chip1))
                outputs[self.hi] = self.chip1
                
nodes = 210 * [None]
outputs = 30 * [None]

import re
setup = re.compile('bot ([0-9]+) gives low to ([a-z]+) ([0-9]+) and high to ([a-z]+) ([0-9]+)')
add = re.compile('value ([0-9]+) goes to bot ([0-9]+)')

file = open('input.txt', 'r')
for line in file:
    line.rsplit(' \n')
   
    if (setup.search(line)):
        nodes[int(setup.search(line).group(1))] = Node(bot=int(setup.search(line).group(1)),
                                                  lo_type=setup.search(line).group(2),
                                                  lo=int(setup.search(line).group(3)),
                                                  hi_type=setup.search(line).group(4),
                                                  hi=int(setup.search(line).group(5)))

file.seek(0)

for line in file:
    line.rsplit(' \n')

    if (add.search(line)):
        nodes[int(add.search(line).group(2))].addChip(int(add.search(line).group(1)))

print('Part two answer - multiply {} * {} * {} = {}'.format(outputs[0], outputs[1], outputs[2], outputs[0]*outputs[1]*outputs[2]))
