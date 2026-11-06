
from collections import defaultdict

class Solution:
    def countServers(self, n, logs, x, queries):
        logs.sort(key=lambda a: a[1])

        indexed_queries = sorted(
            (q, i) for i, q in enumerate(queries)
        )

        freq = defaultdict(int)
        ans = [0] * len(queries)

        left = right = 0
        m = len(logs)

        for q, idx in indexed_queries:
            start = q - x

            # Add logs within the right boundary
            while right < m and logs[right][1] <= q:
                freq[logs[right][0]] += 1
                right += 1

            # Remove logs before the left boundary
            while left < right and logs[left][1] < start:
                server = logs[left][0]
                freq[server] -= 1

                if freq[server] == 0:
                    del freq[server]

                left += 1

            ans[idx] = n - len(freq)

        return ans
