
from collections import deque

class Solution:
    def assignEdgeWeights(self, edges):
        MOD = 10**9 + 7
        n = len(edges) + 1

        adj = [[] for _ in range(n + 1)]

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        q = deque([(1, 0)])
        max_depth = 0

        while q:
            node, depth = q.popleft()
            max_depth = max(max_depth, depth)

            for nei in adj[node]:
                adj[nei].remove(node)
                q.append((nei, depth + 1))

        return pow(2, max_depth - 1, MOD)
