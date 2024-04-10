##Question ID: 1283

def format_date(date):
    months = {
        "Jan": "01",
        "Feb": "02",
        "Mar": "03",
        "Apr": "04",
        "May": "05",
        "Jun": "06",
        "Jul": "07",
        "Aug": "08",
        "Sep": "09",
        "Oct": "10",
        "Nov": "11",
        "Dec": "12",
    }

    day, month, year = date.split()
    return f"{year}-{months[month]}-{day}"

## Structure
def format_date(date):
    # Your code here

    pass