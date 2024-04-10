##Question ID: 1803

def average_waiting_time(customers):
    wait_time = 0
    curr_time = 0
    
    for arrival, time in customers:
        curr_time = max(curr_time, arrival) + time
        wait_time += curr_time - arrival
    
    return wait_time / len(customers)


## Structure
def average_waiting_time(customers):
    # Your code here

    pass