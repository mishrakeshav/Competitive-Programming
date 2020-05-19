from collections import deque
from bfs import bfs
from dfs import dfs
from graphs import Graph
from dijkstras import dijkstras

for t in range(int(input())):
    m = int(input())  # Number of edges
    g = Graph(undirected=False)
    for i in range(m):
        a, b, w = map(str, input().split())  # name of the edges connected
        g.addEdge(a, b, int(w))

    src, dst = map(str, input().split())
    # path = []

    # dijkstras(g, src, dst)
    # print(path)
    # path = deque()
    # node = g.getVertex(dst)
    # cost = node.getDistance()
    # print(cost)
    # while node:
    #     path.appendleft(node.val)
    #     node = node.getPrevious()
    # print(path)
