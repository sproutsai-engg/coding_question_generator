##Question ID: 1584

def average(salary):
    min_salary = min(salary)
    max_salary = max(salary)
    sum_salaries = sum(salary)
    sum_salaries -= (min_salary + max_salary)
    return sum_salaries / (len(salary) - 2)

## Structure
def average(salary):
    # Your code here

    pass