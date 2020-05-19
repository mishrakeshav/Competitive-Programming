
def dfs(g, srcNode, dstNode, path):
    path.append(srcNode)
    if srcNode == dstNode:
        return path
    if not g.getVertex(srcNode).isVisited():
        g.getVertex(srcNode).setVisited(True)
        for node in g.getVertex(srcNode).getConnections():
            k = dfs(g, node, dstNode, path)
            if k:
                return path
            path.pop()
