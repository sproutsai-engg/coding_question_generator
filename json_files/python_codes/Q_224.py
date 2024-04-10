##Question ID: 224

def calculate(s: str) -> int:
    result = 0
    sign = 1
    num = 0
    st = []
    for c in s:
        if c.isdigit():
            num = num * 10 + int(c)
        else:
            result += sign * num
            num = 0
            if c == '+':
                sign = 1
            elif c == '-':
                sign = -1
            elif c == '(':
                st.append(result)
                st.append(sign)
                result = 0
                sign = 1
            elif c == ')':
                prev_sign = st.pop()
                prev_result = st.pop()
                result = prev_result + prev_sign * result
    result += sign * num
    return result

## Structure
def calculate(s: str) -> int:
    # Your code here

    pass