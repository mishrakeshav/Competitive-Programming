from collections import deque


def bfs(g,start):

    start.setDistance(0)
    start.setPred(None)
    queue = deque()
    queue.appendleft(start)
    
    while len(queue):
        currVertex = queue.popleft()
        for nbr in currVertex.getConnections():
            if (nbr.getColor() == "white"):
                nbr.setColor("gray")
                nbr.setDistance(currVertex.getDistance() + 1)
                nbr.setPred(currVertex)
                queue.appendleft(nbr)
        currVertex.setColor("black")