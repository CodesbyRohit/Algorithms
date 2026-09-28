class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        # Create a list of available numbers to pick from
        nums = [str(i) for i in range(1, n + 1)]
        
        # Precompute factorials for 0! to (n-1)!
        fact = [1] * n
        for i in range(1, n):
            fact[i] = fact[i - 1] * i
            
        # Convert k to 0-indexed to make the math align perfectly
        k -= 1
        res = []
        
        for i in range(n, 0, -1):
            # Determine which block of (i-1)! permutations our k falls into
            idx = k // fact[i - 1]
            res.append(nums.pop(idx))
            
            # Update k to the remainder for the next iteration
            k %= fact[i - 1]
            
        return "".join(res)