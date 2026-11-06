
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        altitude = maximum = 0

        for g in gain:
            altitude += g
            maximum = max(maximum, altitude)

        return maximum
