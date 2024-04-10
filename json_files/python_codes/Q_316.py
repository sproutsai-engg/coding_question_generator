##Question ID: 316

def removeDuplicateLetters(s):
    count = [0] * 256
    visited = [False] * 256
    st = []

    for ch in s:
        count[ord(ch)] += 1

    for ch in s:
        count[ord(ch)] -= 1
        if visited[ord(ch)]:
            continue
        while st and ch < st[-1] and count[ord(st[-1])] > 0:
            visited[ord(st.pop())] = False
        st.append(ch)
        visited[ord(ch)] = True

    return "".join(st)   

## Structure
def removeDuplicateLetters(s):
    # Your code here

    pass