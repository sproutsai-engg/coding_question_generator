##Question ID: 1513

MOD = 10**9 + 7

def countGoodStrings(s1, s2, evil):
    n = len(s1)
    m = len(evil)
    dp = [[0] * m for _ in range(n + 1)]

    # Preprocess the KMP prefix function for the evil string
    lps = [0] * m
    len_ = 0
    i = 1
    while i < m:
        if evil[i] == evil[len_]:
            len_ += 1
            lps[i] = len_
            i += 1
        elif len_:
            len_ = lps[len_ - 1]
        else:
            i += 1

    dp[0][0] = 1
    for i in range(n):
        for j in range(m):
            for k in range(2):
                for c in range(ord('a'), ord(s2[i] if k else 'z') + 1):
                    e = j
                    while e and (chr(c) != evil[e]):
                        e = lps[e - 1]

                    if chr(c) != evil[e]:
                        e += 1

                    if e != m:
                        dp[i + 1][k | (c < ord(s2[i]))] += dp[i][k]
                        dp[i + 1][k | (c < ord(s2[i]))] %= MOD

    return (dp[n][1] - dp[n][0] + MOD) % MOD


## Structure
MOD = 10**9 + 7
    # Your code here

    pass