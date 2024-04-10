##Question ID: 568

def maxVacationDays(flights, days):
    n = len(flights)
    k = len(days[0])
    memo = [[-1] * k for _ in range(n)]

    def dfs(currentWeek, currentCity):
        if currentWeek == k:
            return 0
        if memo[currentCity][currentWeek] != -1:
            return memo[currentCity][currentWeek]

        maxVacation = days[currentCity][currentWeek] + dfs(currentWeek + 1, currentCity)

        for i in range(n):
            if flights[currentCity][i] == 1:
                maxVacation = max(maxVacation, days[i][currentWeek] + dfs(currentWeek + 1, i))

        memo[currentCity][currentWeek] = maxVacation
        return maxVacation

    return dfs(0, 0)


## Structure
def maxVacationDays(flights, days):
    # Your code here

    pass