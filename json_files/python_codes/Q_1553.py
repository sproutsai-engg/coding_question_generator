##Question ID: 1553

def countTriplets(arr):
    n = len(arr)
    XOR = [0] * (n + 1)
    
    for i in range(n):
        XOR[i+1] = XOR[i] ^ arr[i]
    
    count = 0
    for i in range(n):
        for k in range(i+1, n):
            if XOR[i] == XOR[k+1]:
                count += k-i
    return count

## Structure
def countTriplets(arr):
    # Your code here

    pass