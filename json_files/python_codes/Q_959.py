##Question ID: 959

def threeSumMulti(arr, target):
    MOD = 1000000007
    ans = 0

    arr.sort()
    n = len(arr)

    for i in range(n - 2):
        j, k = i + 1, n - 1
        while j < k:
            s = arr[i] + arr[j] + arr[k]
            if s > target:
                k -= 1
            elif s < target:
                j += 1
            else:
                if arr[j] != arr[k]:
                    left_count = right_count = 1

                    while j < n - 1 and arr[j] == arr[j + 1]:
                        left_count += 1
                        j += 1

                    while k > 0 and arr[k] == arr[k - 1]:
                        right_count += 1
                        k -= 1

                    ans += left_count * right_count
                    ans %= MOD
                    j += 1
                    k -= 1
                else:
                    ans += (k - j + 1) * (k - j) // 2
                    ans %= MOD
                    break

    return ans

## Structure
def threeSumMulti(arr, target):
    # Your code here

    pass