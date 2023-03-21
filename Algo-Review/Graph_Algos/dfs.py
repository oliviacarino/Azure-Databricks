# Python3 program to print DFS traversal from a given -- GRAPH!
# source vertex. (recursive implementation)
# diagram of graph used in example (as well as dfs code):
# https://www.geeksforgeeks.org/python-program-for-depth-first-search-or-dfs-for-a-graph/

from collections import defaultdict
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def dfs_helper(self, v, visited):
        # If wanting to check for a cycle, insert an if statement here
        # checking if the vertex v is already True in visited
        visited[v] = True
        print(v)

        # Recurse for all vertices adjacent to this vertex
        for i in self.graph[v]:
            if visited[i] == False:
                self.dfs_helper(i, visited)

    def dfs(self):
        V = len(self.graph) # total vertices

        # Mark all the vertices as not visited
        visited = [False] * (V)


        # Call dfs_helper to print DFS traversal starting from all
        # vertices one by one
        for i in range(V):
            if visited[i] == False:
                self.dfs_helper(i, visited)

# Driver code
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)

print("Depth First Traversal")
g.dfs()
