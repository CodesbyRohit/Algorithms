class Solution {
    public int minimumDistance(String word) {
        int n = word.length();

        int[][] pos = new int[26][2];

        for (int i = 0; i < 26; i++) {
            pos[i][0] = i / 6;
            pos[i][1] = i % 6;
        }

        int[] dp = new int[26];
        java.util.Arrays.fill(dp, 0);

        int prev = word.charAt(0) - 'A';

        for (int i = 1; i < n; i++) {
            int curr = word.charAt(i) - 'A';

            int[] next = new int[26];
            java.util.Arrays.fill(next, Integer.MAX_VALUE);

            int movePrevToCurr = distance(pos, prev, curr);

            for (int free = 0; free < 26; free++) {
                if (dp[free] == Integer.MAX_VALUE) {
                    continue;
                }

                next[free] = Math.min(
                    next[free],
                    dp[free] + movePrevToCurr
                );

                next[prev] = Math.min(
                    next[prev],
                    dp[free] + distance(pos, free, curr)
                );
            }

            dp = next;
            prev = curr;
        }

        int answer = Integer.MAX_VALUE;

        for (int cost : dp) {
            answer = Math.min(answer, cost);
        }

        return answer;
    }

    private int distance(int[][] pos, int a, int b) {
        return Math.abs(pos[a][0] - pos[b][0])
             + Math.abs(pos[a][1] - pos[b][1]);
    }
}