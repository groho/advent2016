from collections import deque
from copy import deepcopy
from time import time

# define lowercase as microchip, uppercase as generator, 'X' as elevator
floor1 = ['X','s','S','p','P','d','D','e','E']
floor2 = ['T','r','R','c','C']
floor3 = ['t']
floor4 = []

chips = 'cdeprst'
generators = 'CDEPRST'

floors = [floor1, floor2, floor3, floor4]
moves = 0
initial_state = [floors, moves]

# keep track of visited states as sorted strings in dictionary
seen = {}

# final goal is everything on floor4
goal = '///CDEPRSTXcdeprst/'

# checks whether a state is valid based on generator/microchip rules
def is_valid(state):
    floors = state[0]
    moves = state[1]

    for floor in floors:
        for chip in chips:
            if chip in floor:
                if chip.upper() in floor:
                    continue
                else:
                    for generator in generators:
                        if generator in floor and generator != chip.upper():
                            return False

    return True

# checks whether this is a unique and valid state, and if so, adds it to seen dict    
def is_new(state):
    floors = state[0]
    moves = state[1]

    # flatten current state into string representation for easy dict lookup
    string = ""
    for floor in floors:
        floor.sort()
        string = string + "".join(floor) + "/"
        
    if string == goal:
        print('Reached goal after {} moves'.format(moves))
        quit()
    elif string in seen:
        return False
    elif is_valid(state):
        seen[string] = moves
        return True

# generate moves and add them to BFS queue if they are new    
def gen_moves(queue):
    state = queue.popleft()
    floors = state[0]
    moves = state[1]

    # for each item on the floor that currently has the elevator,
    # generate 4 new states (all of which may not be new and/or valid):
    ## a: move 1 item up
    ## b: move 2 items up
    ## c: move 1 item down
    ## d: move 2 items down

    for i in range(len(floors)):
        if 'X' in floors[i]:
            for j in range(len(floors[i])):

                if (floors[i][j] == 'X'):
                    continue

                # only move up if not at top floor
                if (i != 3):
                
                    # a: move 1 item up
                    state_up1 = deepcopy(state)
                    state_up1[0][i].remove(floors[i][j])
                    state_up1[0][i+1].append(floors[i][j])
                    state_up1[0][i].remove('X')
                    state_up1[0][i+1].append('X')
                    state_up1[1] += 1

                    #print('New state_up1: {}'.format(state_up1))
                    if (is_new(state_up1)):
                        #print('Adding state up1')
                        queue.append(state_up1)

                    for k in range(len(floors[i])):
                        if (k != j and floors[i][k] != 'X'):
                            state_up2 = deepcopy(state_up1)
                            state_up2[0][i].remove(floors[i][k])
                            state_up2[0][i+1].append(floors[i][k])

                            #print('New state_up2: {}'.format(state_up2))
                            if (is_new(state_up2)):
                                #print('Adding state up2')
                                queue.append(state_up2)

                            
                # only move down if not on bottom floor
                if (i != 0):

                    # c: move 1 item down
                    state_down1 = deepcopy(state)
                    state_down1[0][i].remove(floors[i][j])
                    state_down1[0][i-1].append(floors[i][j])
                    state_down1[0][i].remove('X')
                    state_down1[0][i-1].append('X')
                    state_down1[1] += 1

                    #print('New state_down1: {}'.format(state_down1))
                    if (is_new(state_down1)):
                        #print('Adding state down1')
                        queue.append(state_down1)

                    for k in range(len(floors[i])):
                        if (k != j and floors[i][k] != 'X'):
                            state_down2 = deepcopy(state_down1)
                            state_down2[0][i].remove(floors[i][k])
                            state_down2[0][i-1].append(floors[i][k])

                            #print('New state_down2: {}'.format(state_down2))
                            if (is_new(state_down2)):
                                #print('Adding state down2')
                                queue.append(state_down2)

                                
                    
# add initial state to queue and seen                    
def init(initial_state):
    if (is_new(initial_state)):
        queue.append(initial_state)
    else:
        print('Error with initial state - exiting!')
        quit()

print('Starting...')
start = time()
queue = deque([])
iter = 0
init(initial_state)
while queue:
    gen_moves(queue)
    iter += 1
    if (iter % 1000) == 0:
        print('Iteration = {} / Nodes = {} / Time elapsed = {}s'.format(iter, len(queue), time() - start))
        print('Next State / Length = [ {} {} {} {} ] / Moves = {}'.format(len(queue[0][0][0]),len(queue[0][0][1]),len(queue[0][0][2]),len(queue[0][0][3]),queue[0][1]))

    
