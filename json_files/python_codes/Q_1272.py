##Question ID: 1272

def invalid_transactions(transactions):
    trans_map = {}
    
    for trans in transactions:
        temp = trans.split(",")
        trans_map.setdefault(temp[0], []).append(temp)
    
    ans = []

    for trans in transactions:
        temp = trans.split(",")

        if int(temp[2]) > 1000:
            ans.append(trans)
            continue

        for other in trans_map[temp[0]]:
            if other[3] != temp[3] and abs(int(other[1]) - int(temp[1])) <= 60:
                ans.append(trans)
                break

    return ans


## Structure
def invalid_transactions(transactions):
    # Your code here

    pass