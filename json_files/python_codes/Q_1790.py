##Question ID: 1790

def are_almost_equal(s1, s2):
    if s1 == s2:
        return True
    diff = [i for i in range(len(s1)) if s1[i] != s2[i]]
    return len(diff) == 2 and s1[diff[0]] == s2[diff[1]] and s1[diff[1]] == s2[diff[0]]

## Structure
def are_almost_equal(s1, s2):
    # Your code here

    pass