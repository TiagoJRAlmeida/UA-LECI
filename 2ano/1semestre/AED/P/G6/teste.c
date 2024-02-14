#include <stdio.h>

int delannoy(int m, int n) {
    int dp[m + 1][n + 1];
    for (int i = 0; i <= m; i++) {
        for (int j = 0; j <= n; j++) {
            if (i == 0 || j == 0)
                dp[i][j] = 1;
            else
                dp[i][j] = dp[i - 1][j] + dp[i - 1][j - 1] + dp[i][j - 1];
        }
    }
    return dp[m][n];
}

int main() {
    int m, n;

    printf("Entre com m: ");
    scanf("%d", &m);
    printf("Entre com n: ");
    scanf("%d", &n);

    int result = delannoy(m, n);

    printf("D(%d, %d) = %d\n", m, n, result);

    return 0;
}
