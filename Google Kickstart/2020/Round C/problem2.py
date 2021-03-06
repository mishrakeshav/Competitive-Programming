import math
from collections import deque
from collections import defaultdict


class Vertex:
    def __init__(self, val):
        self.val = val
        self.connections = defaultdict()
        self.visited = False
        self.color = 'white'
        self.previous = None
        self.distance = math.inf
        self.degree = None

    def setColor(self, color):
        self.color = color

    def setVisited(self, visited):
        self.visited = visited

    def setPrevious(self, val):
        self.previous = val

    def setDistance(self, val):
        self.distance = val

    def setDegree(self, val):
        self.degree = val

    def addConnection(self, node, w=0):
        self.connections[node] = w
        self.degree = len(self.connections)

    def getColor(self):
        return self.color

    def isVisited(self):
        return self.visited

    def getConnections(self):
        return self.connections

    def getDistance(self):
        return self.distance

    def getEdgeWeight(self, val):
        return self.connections.get(val)

    def getPrevious(self):
        return self.previous

    def getDegree(self):
        return self.degree

    def __repr__(self):
        return str(self.val) + "-->" + str(self.connections)


class Graph:
    def __init__(self, undirected=True):
        self.g = dict()
        self.undirected = undirected
        self.size = 0

    def addVertex(self, val):
        self.g[val] = Vertex(val)

    def addEdge(self, src, dst, w=0):
        if src not in self.g:
            self.g[src] = Vertex(src)
        if dst not in self.g:
            self.g[dst] = Vertex(dst)

        self.g[src].addConnection(dst, w)
        if self.undirected:
            self.g[dst].addConnection(src, w)

    def getSize(self):
        return len(self.g)

    def getVertices(self):
        return self.g.keys()

    def __contains__(self, val):
        return val in self.g

    def __iter__(self):
        return iter(self.g)

    def getVertex(self, val):
        return self.g.get(val, None)


def detect_cyles_in_the_graph(g):
    def dfs(v, g):
        v.setVisited(True)
        for node in v.getConnections():
            vertex = g.getVertex(node)
            if vertex.isVisited():
                return True
            if dfs(vertex, g):
                return True
        v.setVisited(False)
        return False

    for node in g:
        vertex = g.getVertex(node)
        if dfs(vertex, g):
            return True
    return False


def topological_sorting(g):
    def dfs(g, ordering, v):
        for node in v.getConnections():
            vertex = g.getVertex(node)
            if vertex.isVisited():
                continue
            dfs(g, ordering, vertex)
        v.setVisited(True)
        ordering.appendleft(v.val)

    def helper(g, ordering):
        for node in g:
            vertex = g.getVertex(node)
            if vertex.isVisited():
                continue
            dfs(g, ordering, vertex)

    ordering = deque()
    helper(g, ordering)
    return ordering


for t in range(int(input())):
    row, col = map(int, input().split())
    wall = []
    for i in range(row):
        wall.append(input())
    g = Graph(undirected=False)

    for i in range(col):
        for j in range(row - 1, 0, -1):
            if wall[j][i] == wall[j - 1][i]:
                continue
            # print(wall[j][i], wall[j - 1][i])
            g.addEdge(wall[j][i], wall[j - 1][i])

    if detect_cyles_in_the_graph(g):
        print("Case #{}: {}".format(t + 1, -1))
    else:
        for node in g:
            vertex = g.getVertex(node)
            vertex.setVisited(False)
        order = topological_sorting(g)
        print("Case #{}: {}".format(t + 1, "".join(order)))
