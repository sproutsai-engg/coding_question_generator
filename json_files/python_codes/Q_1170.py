##Question ID: 1170

def shortest_common_supersequence(str1, str2):
    m, n = len(str1), len(str2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0:
                dp[i][j] = j
            elif j == 0:
                dp[i][j] = i
            elif str1[i - 1] == str2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1])

    i, j = m, n
    result = []

    while i > 0 and j > 0:
        if str1[i - 1] == str2[j - 1]:
            result.append(str1[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            j -= 1
            result.append(str2[j])
        else:
            i -= 1
            result.append(str1[i])

    while i > 0:
        i -= 1
        result.append(str1[i])

    while j > 0:
        j -= 1
        result.append(str2[j])

    return "".join(result[::-1])

## Structure
def shortest_common_supersequence(str1, str2):
    # Your code here

    pass