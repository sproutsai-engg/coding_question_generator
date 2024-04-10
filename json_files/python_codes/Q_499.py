##Question ID: 499

from heapq import heappush, heappop

class Solution:
    def findShortestWay(self, maze: List[List[int]], ball: List[int], hole: List[int]) -> str:
        m, n = len(maze), len(maze[0])
        dist = [[float("inf")] * n for _ in range(m)]
        dirs = ["d", "l", "r", "u"]
        dirs_vector = [[1, 0], [0, -1], [0, 1], [-1, 0]]
        dist[ball[0]][ball[1]] = 0
        pq = [(0, "", ball[0], ball[1])]
        
        while pq:
            cur_dist, cur_path, x, y = heappop(pq)
            if [x, y] == hole:
                return cur_path

            for k, d in enumerate(dirs):
                dist_move, r, c = 0, x + dirs_vector[k][0], y + dirs_vector[k][1]
                while 0 <= r < m and 0 <= c < n and maze[r][c] == 0 and [r, c] != hole:
                    r += dirs_vector[k][0]
                    c += dirs_vector[k][1]
                    dist_move += 1
                r -= dirs_vector[k][0]
                c -= dirs_vector[k][1]
                dist_move -= 1
                
                if dist[x][y] + dist_move < dist[r][c]:
                    dist[r][c] = dist[x][y] + dist_move
                    heappush(pq, (cur_dist + dist_move, cur_path + d, r, c))
        
        return "impossible"

## Structure
from heapq import heappush, heappop
    # Your code here

    pass