##Question ID: 1375

def find_kth_palindrome(k, int_length):
    mid = (int_length + 1) // 2
    limit = 10 ** mid - 1

    i = 0
    while i <= limit:
        num = str(i)
        rev = num[::-1]
        if int_length % 2 != 0:
            rev = rev[1:]
        palindrome = int(num + rev)
        if palindrome > 0:
            k -= 1
        if k == 0:
            return palindrome
        i += 1
    return -1

def palindrome_queries(queries, int_length):
    return [find_kth_palindrome(query, int_length) for query in queries]


## Structure
def find_kth_palindrome(k, int_length):
    # Your code here

    pass