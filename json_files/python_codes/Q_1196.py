##Question ID: 1196

def minHeightShelves(books, shelfWidth):
    n = len(books)
    dp = [1000000] * (n + 1)
    dp[0] = 0
    
    for i in range(1, n + 1):
        width = 0
        height = 0
        j = i
        while j >= 1:
            width += books[j - 1][0]
            height = max(height, books[j - 1][1])
            
            if width <= shelfWidth:
                dp[i] = min(dp[i], dp[j - 1] + height)
            j -= 1
    
    return dp[n]

## Structure
def minHeightShelves(books, shelfWidth):
    # Your code here

    pass