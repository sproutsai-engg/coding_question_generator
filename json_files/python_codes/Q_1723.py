##Question ID: 1723

def max_achievable_requests(n, requests, idx=0, counts=None):
    if counts is None:
        counts = [0] * n
    if idx == len(requests):
        if all(count == 0 for count in counts):
            return 0
        return 0

    ignored = max_achievable_requests(n, requests, idx+1, counts[:])
    counts[requests[idx][0]] += 1
    counts[requests[idx][1]] -= 1

    accepted = 1 + max_achievable_requests(n, requests, idx+1, counts)

    return max(ignored, accepted)

## Structure
def max_achievable_requests(n, requests, idx=0, counts=None):
    # Your code here

    pass