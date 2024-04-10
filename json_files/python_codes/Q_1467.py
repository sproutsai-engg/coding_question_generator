##Question ID: 1467

from math import factorial

def count_combinations(balls, combinations, curr_ball):
    total_combinations = 1
    for i in range(curr_ball):
        total_combinations *= factorial(balls[i] + combinations[i]) / (factorial(balls[i]) * factorial(combinations[i]))

    return total_combinations

def dfs(balls, combinations, curr_ball):
    if curr_ball == len(balls):
        if combinations[-1] == combinations[0]:
            return count_combinations(balls, combinations, curr_ball)
        else:
            return 0

    result = 0
    for i in range(balls[curr_ball] + 1):
        combinations.append(i)
        result += dfs(balls, combinations, curr_ball + 1)
        combinations.pop()

    return result

def get_probability(balls):
    sum_balls = sum(balls)

    total_combinations = 1
    for ball in balls:
        total_combinations *= factorial(ball)

    combinations = []
    return dfs(balls, combinations, 0) / total_combinations

## Structure
from math import factorial
    # Your code here

    pass