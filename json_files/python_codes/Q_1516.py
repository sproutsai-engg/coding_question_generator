##Question ID: 1516

def get_happy_string(n, k):
    def dfs(s, prev):
        if len(s) == n:
            happy_strings.append(s)
            return
        for c in 'abc':
            if c != prev:
                dfs(s + c, c)

    happy_strings = []
    dfs("", ' ')
    return happy_strings[k - 1] if k <= len(happy_strings) else ""

## Structure
def get_happy_string(n, k):
    # Your code here

    pass