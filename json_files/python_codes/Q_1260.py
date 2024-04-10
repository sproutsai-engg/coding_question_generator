##Question ID: 1260

def dayOfYear(date: str) -> int:
    year, month, day = map(int, date.split('-'))

    daysInMonth = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        daysInMonth[2] = 29

    dayOfYear = sum(daysInMonth[:month]) + day
    return dayOfYear

## Structure
def dayOfYear(date: str) -> int:
    # Your code here

    pass