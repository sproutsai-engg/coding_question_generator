##Question ID: 1657

def get_winner(arr, k):
    winner = arr[0]
    consecutive_wins = 0

    for i in range(1, len(arr)):
        if arr[i] > winner:
            winner = arr[i];
            consecutive_wins = 0

        consecutive_wins += 1
        if consecutive_wins == k:
            break

    return winner

## Structure
def get_winner(arr, k):
    # Your code here

    pass