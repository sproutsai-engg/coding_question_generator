##Question ID: 57

from typing import List

def insert(intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    result = []
    start_pos = 0

    while start_pos < len(intervals) and intervals[start_pos][1] < newInterval[0]:
        result.append(intervals[start_pos])
        start_pos += 1

    while start_pos < len(intervals) and intervals[start_pos][0] <= newInterval[1]:
        newInterval[0] = min(newInterval[0], intervals[start_pos][0])
        newInterval[1] = max(newInterval[1], intervals[start_pos][1])
        start_pos += 1

    result.append(newInterval)

    while start_pos < len(intervals):
        result.append(intervals[start_pos])
        start_pos += 1

    return result

## Structure
from typing import List
    # Your code here

    pass