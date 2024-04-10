##Question ID: 872

def splitIntoFibonacci(num):
    ans = []
    def backtrack(index, prev1, prev2):
        if index == len(num):
            return len(ans) >= 3
        curr = 0
        for i in range(index, len(num)):
            if i > index and num[index] == '0':
                break
            curr = curr * 10 + ord(num[i]) - ord('0')
            if curr > 2**31 - 1:
                break
            if len(ans) >= 2:
                if curr < prev1 + prev2:
                    continue
                elif curr > prev1 + prev2:
                    break
            ans.append(curr)
            if backtrack(i + 1, prev2, curr):
                return True
            ans.pop()
        return False
            
    backtrack(0, 0, 0)
    return ans

## Structure
def splitIntoFibonacci(num):
    # Your code here

    pass