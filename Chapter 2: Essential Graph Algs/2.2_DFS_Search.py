# Depth First Search

# Input: G
# Output: pre: [u] and post: [v]

# pick vertex with smallest label
# pre is arrival times
# post is stuck/finishing times
# When arriving at new nodes, the label is 1 + previous node

# With a DFS 
# Forward edge: Which way the flow is going
# Back edge: The oposite of flow direction
# Cross edge: Everything else

# Pseudo Code:
# Explore(G, u):
    # pre[u] = t; t+=1
    # for v in G[u]:
        # if pre[v] = inf:
            # Explore(G, u)
    # post[u] = t

# DFS[G]:
    # pre, post, t = [inf] * n, [inf] * n, 1
    # for u in v:
        # if pre[u] = inf:
            # Explore(G, u)
    # return pre, post

# RT: Similar to BFS O(m + n)

# Modifying Explore:
    # R = empty list
    # post[u] = t; t+=1
    # new line: add u to front of R