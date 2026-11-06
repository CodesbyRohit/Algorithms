
class Solution:
    def mapWordWeights(self, words, weights):
        result = []

        for word in words:
            total = sum(weights[ord(c) - 97] for c in word)
            result.append(chr(122 - total % 26))

        return ''.join(result)
