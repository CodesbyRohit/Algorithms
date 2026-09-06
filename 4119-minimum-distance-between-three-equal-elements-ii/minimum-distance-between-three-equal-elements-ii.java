class Solution {
    public int minimumDistance(int[] nums) {
        int n = nums.length;

        int[] last = new int[n + 1];
        int[] secondLast = new int[n + 1];

        java.util.Arrays.fill(last, -1);
        java.util.Arrays.fill(secondLast, -1);

        int ans = Integer.MAX_VALUE;

        for (int i = 0; i < n; i++) {
            int x = nums[i];

            if (secondLast[x] != -1) {
                int distance = 2 * (i - secondLast[x]);
                ans = Math.min(ans, distance);
            }

            secondLast[x] = last[x];
            last[x] = i;
        }

        return ans == Integer.MAX_VALUE ? -1 : ans;
    }
}