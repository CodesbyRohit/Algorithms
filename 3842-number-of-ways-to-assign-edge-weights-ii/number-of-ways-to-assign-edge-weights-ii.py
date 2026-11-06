
from collections import deque

class Solution:
    def assignEdgeWeights(self, edges, queries):
        MOD = 10**9 + 7
        n = len(edges) + 1
        LOG = n.bit_length()

        # Build adjacency list
        adj = [[] for _ in range(n + 1)]

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        # BFS: calculate depth and immediate parent
        depth = [0] * (n + 1)
        parent = [0] * (n + 1)
        parent[1] = 1

        q = deque([1])

        while q:
            u = q.popleft()

            for v in adj[u]:
                if v != parent[u]:
                    parent[v] = u
                    depth[v] = depth[u] + 1
                    q.append(v)

        # Binary lifting table
        up = [parent]

        for j in range(1, LOG):
            prev = up[-1]
            up.append([prev[prev[i]] for i in range(n + 1)])

        # Lowest Common Ancestor
        def lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u

            diff = depth[u] - depth[v]

            for j in range(LOG):
                if diff & (1 << j):
                    u = up[j][u]

            if u == v:
                return u

            for j in range(LOG - 1, -1, -1):
                if up[j][u] != up[j][v]:
                    u = up[j][u]
                    v = up[j][v]

            return up[0][u]

        # Precompute powers of 2
        powers = [1] * n

        for i in range(1, n):
            powers[i] = (powers[i - 1] * 2) % MOD

        # Answer queries
        ans = []

        for u, v in queries:
            w = lca(u, v)

            dist = depth[u] + depth[v] - 2 * depth[w]

            ans.append(powers[dist - 1] if dist else 0)

        return ans
