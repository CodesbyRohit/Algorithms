
class Solution:
    def processStr(self, s):
        result = ""

        for c in s:
            if c == '*':
                result = result[:-1]
            elif c == '#':
                result += result
            elif c == '%':
                result = result[::-1]
            else:
                result += c

        return result
