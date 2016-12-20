
file = open('input.txt', 'r')

ranges = []
for line in file:
    line.rsplit('\n')
    (low, high) = line.split('-')
    ranges.append((int(low),int(high)))
    ranges = sorted(ranges, key=lambda ranges: ranges[0])

pos = 0
gaps = 0
for item in ranges:
    (low, high) = item;

    if pos >= low and pos < high:
        pos = high
    elif pos+1 == low:
        pos = high
    elif pos > low and pos > high:
        continue
    elif pos+1 < low:
        print('Gap at {}'.format(pos+1))
        gaps += low - (pos + 1)
        pos = high

gaps += 4294967295 - pos
print('Total gaps = {}'.format(gaps))
