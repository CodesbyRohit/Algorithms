class Solution {
    using ll = long long;
    static constexpr ll MOD = 1'000'000'007;

    using Matrix = vector<vector<ll>>;

    Matrix multiply(const Matrix& A, const Matrix& B) {
        int sz = A.size();
        Matrix C(sz, vector<ll>(sz, 0));

        for (int i = 0; i < sz; ++i) {
            for (int k = 0; k < sz; ++k) {
                if (A[i][k] == 0) continue;

                ll val = A[i][k];

                for (int j = 0; j < sz; ++j) {
                    C[i][j] = (C[i][j] +
                               val * B[k][j]) % MOD;
                }
            }
        }

        return C;
    }

    vector<ll> multiply(const Matrix& A,
                        const vector<ll>& v) {
        int sz = A.size();
        vector<ll> res(sz, 0);

        for (int i = 0; i < sz; ++i) {
            for (int j = 0; j < sz; ++j) {
                res[i] = (res[i] +
                          A[i][j] * v[j]) % MOD;
            }
        }

        return res;
    }

public:
    int zigZagArrays(int n, int l, int r) {
        int m = r - l + 1;
        int sz = 2 * m;

        vector<ll> dp(sz);

        for (int i = 0; i < m; ++i) {
            dp[i] = i;
            dp[m + i] = m - 1 - i;
        }

        Matrix T(sz, vector<ll>(sz, 0));

        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < i; ++j) {
                T[i][m + j] = 1;
            }

            for (int j = i + 1; j < m; ++j) {
                T[m + i][j] = 1;
            }
        }

        int exp = n - 2;

        while (exp > 0) {
            if (exp & 1) {
                dp = multiply(T, dp);
            }

            exp >>= 1;

            if (exp > 0) {
                T = multiply(T, T);
            }
        }

        ll ans = 0;

        for (ll x : dp) {
            ans = (ans + x) % MOD;
        }

        return (int)ans;
    }
};
