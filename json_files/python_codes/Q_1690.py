##Question ID: 1690

def getMaxLen(nums):
    maxLength = currentLen = currentNegLen = 0
    
    for num in nums:
        if num > 0:
            currentLen += 1
            if currentNegLen > 0:
                currentNegLen += 1
        elif num < 0:
            currentLen, currentNegLen = currentNegLen, currentLen + 1
        else:
            currentLen = currentNegLen = 0
        maxLength = max(maxLength, currentLen)
    
    return maxLength

## Structure
def getMaxLen(nums):
    # Your code here

    pass