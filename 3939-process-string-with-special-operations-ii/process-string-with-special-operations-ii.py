
class Solution:
    def processStr(self, s, k):
        n = len(s)
        length = [0] * (n + 1)

        # Forward pass: calculate prefix lengths
        for i, c in enumerate(s):
            prev = length[i]

            if c == '*':
                length[i + 1] = max(0, prev - 1)
            elif c == '#':
                length[i + 1] = prev * 2
            elif c == '%':
                length[i + 1] = prev
            else:
                length[i + 1] = prev + 1

        # Out of bounds
        if k >= length[n]:
            return '.'

        # Backward pass: find original character
        for i in range(n - 1, -1, -1):
            c = s[i]
            prev = length[i]

            if c == '%':
                k = prev - 1 - k

            elif c == '#':
                if prev:
                    k %= prev

            elif c == '*':
                pass

            else:
                if k == prev:
                    return c

        return '.'
