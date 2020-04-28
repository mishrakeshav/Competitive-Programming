from graphs import Graph,Vertex
from collections import deque
from bfs import bfs

"""
1. Build the graph
2. run the bfs from the starting word
3. traverse back from the vertex
"""


def buildGraph(words):
    d = {}
    g = Graph()
    for word in words:
        for i in range(len(word)):
            bucket = word[:i] + "_" + word[i+1:]
            if bucket in d:
                d[bucket].append(word)
            else:
                d[bucket] = [word] 
    for bucket in d.keys():
        for word1 in d[bucket]:
            for word2 in d[bucket]:
                if word1!=word2:
                    g.addEdge(word1,word2)
    return g
 

def traverse(y):
    x = y
    while x.getPred():
        print(x.getId())
        x = x.getPred()
    print(x.getId())       