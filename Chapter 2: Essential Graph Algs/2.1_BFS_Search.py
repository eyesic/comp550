# Breadth First Search
from collections import defaultdict

# Input: (G, s)
# G: directed graph (n,m)
# s: vertex in G, "start" or "source"

# Goal: return array d s.t. 
# d[u] = distance from S to u in G
# where distance is length(# of edges "in" path) of shortest path
# and a path is a sequence of verticies that follow edges

# if path p has k verticies then len(P) = k-1

# d = [inf]*n, d[s] = 0
# Q = queue(s), add/remove/create in O(1) time 

# Pseudo Code
# While |Q| >= 1:
    # u = dequeue from Q
    # for v in G[u]:
        # if d[u] = inf
            # d[v] = d[u] + 1
            # add u to Q

# RT: O(m+n)
# Total RT: out-deg(s) + out-deg(s's first out-neighbor)
# or the total sum of out-deg(u)

# This class represents a directed graph
# using adjacency list representation
class Graph:

    # Constructor
    def __init__(self):

        # Default dictionary to store graph
        self.graph = defaultdict(list)

    # Function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)

    # Function to print a BFS of graph
    def BFS(self, s):

        # Mark all the vertices as not visited
        visited = [False] * (max(self.graph) + 1)

        # Create a queue for BFS
        queue = []

        # Mark the source node as
        # visited and enqueue it
        queue.append(s)
        visited[s] = True

        while queue:

            # Dequeue a vertex from
            # queue and print it
            s = queue.pop(0)
            print(s, end=" ")

            # Get all adjacent vertices of the
            # dequeued vertex s.
            # If an adjacent has not been visited,
            # then mark it visited and enqueue it
            for i in self.graph[s]:
                if not visited[i]:
                    queue.append(i)
                    visited[i] = True

# Driver code
if __name__ == '__main__':

    # Create a graph given in
    # the above diagram
    g = Graph()
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)

    print("Following is Breadth First Traversal"
        " (starting from vertex 2)")
    g.BFS(2)

