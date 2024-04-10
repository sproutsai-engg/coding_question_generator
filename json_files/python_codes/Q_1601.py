##Question ID: 1601

def maximumRequests(n, requests):
    req_size = len(requests)
    max_requests = 0

    for i in range(1 << req_size):
        net_transfers = [0] * n
        count = 0
        
        for j in range(req_size):
            if i & (1 << j):
                net_transfers[requests[j][0]] -= 1
                net_transfers[requests[j][1]] += 1
                count += 1

        valid = all(val == 0 for val in net_transfers)

        if valid:
            max_requests = max(max_requests, count)

    return max_requests

## Structure
def maximumRequests(n, requests):
    # Your code here

    pass