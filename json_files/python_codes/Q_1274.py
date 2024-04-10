##Question ID: 1274

from datetime import datetime

def countDaysBetweenDates(date1, date2):
    d1 = datetime.strptime(date1, "%Y-%m-%d")
    d2 = datetime.strptime(date2, "%Y-%m-%d")
    return abs((d2 - d1).days)

## Structure
from datetime import datetime
    # Your code here

    pass