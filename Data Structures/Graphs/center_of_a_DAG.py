from graphs import Graph

def treeCenters(g):
    n = g.getSize()
    leaves = []
    for node in g:
        vertex = g.getVertex(node)
        if vertex.degree == 0 or vertex.degree == 1:
            leaves.append(vertex)
            vertex.setDegree(0)
    count = len(leaves)
    while count < n:
        new_leaves = []
        for node in leaves:
            for nbr in node.getConnections():
                vertex = g.getVertex(nbr)
                vertex.setDegree(vertex.getDegree() - 1)
                if vertex.getDegree() == 1:
                    new_leaves.append(vertex)
            node.setDegree(0)
        count += len(new_leaves)
        leaves = new_leaves
    return leaves


for t in range(int(input())):
    n = int(input())
    g = Graph()
    for i in range(n):
        a, b = map(str, input().split())
        g.addEdge(a, b)

    print(treeCenters(g))
