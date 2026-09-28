class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        # If the starting cell has an obstacle, the robot can't even start.
        if not obstacleGrid or obstacleGrid[0][0] == 1:
            return 0
            
        n = len(obstacleGrid[0])
        dp = [0] * n
        dp[0] = 1  # Base case: 1 way to reach the starting position
        
        for row in obstacleGrid:
            for j in range(n):
                # An obstacle and space are marked as 1 or 0 respectively in grid.
                # A path that the robot takes cannot include any square that is an obstacle[cite: 9].
                if row[j] == 1:
                    dp[j] = 0
                elif j > 0:
                    # Number of ways to reach this cell is the sum of ways 
                    # from the cell above (currently in dp[j]) and the cell to the left (dp[j-1])
                    dp[j] += dp[j-1]
                    
        # Return the number of possible unique paths to reach the bottom-right corner[cite: 9].
        return dp[-1]