input = 3005290

# use binary trick where input = 2^a + l, and last_alive = 2l + 1
bin_input = bin(input)
bin_input = '{}{}'.format(bin_input[3:], bin_input[2])

print('Last alive (part 1): {0:d}'.format(int(bin_input,2)))
