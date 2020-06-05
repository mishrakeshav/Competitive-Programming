import math
from collections import deque


class Vertex:
    def __init__(self, val):
        self.val = val
        self.connections = dict()
        self.visited = False
        self.previous = None

    def setVisited(self, visited):
        self.visited = visited

    def setPrevious(self, val):
        self.previous = val

    def addConnection(self, node, w=0):
        self.connections[node] = w

    def isVisited(self):
        return self.visited

    def getConnections(self):
        return self.connections

    def __repr__(self):
        return str(self.val)


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
    def dfshelper(g, ordering, v):
        for node in v.getConnections():
            vertex = g.getVertex(node)
            if vertex.isVisited():
                continue
            dfshelper(g, ordering, vertex)
        v.setVisited(True)
        ordering.appendleft(v.val)

    def helper(g, ordering):
        for node in g:
            vertex = g.getVertex(node)
            if vertex.isVisited():
                continue
            dfshelper(g, ordering, vertex)
    ordering = deque()
    helper(g, ordering)
    return ordering


if __name__ == '__main__':
    g = Graph(undirected=False)
    for i in range(3):
        a = input()
        if a[1] == '<':
            g.addEdge(a[0], a[2])
        else:
            g.addEdge(a[2], a[0])
    if detect_cyles_in_the_graph(g):
        print("Impossible")
    else:
        order = topological_sorting(g)
        print("".join(order))
