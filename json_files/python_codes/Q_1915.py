##Question ID: 1915

def are_almost_equal(s1, s2):
    diff_count = 0
    first_diff = -1
    second_diff = -1
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            diff_count += 1
            if diff_count == 1:
                first_diff = i
            elif diff_count == 2:
                second_diff = i
            else:
                return False
    return diff_count == 0 or (diff_count == 2 and s1[first_diff] == s2[second_diff] and s1[second_diff] == s2[first_diff])


## Structure
def are_almost_equal(s1, s2):
    # Your code here

    pass