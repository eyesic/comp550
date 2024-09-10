# Cycle Finding
# Input: Dir G
# Goal: Return a cycle C in G (or nothing)

# ALG: Check for a back edge (u,v)
# Pseudo Code:
# ALG(G):
    # T = DFS -tree (G)
    # for u in v: 
        # for v in G[u]:
            # if (u,v) is a back edge:
                # p = v -> u path in T
                # return p + (u,v)
# or simply for(u,v) in E, we are checking every edge

# ALG doesn't "miss" a cycle

# RT: DFS + O(m + n)