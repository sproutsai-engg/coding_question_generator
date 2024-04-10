##Question ID: 1436

from collections import deque
from collections import defaultdict

def watched_videos_by_friends(watched_videos, friends, id, level):
    visited = set()
    q = deque([(id, 0)])
    video_freq = defaultdict(int)

    while q:
        current_id, current_level = q.popleft()

        if current_level == level:
            for video in watched_videos[current_id]:
                video_freq[video] += 1
        elif current_level < level:
            for friend_id in friends[current_id]:
                if friend_id not in visited:
                    visited.add(friend_id)
                    q.append((friend_id, current_level + 1))

    result = sorted(video_freq.keys(), key=lambda x: (video_freq[x], x))

    return result

## Structure
from collections import deque
    # Your code here

    pass