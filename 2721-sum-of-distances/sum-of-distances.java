import java.util.*;

class Solution {
    public long[] distance(int[] nums) {
        int n = nums.length;
        long[] ans = new long[n];

        // value -> [count, sum of indices]
        Map<Integer, long[]> map = new HashMap<>();

        // Left to right
        for (int i = 0; i < n; i++) {
            int x = nums[i];

            long[] data = map.getOrDefault(x, new long[2]);

            // Distance from all previous equal elements
            ans[i] += (long) i * data[0] - data[1];

            data[0]++;
            data[1] += i;

            map.put(x, data);
        }

        map.clear();

        // Right to left
        for (int i = n - 1; i >= 0; i--) {
            int x = nums[i];

            long[] data = map.getOrDefault(x, new long[2]);

            // Distance from all following equal elements
            ans[i] += data[1] - (long) i * data[0];

            data[0]++;
            data[1] += i;

            map.put(x, data);
        }

        return ans;
    }
}