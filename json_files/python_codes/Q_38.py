##Question ID: 38

def count_and_say(n):
    if n == 1:
        return "1"
    previous = count_and_say(n - 1)
    result = []
    count = 1
    for i in range(1, len(previous)):
        if previous[i] == previous[i - 1]:
            count += 1
        else:
            result.append(str(count))
            result.append(previous[i - 1])
            count = 1
    result.append(str(count))
    result.append(previous[-1])
    return "".join(result)

## Structure
def count_and_say(n):
    # Your code here

    pass