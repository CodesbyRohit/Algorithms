import math

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # The total number of steps is (m - 1) down + (n - 1) right = m + n - 2 total steps.
        # We simply choose exactly (m - 1) steps to be our downward moves.
        return math.comb(m + n - 2, m - 1)