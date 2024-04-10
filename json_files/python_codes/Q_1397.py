##Question ID: 1397

from bisect import bisect_left

def suggestedProducts(products, searchWord):
    products.sort()
    result = []
    current_prefix = ""
    
    for letter in searchWord:
        current_prefix += letter
        index = bisect_left(products, current_prefix)
        suggestions = []
        
        for i in range(3):
            if index < len(products) and products[index].startswith(current_prefix):
                suggestions.append(products[index])
                index += 1
            else:
                break
        
        result.append(suggestions)
    
    return result

## Structure
from bisect import bisect_left
    # Your code here

    pass