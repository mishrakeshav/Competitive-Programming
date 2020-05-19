from collections import deque


def bfs(g, srcNode, dstNode):
    if srcNode == dstNode:
        return
    queue = deque()
    queue.append(g.getVertex(srcNode))
    while queue:
        currVertex = queue.popleft()
        if currVertex.val == dstNode:
            return
        for nbr in currVertex.getConnections():
            node = g.getVertex(nbr)
            if node.getColor() == "white":
                node.setColor("grey")
                node.setPrevious(currVertex)
                queue.append(node)
        currVertex.setColor("black")
