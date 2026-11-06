
class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = 10**9 + 7
        m = r - l + 1

        up = list(range(m))
        down = list(range(m - 1, -1, -1))

        for _ in range(3, n + 1):
            new_up = [0] * m
            new_down = [0] * m

            # Prefix sums of down
            prefix = 0
            for x in range(m):
                new_up[x] = prefix
                prefix = (prefix + down[x]) % MOD

            # Suffix sums of up
            suffix = 0
            for x in range(m - 1, -1, -1):
                new_down[x] = suffix
                suffix = (suffix + up[x]) % MOD

            up = new_up
            down = new_down

        return (sum(up) + sum(down)) % MOD
