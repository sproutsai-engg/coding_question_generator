##Question ID: 1177

def canMakePaliQueries(s, queries):
    answer = []
    prefixSum = [0] * (len(s) + 1)

    for i in range(len(s)):
        prefixSum[i + 1] = prefixSum[i] ^ (1 << (ord(s[i]) - ord('a')))

    for query in queries:
        left, right, k = query
        diffCount = bin(prefixSum[right + 1] ^ prefixSum[left]).count('1')
        answer.append((diffCount // 2) <= k)

    return answer


## Structure
def canMakePaliQueries(s, queries):
    # Your code here

    pass