class Solution:
    def solve(self, graph):
        reverse_graph = []
        for i in graph:
            reverse_graph.append([])
        
        for i in range(len(graph)):
            for j in graph[i]:
                reverse_graph[j].append(i)
        return reverse_graph
        