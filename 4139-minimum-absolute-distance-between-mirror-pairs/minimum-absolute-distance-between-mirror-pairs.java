import java.util.*;

class Solution {
    public int minMirrorPairDistance(int[] nums) {
        Map<Integer, Integer> map = new HashMap<>();

        int ans = Integer.MAX_VALUE;

        for (int j = 0; j < nums.length; j++) {

            // Check whether some previous number reverses to nums[j]
            if (map.containsKey(nums[j])) {
                int i = map.get(nums[j]);
                ans = Math.min(ans, j - i);
            }

            // Store reverse(nums[j]) for future elements
            map.put(reverse(nums[j]), j);
        }

        return ans == Integer.MAX_VALUE ? -1 : ans;
    }

    private int reverse(int x) {
        int rev = 0;

        while (x > 0) {
            rev = rev * 10 + x % 10;
            x /= 10;
        }

        return rev;
    }
}