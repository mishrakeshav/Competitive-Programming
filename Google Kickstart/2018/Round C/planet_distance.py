from collections import OrderedDict,deque
class Vertex:
    def __init__(self,val):
        self.val = val 
        self.isVisited = False 
        self.connections = dict()
        self.parent = None
        self.distance = None
        
    
    def addConnection(self,val):
        self.connections[val] = True

class Graph:
    def __init__(self):
        self.vertices = OrderedDict()
    
    def addVertex(self,val):
        self.vertices[val] = Vertex(val)
        return self.vertices[val]
    
    def getVertex(self,val):
        if val in self.vertices:
            return self.vertices[val]
        return None

    def addEdge(self,src,dst):
        if src not in self:
            self.addVertex(src)
        if dst not in self:
            self.addVertex(dst)
        self.vertices[src].addConnection(dst)
        
    def __contains__(self,val):
        return val in self.vertices

    def __iter__(self):
        return iter(self.vertices.keys())
    
    def resetDistances(self):
        for node in self:
            self.vertices[node].distance = None
    
def dfs(g):
    visitedNodes = []

    for node in g:
        if node.isVisited and node != visitedNodes[-1]:
            return node 
        v = dfsHelper(node,g,visitedNodes)
        

def dfsHelper(startNode,g,visitedNodes):
    
    visitedNodes.append(startNode)
    for node in g.vertices[startNode].connections:
        if g.vertices[node] and visitedNodes[-1] != node:
            return node
        g.vertices[node].parent = startNode
        d = dfsHelper(node,g,visitedNodes)
    g.vertices[startNode].isVisited = True
    
    return d

def bfs(start,g):
    queue = deque()
    queue.appendleft(start)

    while len(queue):
        currVertex = queue.popleft()
        for nbr in g.vertices[currVertex].connections:
            pass 
     
for t in range(int(input())):
    n = int(input())
    g = Graph()
    for i in range(n):
        x,y = map(int,input().split())
        g.addVertex(x,y)
    
    node_in_cycle = dfs(g)
    start = node_in_cycle
    while g.vertices[start].parent != node_in_cycle:
        g.vertices[start].distance = 0
        start = g.vertices[start].parent
    g.vertices[start].distance = 0


    

    


