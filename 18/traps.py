input = '.^^..^...^..^^.^^^.^^^.^^^^^^.^.^^^^.^^.^^^^^^.^...^......^...^^^..^^^.....^^^^^^^^^....^^...^^^^..^'
input_len = len(input)

rows_a = 40
rows_b = 400000
cols = input_len+2

maze_a = [[0 for x in range(rows_a)] for y in range(cols)]
maze_b = [[0 for x in range(rows_b)] for y in range(cols)]

# create maze with 'safe' left/right border to allow
# for ignoring special edge checks for out of bounds
def init_maze(maze, rows, cols, input):

    first = list(input)
    for x in range(1, cols-1):
        maze[x][0] = first[x-1]
        
    for y in range(rows):
        for x in range(cols):
            if x==0 or x==input_len+1:
                maze[x][y] = '.'

def populate_traps(maze, rows, cols):
    for y in range(1, rows):
        for x in range(1, cols-1):
            if maze[x-1][y-1] != maze[x+1][y-1]:
                maze[x][y] = '^'
            else:
                maze[x][y] = '.'
                
def print_maze(maze, rows, cols):
    for y in range(rows):
        for x in range(cols):
            print('{}'.format(maze[x][y]),end='')
        print('')

def count_safe(maze, rows, cols):
    count = 0
    for y in range(rows):
        for x in range(1, cols-1):
            if maze[x][y]=='.':
                count += 1

    return count
        
init_maze(maze_a, rows_a, cols, input)
populate_traps(maze_a, rows_a, cols)
#print_maze(maze, rows, cols)
print('Safe A: {}'.format(count_safe(maze_a, rows_a, cols)))

init_maze(maze_b, rows_b, cols, input)
populate_traps(maze_b, rows_b, cols)
#print_maze(maze, rows, cols)
print('Safe B: {}'.format(count_safe(maze_b, rows_b, cols)))
