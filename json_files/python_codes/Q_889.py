##Question ID: 889

def are_almost_equal(s, goal):
    if s == goal:
        return True
    count = 0
    index1, index2 = -1, -1
    for i in range(len(s)):
        if s[i] != goal[i]:
            count += 1
            if index1 == -1:
                index1 = i
            else:
                index2 = i
            if count > 2:
                return False
    return count == 2 and s[index1] == goal[index2] and s[index2] == goal[index1]

## Structure
def are_almost_equal(s, goal):
    # Your code here

    pass