##Question ID: 1305

def people_can_see(heights):
    n = len(heights)
    ans = [0] * n
    st = []

    for i in range(n - 1, -1, -1):
        while st and heights[st[-1]] < heights[i]:
            idx = st.pop()
            ans[i] += 1
            ans[i] += ans[idx]
        st.append(i)

    return ans


## Structure
def people_can_see(heights):
    # Your code here

    pass