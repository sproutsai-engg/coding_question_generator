##Question ID: 1206

def corp_flight_bookings(bookings, n):
    answer = [0] * n
    for start, end, seats in bookings:
        answer[start - 1] += seats
        if end < n:
            answer[end] -= seats
    for i in range(1, n):
        answer[i] += answer[i - 1]
    return answer

## Structure
def corp_flight_bookings(bookings, n):
    # Your code here

    pass