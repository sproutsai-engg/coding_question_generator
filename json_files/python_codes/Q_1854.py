##Question ID: 1854

def maxAliveYear(logs):
    years = [0] * 101
    for log in logs:
        years[log[0] - 1950] += 1
        years[log[1] - 1950] -= 1
    max_population = years[0]
    max_year = 1950
    for i in range(1, 101):
        years[i] += years[i - 1]
        if years[i] > max_population:
            max_population = years[i]
            max_year = i + 1950
    return max_year

## Structure
def maxAliveYear(logs):
    # Your code here

    pass