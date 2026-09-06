import java.util.*;

class Solution {
    public long minimumTotalDistance(List<Integer> robot, int[][] factory) {

        Collections.sort(robot);

        Arrays.sort(factory, (a, b) -> Integer.compare(a[0], b[0]));

        int n = robot.size();

        long[] dp = new long[n + 1];
        Arrays.fill(dp, Long.MAX_VALUE / 2);

        dp[0] = 0;

        for (int[] f : factory) {
            int position = f[0];
            int limit = f[1];

            long[] next = new long[n + 1];
            Arrays.fill(next, Long.MAX_VALUE / 2);

            for (int i = 0; i <= n; i++) {
                next[i] = dp[i];
            }

            for (int i = 0; i <= n; i++) {

                if (dp[i] >= Long.MAX_VALUE / 2) {
                    continue;
                }

                long cost = 0;

                // Take robots i, i+1, ..., i+k-1
                for (int k = 1; k <= limit && i + k <= n; k++) {

                    cost += Math.abs(
                        (long) robot.get(i + k - 1) - position
                    );

                    next[i + k] = Math.min(
                        next[i + k],
                        dp[i] + cost
                    );
                }
            }

            dp = next;
        }

        return dp[n];
    }
}