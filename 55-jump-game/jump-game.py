class Solution:
    def canJump(self, nums: list[int]) -> bool:
        max_reach = 0
        
        for i, jump in enumerate(nums):
            # If our current index is beyond our maximum reach, we're stuck.
            if i > max_reach:
                return False
            
            # Update the maximum reachable index from our current position.
            max_reach = max(max_reach, i + jump)
            
            # Optimization: If we can already reach or pass the last index, stop early.
            if max_reach >= len(nums) - 1:
                return True
                
        return True