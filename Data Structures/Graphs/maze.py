from collections import deque


class Node():
    def __init__(self, val):
        self.visited = False
        self.val = val
        self.prev = None

    def setPrevious(self, node):
        self.prev = node

    def setVisited(self):
        self.visited = True

    def resetVisited(self):
        self.visited = False

    def isVisited(self):
        return self.visited

    def getPrev(self):
        return self.prev

    def __repr__(self):
        return self.val


def helper(x, y, q, maze):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    for i in range(4):
        new_x = x + dx[i]
        new_y = y + dy[i]
        # print(q)
        if new_x < 0 or new_x > m - 1:
            continue
        if new_y < 0 or new_y > n - 1:
            continue
        if maze[new_y][new_x].isVisited():
            continue
        if maze[new_y][new_x].val == "O":
            continue
        maze[new_y][new_x].setPrevious((x, y))
        maze[new_y][new_x].setVisited()
        q.append((new_x, new_y))

# doing bfs from the starting cell
def solve(start_x, start_y, maze):

    queue = deque()
    maze[start_y][start_x].setVisited()
    queue.append((start_x, start_y))
    while queue:
        x, y = queue.popleft()
        if maze[y][x] == "E":
            return
        helper(x, y, queue, maze)


for t in range(int(input())):
    n, m = map(int, input().split())
    maze = []
    for i in range(n):
        s = input()
        maze.append([])
        for j in s:
            maze[i].append(Node(j))
    """
    1
    5 5
    ****O
    **O*O
    *OO**
    *OO**
    *EO*E
    0 0
    """
    start_x, start_y = map(int, input().split())

    solve(start_x, start_y, maze)
    path = deque()
    escape = maze[1][2]

    while escape.getPrev():
        x, y = escape.getPrev()
        path.appendleft((x, y))
        escape = maze[y][x]

    for x, y in path:
        print(y, x)
