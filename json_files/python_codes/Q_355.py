##Question ID: 355

from collections import defaultdict
from typing import List

class Twitter:

    class Tweet:
        def __init__(self, time, tweetId):
            self.time = time
            self.tweetId = tweetId

    def __init__(self):
        self.tweets = defaultdict(list)
        self.following = defaultdict(set)
        self.timeStamp = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append(self.Tweet(self.timeStamp, tweetId))
        self.timeStamp += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        feed = self.tweets[userId][:]
        for user in self.following[userId]:
            feed.extend(self.tweets[user])

        feed.sort(key=lambda x: x.time, reverse=True)
        return [t.tweetId for t in feed[:10]]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)


## Structure
from collections import defaultdict
    # Your code here

    pass