# This algorithm is used to find a "Mother" vertex. A mother vertex
# is a vertex from which we can reach all the nodes in the graph through
# directed paths.
# Time: O(V + E)
# CONS: will only find ONE mother vertex, even if there are multiple ones present

from collections import deque
import sys
sys.path.insert(0, '/Users/olivia/Dropbox/Coding/Python/DS/LinkedList')
from singly import *

# Graph class used
class Graph:
    def __init__(self, vertices):
        # Total number of vertices
        self.vertices = vertices
        # definining a list which can hold multiple LinkedLists
        # equal to the number of vertices in the graph
        self.array = []
        # Creating a new Linked List for each vertex/index of the list
        for i in range(vertices):
            self.array.append(LinkedList())

    # Function to add an edge from source to destination
    def add_edge(self, source, destination):
        if source < self.vertices and destination < self.vertices:
        # As we are implementing a directed graph, (1,0) is not equal to (0,1)
            self.array[source].insert_at_head(destination)
            # Uncomment the following line for undirected graph
            # self.array[destination].insert_at_head(source)

        # If we were to implement an Undirected Graph i.e (1,0) == (0,1)
        # We would create an edge from destination towards source as well
        # i.e self.list[destination].insertAtHead(source)

    def print_graph(self):
        print(">>Adjacency List of Directed Graph<<")
        for i in range(self.vertices):
            print("|", i, end=" | => ")
            temp = self.array[i].get_head()
            while temp is not None:
                print("[", temp.data, end=" ] -> ")
                temp = temp.next_element
            print("None")

# Kosaraju's Algo Implementation
def find_mother_vertex(g):
    # visited[] is used for DFS. Initially all are
    # initialized as not visited
    visited = [False]*(g.vertices)
    # To store last finished vertex (or mother vertex)
    last_v = 0
    # Do a DFS traversal and find the last finished
    # vertex
    for i in range(g.vertices):
        if not visited[i]:
            perform_DFS(g, i, visited)
            last_v = i

    # If there exist mother vertex (or vetices) in given
    # graph, then v must be one (or one of them)

    # Now check if v is actually a mother vertex (or graph
    # has a mother vertex). We basically check if every vertex
    # is reachable from v or not.

    # Reset all values in visited[] as false and do
    # DFS beginning from v to check if all vertices are
    # reachable from it or not.
    visited = [False]*(g.vertices)
    perform_DFS(g, last_v, visited)
    if any (not i for i in visited): # any() func iterates over a list
        return -1
    else:
        return last_v

# A recursive function to print DFS starting from v
def perform_DFS(g, node, visited):
    # Mark the current node as visited and print it
    visited[node] = True
    # Recur for all the vertices adjacent to this vertex
    temp = g.array[node].head_node
    while temp:
        if not visited[temp.data]:
            perform_DFS(g, temp.data, visited)
        temp = temp.next_element

# Driver code
g = Graph(4)
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(3, 0)
g.add_edge(3, 1)
print(find_mother_vertex(g))
