
import heapq

class Solution:
    def maxTotalValue(self, nums, k):
        n = len(nums)

        # Precompute logarithms
        logs = [0] * (n + 1)
        for i in range(2, n + 1):
            logs[i] = logs[i // 2] + 1

        # Build Sparse Tables
        st_max = [nums[:]]
        st_min = [nums[:]]

        j = 1
        while (1 << j) <= n:
            half = 1 << (j - 1)
            prev_max = st_max[-1]
            prev_min = st_min[-1]

            st_max.append([
                max(prev_max[i], prev_max[i + half])
                for i in range(n - (1 << j) + 1)
            ])

            st_min.append([
                min(prev_min[i], prev_min[i + half])
                for i in range(n - (1 << j) + 1)
            ])

            j += 1

        # O(1) range query
        def get_range(l, r):
            j = logs[r - l + 1]
            length = 1 << j
            end = r - length + 1

            maximum = max(st_max[j][l], st_max[j][end])
            minimum = min(st_min[j][l], st_min[j][end])

            return maximum - minimum

        # Max heap: (-range, left, right)
        heap = [
            (-get_range(l, n - 1), l, n - 1)
            for l in range(n)
        ]
        heapq.heapify(heap)

        ans = 0

        for _ in range(k):
            neg_value, l, r = heapq.heappop(heap)
            ans -= neg_value

            if r > l:
                new_r = r - 1
                heapq.heappush(
                    heap,
                    (-get_range(l, new_r), l, new_r)
                )

        return ans
