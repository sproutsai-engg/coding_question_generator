##Question ID: 166

def fraction_to_decimal(numerator, denominator):
    if numerator == 0:
        return "0"
    res = []
    if (numerator > 0) ^ (denominator > 0):
        res.append("-")
    num = abs(numerator)
    den = abs(denominator)
    res.append(str(num // den))
    num %= den
    if num == 0:
        return "".join(res)
    res.append(".")
    map = {}
    while num:
        if num in map:
            res.insert(map[num], "(")
            res.append(")")
            break
        map[num] = len(res)
        num *= 10
        res.append(str(num // den))
        num %= den
    return "".join(res)


## Structure
def fraction_to_decimal(numerator, denominator):
    # Your code here

    pass