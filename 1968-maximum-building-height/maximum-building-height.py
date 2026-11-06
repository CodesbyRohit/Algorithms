
class Solution:
    def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
        restrictions.append([1, 0])

        limits = {i: h for i, h in restrictions}
        limits[n] = min(limits.get(n, n - 1), n - 1)

        arr = sorted(limits.items())

        # Left to right: propagate height restrictions
        for i in range(1, len(arr)):
            prev_id, prev_h = arr[i - 1]
            curr_id, curr_h = arr[i]

            arr[i] = (
                curr_id,
                min(curr_h, prev_h + curr_id - prev_id)
            )

        # Right to left: propagate restrictions backwards
        for i in range(len(arr) - 2, -1, -1):
            curr_id, curr_h = arr[i]
            next_id, next_h = arr[i + 1]

            arr[i] = (
                curr_id,
                min(curr_h, next_h + next_id - curr_id)
            )

        # Calculate maximum possible peak between restrictions
        ans = 0

        for i in range(1, len(arr)):
            left_id, left_h = arr[i - 1]
            right_id, right_h = arr[i]

            distance = right_id - left_id

            peak = (left_h + right_h + distance) // 2

            ans = max(ans, peak)

        return ans
