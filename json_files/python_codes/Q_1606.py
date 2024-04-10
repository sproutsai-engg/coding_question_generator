##Question ID: 1606

def busiestServers(k, arrival, load):
    server_status = [-1] * k
    server_request_count = [0] * k

    for i in range(len(arrival)):
        index = i % k
        for _ in range(k):
            if server_status[index] <= arrival[i]:
                server_status[index] = arrival[i] + load[i]
                server_request_count[index] += 1
                break
            index = (index + 1) % k

    max_requests = max(server_request_count)
    return [i for i in range(k) if server_request_count[i] == max_requests]

## Structure
def busiestServers(k, arrival, load):
    # Your code here

    pass