##Question ID: 32

def longest_valid_parentheses(s: str) -> int:
    n = len(s)
    result = 0
    st = []

    for i in range(n):
        if s[i] == '(':
            st.append(i)
        else:
            if st and s[st[-1]] == '(':
                st.pop()
            else:
                st.append(i)

    if not st:
        result = n
    else:
        right, left = n, 0
        while st:
            left = st.pop()
            result = max(result, right - left - 1)
            right = left
        result = max(result, right)

    return result

## Structure
def longest_valid_parentheses(s: str) -> int:
    # Your code here

    pass