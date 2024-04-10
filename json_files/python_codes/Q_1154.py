##Question ID: 1154

def is_leap_year(year: int) -> bool:
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def day_of_year(date: str) -> int:
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    year, month, day = int(date[:4]), int(date[5:7]), int(date[8:])

    if is_leap_year(year):
        days_in_month[1] = 29

    return sum(days_in_month[:month-1]) + day


## Structure
def is_leap_year(year: int) -> bool:
    # Your code here

    pass