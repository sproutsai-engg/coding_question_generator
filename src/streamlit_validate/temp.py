
from bisect import bisect_left

def max_envelopes(envelopes):
    envelopes.sort(key=lambda x: (x[0], -x[1]))
    dp = []
    
    for _, h in envelopes:
        idx = bisect_left(dp, h)
        if idx == len(dp):
            dp.append(h)
        else:
            dp[idx] = h

    return len(dp)


if __name__ == "__main__":
    envelopes =[[5, 4], [6, 4], [6, 7], [2, 3]]
    result = max_envelopes(envelopes)
