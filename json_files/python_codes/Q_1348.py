##Question ID: 1348

from collections import defaultdict
from typing import List

class TweetCounts:

    def __init__(self):
        self.data = defaultdict(dict)

    def recordTweet(self, tweetName: str, time: int) -> None:
        if time not in self.data[tweetName]:
            self.data[tweetName][time] = 1
        else:
            self.data[tweetName][time] += 1

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        step = 60 if freq == "minute" else 3600 if freq == "hour" else 86400
        chunks = [0] * ((endTime - startTime) // step + 1)

        if tweetName in self.data:
            for time, count in self.data[tweetName].items():
                chunk_index = (time - startTime) // step
                if 0 <= chunk_index < len(chunks):
                    chunks[chunk_index] += count

        return chunks

## Structure
from collections import defaultdict
    # Your code here

    pass