import math


class Vertex:
    def __init__(self, val):
        self.val = val
        self.connections = dict()
        self.visited = False
        self.color = 'white'
        self.previous = None
        self.distance = math.inf

    def setColor(self, color):
        self.color = color

    def setVisited(self, visited):
        self.visited = visited

    def setPrevious(self, val):
        self.previous = val

    def setDistance(self, val):
        self.distance = val

    def addConnection(self, node, w=0):
        self.connections[node] = w

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


class Graph:
    def __init__(self, undirected=True):
        self.g = dict()
        self.undirected = undirected

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

    def getVertices(self):
        return self.g.keys()

    def __contains__(self, val):
        return val in self.g

    def __iter__(self):
        return iter(self.g)

    def getVertex(self, val):
        return self.g.get(val, None)
