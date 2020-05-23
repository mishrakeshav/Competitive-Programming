
from graphs import Graph
from collections import deque


def topological_sorting(g):
    ordering = deque()
    helper(g, ordering)
    return ordering


def helper(g, ordering):
    for node in g:
        vertex = g.getVertex(node)
        if vertex.isVisited():
            continue
        dfs(g, ordering, vertex)


def dfs(g, ordering, v):
    for node in v.getConnections():
        vertex = g.getVertex(node)
        if vertex.isVisited():
            continue
        dfs(g, ordering, vertex)
    v.setVisited(True)
    ordering.appendleft(v.val)


if __name__ == '__main__':
    for t in range(int(input())):
        n = int(input())
        g = Graph(undirected=False)
        for i in range(n):
            src, dst = map(int, input().split())
            g.addEdge(src, dst)
        order = topological_sorting(g)
        print(order)
