##Question ID: 1868

def findRLEProduct(encoded1, encoded2):
    result = []
    i, j, count1, count2 = 0, 0, 0, 0

    while i < len(encoded1) and j < len(encoded2):
        product = encoded1[i][0] * encoded2[j][0]
        count = min(encoded1[i][1] - count1, encoded2[j][1] - count2)
        count1 += count
        count2 += count

        if result and result[-1][0] == product:
            result[-1][1] += count
        else:
            result.append([product, count])

        if count1 == encoded1[i][1]:
            i += 1
            count1 = 0

        if count2 == encoded2[j][1]:
            j += 1
            count2 = 0

    return result

## Structure
def findRLEProduct(encoded1, encoded2):
    # Your code here

    pass