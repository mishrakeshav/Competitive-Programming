from queue import PriorityQueue
from graphs import Graph


def dijkstras(g, startNode, dstNode):
    if startNode == dstNode:
        return
    P = PriorityQueue()
    g.getVertex(startNode).setDistance(0)
    P.put((0, startNode))

    while not P.empty():
        dst, val = P.get()
        if val == dstNode:
            return
        node = g.getVertex(val)
        for nbr in node.getConnections():
            nbr_node = g.getVertex(nbr)
            if nbr_node.getDistance() > dst + node.getEdgeWeight(nbr):
                nbr_node.setDistance(dst + node.getEdgeWeight(nbr))
                nbr_node.setPrevious(node)
                P.put([nbr_node.getDistance(), nbr])
