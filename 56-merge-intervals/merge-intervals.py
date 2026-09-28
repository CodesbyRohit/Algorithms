class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        # Sort intervals based on the starting value of each interval
        intervals.sort(key=lambda x: x[0])
        
        merged = []
        for interval in intervals:
            # If the merged list is empty or the current interval does not overlap
            # with the previous one, append it directly.
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                # If they do overlap, merge them by updating the end time of the 
                # last interval in the merged list to the maximum end time.
                merged[-1][1] = max(merged[-1][1], interval[1])
                
        # Return the array of non-overlapping intervals
        return merged