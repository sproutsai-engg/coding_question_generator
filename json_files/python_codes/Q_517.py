##Question ID: 517

def find_min_moves(machines):
    n = len(machines)
    total_dresses = sum(machines)
    if total_dresses % n != 0:
        return -1
    average = total_dresses // n
    moves = 0
    imbalance = 0
    
    for i in range(n):
        imbalance += machines[i] - average
        moves = max(moves, abs(imbalance), machines[i] - average)
        
    return moves

## Structure
def find_min_moves(machines):
    # Your code here

    pass