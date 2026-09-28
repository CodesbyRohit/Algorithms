class Solution:
    def generateMatrix(self, n: int) -> list[list[int]]:
        # Initialize the n x n matrix with zeros
        matrix = [[0] * n for _ in range(n)]
        
        # Define our starting boundaries
        top, bottom = 0, n - 1
        left, right = 0, n - 1
        
        num = 1
        
        # Continue until we have filled elements from 1 to n^2
        while num <= n * n:
            # Traverse Right: fill the top row from left to right
            for i in range(left, right + 1):
                matrix[top][i] = num
                num += 1
            top += 1 # Shrink top boundary
            
            # Traverse Down: fill the right column from top to bottom
            for i in range(top, bottom + 1):
                matrix[i][right] = num
                num += 1
            right -= 1 # Shrink right boundary
            
            # Traverse Left: fill the bottom row from right to left
            for i in range(right, left - 1, -1):
                matrix[bottom][i] = num
                num += 1
            bottom -= 1 # Shrink bottom boundary
            
            # Traverse Up: fill the left column from bottom to top
            for i in range(bottom, top - 1, -1):
                matrix[i][left] = num
                num += 1
            left += 1 # Shrink left boundary
            
        return matrix