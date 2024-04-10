##Question ID: 1146

def gcd_of_strings(str1: str, str2: str) -> str:
    if str1 + str2 != str2 + str1:
        return ''
    gcd = lambda a, b: a if not b else gcd(b, a % b)
    return str1[:gcd(len(str1), len(str2))]


## Structure
def gcd_of_strings(str1: str, str2: str) -> str:
    # Your code here

    pass