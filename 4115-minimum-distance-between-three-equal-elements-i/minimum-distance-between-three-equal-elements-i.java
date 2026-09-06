import java.util.*;

class Solution {
    public int minimumDistance(int[] nums) {
        List<Integer>[] positions = new ArrayList[nums.length + 1];

        for (int i = 0; i < nums.length; i++) {
            if (positions[nums[i]] == null) {
                positions[nums[i]] = new ArrayList<>();
            }
            positions[nums[i]].add(i);
        }

        int ans = Integer.MAX_VALUE;

        for (List<Integer> list : positions) {
            if (list == null || list.size() < 3) {
                continue;
            }

            for (int i = 0; i + 2 < list.size(); i++) {
                int distance = 2 * (list.get(i + 2) - list.get(i));
                ans = Math.min(ans, distance);
            }
        }

        return ans == Integer.MAX_VALUE ? -1 : ans;
    }
}