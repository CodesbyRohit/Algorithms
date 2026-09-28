class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        res = []
        
        for i in range(len(intervals)):
            # Case 1: newInterval comes strictly before the current interval
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                # Since the rest of the array is sorted and non-overlapping, just append it all
                return res + intervals[i:]
            
            # Case 2: newInterval comes strictly after the current interval
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
                
            # Case 3: Intervals overlap, so we merge them into newInterval
            else:
                newInterval = [
                    min(newInterval[0], intervals[i][0]), 
                    max(newInterval[1], intervals[i][1])
                ]
                
        # If we finish the loop and newInterval belongs at the very end
        res.append(newInterval)
        
        # Return the new array of non-overlapping intervals
        return res