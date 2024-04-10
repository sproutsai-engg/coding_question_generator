##Question ID: 947

from collections import defaultdict
from bisect import bisect

class TopVotedCandidate:

    def __init__(self, persons, times):
        self.leader_map = {}
        self.times = times
        votes = defaultdict(int)
        leader = -1
        for i, t in enumerate(times):
            votes[persons[i]] += 1
            if votes[persons[i]] >= votes[leader]:
                leader = persons[i]
            self.leader_map[t] = leader

    def q(self, t):
        idx = bisect.bisect(self.times, t)
        return self.times[idx - 1]

## Structure
from collections import defaultdict
    # Your code here

    pass