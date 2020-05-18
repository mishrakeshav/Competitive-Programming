# Implementation of Graph Data Structure
class Vertex:
    def __init__(self, key):
        self.id = key
        self.connectedTo = dict()
        self.distance = -1
        self.predecessor = None
        self.color = "white"

    def addNeighbor(self, nbr, weight=0):
        self.connectedTo[nbr] = weight

    def __str__(self):
        return str(self.id) + " connectedTo: " + str([x.id for x in self.connectedTo])

    def setDistance(self, d):
        self.distance = d

    def setPred(self, p):
        self.predecessor = p

    def setColor(self, color):
        self.color = color

    def getDistance(self):
        return self.distance

    def getPred(self):
        return self.predecessor

    def setColor(self):
        return self.color

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self, nbr):
        return self.connectedTo[nbr]


class Graph:
    def __init__(self):
        self.vertList = dict()
        self.numVertices = 0

    def addVertex(self, key):
        self.numVertices += 1
        self.vertList[key] = Vertex(key)
        return self.vertList[key]

    def getVertex(self, key):
        if key in self.vertList:
            return self.vertList[key]
        else:
            return None

    def __contains__(self, key):
        return key in self.vertList

    def addEdge(self, f, t, weight=0):
        if f not in self.vertList:
            self.addVertex(f)
        if t not in self.vertList:
            self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], weight)

    def getVertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.keys())
