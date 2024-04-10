##Question ID: 458

def poor_pigs(buckets, minutes_to_die, minutes_to_test):
    pigs = 0
    while (minutes_to_test // minutes_to_die + 1) ** pigs < buckets:
        pigs += 1
    return pigs


## Structure
def poor_pigs(buckets, minutes_to_die, minutes_to_test):
    # Your code here

    pass