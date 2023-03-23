# practicing BFS for graphs
from collections import defaultdict
from collections import deque

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def bfs(self, start):
        queue = deque()
        visited = [False] * len(self.graph)
        queue.append(start)

        while queue:
            node = queue.popleft()
            print(node)

            for i in self.graph[node]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True



# Driver code
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)
print(g.graph)

print("Breadth First Traversal starting from vertex 2")
g.bfs(2)
print("\n")
