
class Solution {
public:
    string shortestSuperstring(vector<string>& words) {
        int n = words.size();
        int FULL = 1 << n;
        const int INF = 1e9;

        // Calculate maximum suffix-prefix overlap.
        vector<vector<int>> overlap(n, vector<int>(n, 0));

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (i == j) continue;

                int a = words[i].size();
                int b = words[j].size();

                for (int k = min(a, b); k >= 1; k--) {
                    if (words[i].compare(a - k, k,
                                         words[j], 0, k) == 0) {
                        overlap[i][j] = k;
                        break;
                    }
                }
            }
        }

        // dp[mask][i] = minimum length ending at word i.
        vector<vector<int>> dp(FULL, vector<int>(n, INF));

        // Parent array for reconstructing the answer.
        vector<vector<int>> parent(FULL, vector<int>(n, -1));

        // Base cases.
        for (int i = 0; i < n; i++) {
            dp[1 << i][i] = words[i].size();
        }

        // Bitmask DP.
        for (int mask = 1; mask < FULL; mask++) {
            for (int i = 0; i < n; i++) {

                if (!(mask & (1 << i))) continue;

                int prevMask = mask ^ (1 << i);

                if (prevMask == 0) continue;

                for (int j = 0; j < n; j++) {
                    if (!(prevMask & (1 << j))) continue;

                    int candidate = dp[prevMask][j]
                                  + words[i].size()
                                  - overlap[j][i];

                    if (candidate < dp[mask][i]) {
                        dp[mask][i] = candidate;
                        parent[mask][i] = j;
                    }
                }
            }
        }

        // Find the best ending word.
        int mask = FULL - 1;
        int last = 0;

        for (int i = 1; i < n; i++) {
            if (dp[mask][i] < dp[mask][last]) {
                last = i;
            }
        }

        // Reconstruct the optimal word order.
        vector<int> order;

        while (last != -1) {
            order.push_back(last);

            int prev = parent[mask][last];
            mask ^= (1 << last);
            last = prev;
        }

        reverse(order.begin(), order.end());

        // Construct the shortest superstring.
        string ans = words[order[0]];

        for (int i = 1; i < n; i++) {
            int prev = order[i - 1];
            int curr = order[i];

            ans += words[curr].substr(overlap[prev][curr]);
        }

        return ans;
    }
};
