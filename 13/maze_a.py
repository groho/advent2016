from collections import deque

number = 1362

rows = 50
cols = 50
start = (1,1)
end = (31,39)

maze = [[0 for x in range(cols)] for y in range(rows)]

# create maze for quick neighbor lookup
def init_maze(maze, rows, cols):
    for x in range(rows):
        for y in range(cols):
            item_sum = x*x + 3*x + 2*x*y + y + y*y + number
            bin_sym = 0
            for digit in str(bin(item_sum))[2:]:
                bin_sym += int(digit)
            maze[x][y] = bin_sym % 2

def print_maze(maze, rows, cols, start, end, paths):

    length = 0
    path = end
    while path in paths:
        path = paths[path]
        if path == None:
            break
        maze[path[0]][path[1]] = 2
        length += 1
    
    for y in range(cols):
        for x in range(rows):
            if x==start[0] and y==start[1]:
                print("S", end="")
            elif x==end[0] and y==end[1]:
                print("E", end="")
            else:
                printer = {0: ' ',
                           1: '#',
                           2: '*',}
                print("{}".format(printer[maze[x][y]]), end="")
        print("")

    print("Path length = {}".format(length))

def path_length(start, end, paths):
    length = 0
    path = end
    while path in paths:
        path = paths[path]
        if path == None:
            break
        length += 1
    return length
    
class Grid:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def in_bounds(self, loc):
        (x,y) = loc
        return 0 <= x < self.width and 0 <= y < self.height

    def not_wall(self, loc):
        (x,y) = loc
        return maze[x][y]==0

    def moves(self, loc):
        (x,y) = loc
        moves = [(x+1,y), (x-1,y), (x,y+1), (x,y-1)]
        moves = filter(self.in_bounds, moves)
        moves = filter(self.not_wall, moves)
        return moves

def run_bfs(graph, start, end):
    mapped = deque()
    mapped.append(start)
    path_from = {}
    path_from[start] = None

    while mapped:
        current = mapped.popleft()

        if current == end:
            break

        for next in graph.moves(current):
            if next not in path_from:
                mapped.append(next)
                path_from[next] = current

    return path_from

init_maze(maze, rows, cols)

grid = Grid(rows, cols)
path = run_bfs(grid, start, end)
      
print_maze(maze, rows, cols, start, end, path)
