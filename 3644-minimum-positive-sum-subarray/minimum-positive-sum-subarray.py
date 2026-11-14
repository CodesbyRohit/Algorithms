class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        n = len(nums)
        pre = [0] * (n + 1)
        for i, x in enumerate(nums):
            pre[i + 1] = pre[i] + x

        INF = 10**9  # max possible sum is 100 * 1000 = 10^5
        best = INF
        for i in range(n):
            for j in range(i + l, min(i + r, n) + 1):
                s = pre[j] - pre[i]
                if 0 < s < best:
                    best = s
        return -1 if best == INF else best