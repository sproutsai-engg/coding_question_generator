##Question ID: 1281

def can_make_pali_queries(s, queries):
    result = []
    for left, right, k in queries:
        count = [0] * 26
        for i in range(left, right + 1):
            count[ord(s[i]) - ord('a')] += 1
        odd_count = sum(c % 2 for c in count)
        result.append(odd_count // 2 <= k)
    return result

## Structure
def can_make_pali_queries(s, queries):
    # Your code here

    pass