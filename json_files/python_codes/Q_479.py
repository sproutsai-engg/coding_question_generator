##Question ID: 479

def largestPalindrome(n):
    if n == 1: 
        return 9
    upper_limit = 10**n - 1
    lower_limit = upper_limit // 10
    for i in range(upper_limit, lower_limit, -1):
        temp = i
        reverse = 0
        while temp != 0:
            reverse = reverse * 10 + temp % 10
            temp //= 10
        palindrome = i * (10**n) + reverse
        for j in range(upper_limit, lower_limit, -1):
            product = palindrome // j
            if palindrome % j == 0 and product <= upper_limit:
                return palindrome % 1337
    return -1

## Structure
def largestPalindrome(n):
    # Your code here

    pass