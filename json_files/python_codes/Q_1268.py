##Question ID: 1268

def suggestedProducts(products, searchWord):
    result = []
    products.sort()
    
    for i in range(len(searchWord)):
        suggestions = []
        for product in products:
            if len(product) > i and product[i] == searchWord[i]:
                suggestions.append(product)
                if len(suggestions) == 3:
                    break
        result.append(suggestions)
    
    return result


## Structure
def suggestedProducts(products, searchWord):
    # Your code here

    pass