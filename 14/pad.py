import re
import hashlib

three = re.compile(r'.*?(.)\1{2,}.*')
salt = 'ihaygndm'
#salt = 'yjdafjpo'

index = 0
seen = []
indices = []

while len(indices) < 64:

    seed = '{}{}'.format(salt, index).encode()
    digest = hashlib.md5(seed).hexdigest()

    # additional 2016 hashes for part b
    for i in range(2016):
        digest = hashlib.md5(digest.encode()).hexdigest()
        
    for i in range(len(seen)):
        pad = seen[i]
        if pad[3] > 1000:
            continue
        regex = r'.*?(' + pad[2] + r')\1{4,}.*'
        five = re.compile(regex)
        fives = five.search(digest)
        if fives:
            seen[i][3] = 1001
            indices.append(pad[0])
            #print('Found match for index={}'.format(pad[0]))
        else:
            seen[i][3] += 1
            
    threes = three.search(digest)
    if threes:
        repeat = threes.group(1)
        seen.append([index, digest, repeat, 0])
        
    index += 1
    
print('indices[63]={}'.format(sorted(indices)[63]))
    
