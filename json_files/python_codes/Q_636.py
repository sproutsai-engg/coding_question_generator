##Question ID: 636

def exclusiveTime(n, logs):
    res = [0] * n
    stack = []
    prev_time = 0

    for log in logs:
        parts = log.split(':')
        id = int(parts[0])
        type = parts[1]
        time = int(parts[2])

        if type == "start":
            if stack:
                res[stack[-1]] += time - prev_time
            stack.append(id)
            prev_time = time
        else:
            res[stack.pop()] += time - prev_time + 1
            prev_time = time + 1

    return res

## Structure
def exclusiveTime(n, logs):
    # Your code here

    pass