##Question ID: 1051

def height_checker(heights):
    expected = sorted(heights)
    
    count = 0
    for i in range(len(heights)):
        if heights[i] != expected[i]:
            count += 1
            
    return count

## Structure
def height_checker(heights):
    # Your code here

    pass