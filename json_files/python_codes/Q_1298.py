##Question ID: 1298

def reverseParentheses(s: str) -> str:
    st = []
    result = []

    for c in s:
        if c != ')':
            st.append(c)
        else:
            temp = []
            while st and st[-1] != '(':
                temp.append(st.pop())
            if st: st.pop()  # Remove '('
            st.extend(temp)

    result = "".join(st)
    return result


## Structure
def reverseParentheses(s: str) -> str:
    # Your code here

    pass