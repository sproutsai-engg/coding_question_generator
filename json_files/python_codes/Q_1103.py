##Question ID: 1103

def distribute_candies(candies, num_people):
    result = [0] * num_people
    i = 0
    count = 1

    while candies > 0:
        result[i % num_people] += min(candies, count)
        candies -= count
        count += 1
        i += 1

    return result


## Structure
def distribute_candies(candies, num_people):
    # Your code here

    pass