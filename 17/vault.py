import hashlib
from collections import deque

input = 'veumntbg'

rows = 4
cols = 4
start = (0,0)
end = (3,3)

open = ['b', 'c', 'd', 'e', 'f']
maze = [[0 for x in range(cols)] for y in range(rows)]
    
class Grid:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def in_bounds(self, loc):
        (x,y) = loc
        return 0 <= x < self.width and 0 <= y < self.height
   
    def moves(self, current_path):
        moves = []
        path = current_path[0]
        (x,y) = current_path[1]
        digest = list(hashlib.md5('{}{}'.format(input, path).encode()).hexdigest())
        if digest[0] in open:
            if self.in_bounds((x,y-1)):
                moves.append(['{}U'.format(path), (x,y-1)])
        if digest[1] in open:
            if self.in_bounds((x,y+1)):
                moves.append(['{}D'.format(path), (x,y+1)])
        if digest[2] in open:
            if self.in_bounds((x-1,y)):
                moves.append(['{}L'.format(path), (x-1,y)])
        if digest[3] in open:
            if self.in_bounds((x+1,y)):
                moves.append(['{}R'.format(path), (x+1,y)])
        return moves

   
def run_bfs(graph, start, end):
    mapped = deque()
    mapped.append(start)

    path = ''
    path_len = 0
    
    while mapped:
        current = mapped.popleft()
        #print('current = {}'.format(current))
        
        if current[1] == end:
            if len(current[0]) > path_len:
                print('Path({}) = {}'.format(len(current[0]), current[0]))
                path = current[0]
                path_len = len(current[0])
            continue

        for next in graph.moves(current):
            mapped.append(next)

    return;

grid = Grid(rows, cols)
first = grid.moves(['', (0,0)])
path = run_bfs(grid, first[0], end)
