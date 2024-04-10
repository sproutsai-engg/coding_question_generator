##Question ID: 1081

def videoStitching(clips, time):
    dp = [float('inf')] * (time + 1)
    dp[0] = 0
    for i in range(1, time + 1):
        for clip in clips:
            if clip[0] < i and i <= clip[1]:
                dp[i] = min(dp[i], dp[clip[0]] + 1)
    return -1 if dp[time] == float('inf') else dp[time]

## Structure
def videoStitching(clips, time):
    # Your code here

    pass