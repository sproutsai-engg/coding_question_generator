##Question ID: 1118

def number_of_days(year, month):
    if month == 2:
        if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
            return 29
        return 28
    if month in [4, 6, 9, 11]:
        return 30
    return 31

## Structure
def number_of_days(year, month):
    # Your code here

    pass