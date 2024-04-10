##Question ID: 131

def isPalindrome(s, start, end):
    while start < end:
        if s[start] != s[end]:
            return False
        start += 1
        end -= 1
    return True

def dfs(s, start, results, current):
    if start == len(s):
        results.append(current[:])
        return
    
    for end in range(start, len(s)):
        if isPalindrome(s, start, end):
            current.append(s[start:end+1])
            dfs(s, end + 1, results, current)
            current.pop()

def partition(s):
    results = []
    dfs(s, 0, results, [])
    return results

## Structure
def isPalindrome(s, start, end):
    # Your code here

    pass