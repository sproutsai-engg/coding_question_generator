##Question ID: 1470

from collections import defaultdict
from typing import List

class TweetCounts:

    def __init__(self):
        self.tweet_records = defaultdict(lambda: defaultdict(int))

    def recordTweet(self, tweetName: str, time: int) -> None:
        self.tweet_records[tweetName][time] += 1

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        if freq == "minute":
            interval = 60
        elif freq == "hour":
            interval = 3600
        else:
            interval = 86400

        result = [0] * ((endTime - startTime) // interval + 1)
        for time, count in self.tweet_records[tweetName].items():
            if startTime <= time <= endTime:
                result[(time - startTime) // interval] += count

        return result


## Structure
from collections import defaultdict
    # Your code here

    pass