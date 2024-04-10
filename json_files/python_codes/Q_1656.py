##Question ID: 1656

def count_good_triplets(arr, a, b, c):
    count = 0
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if abs(arr[i] - arr[j]) <= a:
                for k in range(j+1, len(arr)):
                    if abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c:
                        count += 1
    return count


## Structure
def count_good_triplets(arr, a, b, c):
    # Your code here

    pass