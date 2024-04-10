##Question ID: 1898

def maximumRemovals(s: str, p: str, removable: List[int]) -> int:
    low, high = 0, len(removable)
    while low < high:
        mid = (low + high + 1) // 2
        temp_s = list(s)
        for i in range(mid):
            temp_s[removable[i]] = '-'
        i, j = 0, 0
        while i < len(temp_s) and j < len(p):
            if temp_s[i] == p[j]:
                j += 1
            i += 1
        if j == len(p):
            low = mid
        else:
            high = mid - 1
    return low


## Structure
def maximumRemovals(s: str, p: str, removable: List[int]) -> int:
    # Your code here

    pass