# https://www.geeksforgeeks.org/python-program-for-breadth-first-search-or-bfs-for-a-graph/
# Python3 Program to print BFS traversal OF A GRAPH
# from a given source vertex. BFS(int s)
# traverses vertices reachable from s.
from collections import defaultdict
from collections import deque

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def bfs(self, start):
        # Mark all the vertices as note visited
        visited = [False] * (len(self.graph))

        # Create a queue for BFS
        queue = deque()

        # Mark the source node as visited and enqueue it
        queue.append(start)
        visited[start] = True

        while queue:
            # Dequeue a vertex from queue and print it
            s = queue.popleft()
            print(s, end = " ")

            # Get all adjacent vertices of the dequeued vertex s. If an adjacent
            # has not been visited, then mark it ias visited and enqueue it
            for i in self.graph[s]:
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

print("Breadth First Traversal starting from vertex 2")
g.bfs(2)
print("\n")
