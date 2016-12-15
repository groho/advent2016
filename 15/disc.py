
# [ # of disc, positions, start position ]
discs = []

# process input file into dictionary
file = open('input.txt', 'r')
for line in file:
    words = line.split()
    words[11] = words[11][:-1] # strip trailing period

    discs.append([int(words[1][1:]), int(words[3]), int(words[11])])
   
time = 0
while True:
    closed = 0
    for disc in discs:
        closed |= (disc[0] + disc[2] + time) % disc[1]

    if closed:
        time += 1
    else:
        break

print('Found time = {}'.format(time))
