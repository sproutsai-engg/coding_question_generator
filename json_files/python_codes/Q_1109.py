##Question ID: 1109

def corpFlightBookings(bookings, n):
    seats = [0] * n
    for booking in bookings:
        seats[booking[0] - 1] += booking[2]
        if booking[1] < n:
            seats[booking[1]] -= booking[2]
    for i in range(1, n):
        seats[i] += seats[i - 1]
    return seats

## Structure
def corpFlightBookings(bookings, n):
    # Your code here

    pass