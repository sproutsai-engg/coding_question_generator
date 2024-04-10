##Question ID: 332

from collections import defaultdict

def findItinerary(tickets):
    flights = defaultdict(list)
    itinerary = []

    for ticket in tickets:
        flights[ticket[0]].append(ticket[1])
        flights[ticket[0]].sort(reverse=True)

    def dfs(airport):
        while flights[airport]:
            dfs(flights[airport].pop())
        itinerary.append(airport)

    dfs("JFK")
    
    return itinerary[::-1]

## Structure
from collections import defaultdict
    # Your code here

    pass