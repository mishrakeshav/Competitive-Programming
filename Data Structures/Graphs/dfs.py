from graphs import Graph

def dfs(graph,endvertex):
    for v in graph:
        dfsHelper(v) 


def dfsHelper(startVertex):
    startVertex.setColor('gray')
    for nextVertex in startVertex.getConnections():
        if nextVertex.getColor() == 'white':
            nextVertex.setPred(startVertex)
            dfsHelper(nextVertex)
    startVertex.setColor('black')

