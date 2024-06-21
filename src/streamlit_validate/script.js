function isMatch(s, p) {
    const m = s.length, n = p.length;
    const dp = Array.from({ length: m + 1 }, () => Array(n + 1).fill(false));
    dp[0][0] = true;

    for (let j = 1; j <= n; j++) {
        if (p[j - 1] === '*' && dp[0][j - 2]) {
            dp[0][j] = true;
        }
    }

    for (let i = 1; i <= m; i++) {
      for (let j = 1; j <= n; j++) {
          if (p[j - 1] === s[i - 1] || p[j - 1] === '.') {
              dp[i][j] = dp[i - 1][j - 1];
          } else if (p[j - 1] === '*') {
              dp[i][j] = dp[i][j - 2] || (dp[i - 1][j] && (s[i - 1] === p[j - 2] || p[j - 2] === '.'));
          }
      }
    }

    return dp[m][n];
}


function main() {
    const inputs =['mississippi ', 'mis*is*p*. '];
    const s = inputs[0];
    const p = inputs[1];
    const result = isMatch(s, p);
    console.log(result);
}
main();