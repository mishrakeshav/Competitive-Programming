from graphs import Graph


def detect_cyles_in_the_graph(g):
    def dfs(v, g):
        v.setVisited(True)
        for node in v.getConnections():
            vertex = g.getVertex(node)
            if vertex.isVisited():
                return True
            if dfs(vertex, g):
                return True
        v.setVisited(False)
        return False

    for node in g:
        vertex = g.getVertex(node)
        if dfs(vertex, g):
            return True
    return False


if __name__ == '__main__':
    for t in range(int(input())):
        # Number of edges
        n = int(input())
        g = Graph(undirected=False)
        for t in range(n):
            src, dst = map(int, input().split())
            g.addEdge(src, dst)
        print(detect_cyles_in_the_graph(g))
