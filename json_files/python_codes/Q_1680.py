##Question ID: 1680

def count_routes(locations, start, finish, fuel, curr=None, remaining_fuel=None, memo=None):
    if memo is None:
        memo = {}
     
    if curr is None:
        curr = start
        remaining_fuel = fuel

    if remaining_fuel < 0:
        return 0

    if (curr, remaining_fuel) in memo:
        return memo[(curr, remaining_fuel)]

    ans = 1 if curr == finish else 0
    for next in range(len(locations)):
        if next != curr:
            ans += count_routes(locations, start, finish, fuel, next, remaining_fuel - abs(locations[curr] - locations[next]), memo)
            ans %= 1000000007

    memo[(curr, remaining_fuel)] = ans
    return ans

## Structure
def count_routes(locations, start, finish, fuel, curr=None, remaining_fuel=None, memo=None):
    # Your code here

    pass