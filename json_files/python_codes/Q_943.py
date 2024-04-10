##Question ID: 943

def sum_of_mins(arr):
    mod = 10**9 + 7
    n = len(arr)
    left, right = [0] * n, [0] * n
    st = []

    for i in range(n):
        while st and arr[st[-1]] > arr[i]:
            st.pop()
        left[i] = st[-1] if st else -1
        st.append(i)

    st.clear()
    for i in range(n - 1, -1, -1):
        while st and arr[st[-1]] > arr[i]:
            st.pop()
        right[i] = st[-1] if st else n
        st.append(i)

    ans = 0
    for i in range(n):
        ans = (ans + arr[i] * (i - left[i]) * (right[i] - i)) % mod
    return ans

## Structure
def sum_of_mins(arr):
    # Your code here

    pass