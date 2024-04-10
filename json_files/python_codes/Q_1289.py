##Question ID: 1289

def day_of_the_week(day, month, year):
    days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    if month < 3:
        month += 12
        year -= 1
    k = year % 100
    j = year // 100
    day_of_week = (day + 13 * (month + 1) // 5 + k + k // 4 + 5 * j + j // 4) % 7
    return days[day_of_week]

## Structure
def day_of_the_week(day, month, year):
    # Your code here

    pass