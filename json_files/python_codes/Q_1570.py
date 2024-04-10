##Question ID: 1570

def final_prices(prices):
    for i in range(len(prices)):
        for j in range(i + 1, len(prices)):
            if prices[j] <= prices[i]:
                prices[i] -= prices[j]
                break
    return prices

## Structure
def final_prices(prices):
    # Your code here

    pass