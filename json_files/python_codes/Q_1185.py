##Question ID: 1185

def day_of_the_week(day, month, year):
    from datetime import date
    days = ["Sunday ", "Monday ", "Tuesday ", "Wednesday ", "Thursday ", "Friday ", "Saturday "]
    return days[date(year, month, day).weekday()]

## Structure
def day_of_the_week(day, month, year):
    # Your code here

    pass