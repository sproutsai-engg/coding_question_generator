##Question ID: 464

def canIWin(maxChoosableInteger, desiredTotal):
    if maxChoosableInteger >= desiredTotal: return True
    if (maxChoosableInteger * (maxChoosableInteger + 1)) // 2 < desiredTotal: return False

    memo = {}
        
    def canWin(state):
        if state in memo:
            return memo[state]
        for i in range(1, maxChoosableInteger + 1):
            bitCheck = 1 << i
            if (state & bitCheck) == 0:
                if not canWin(state | bitCheck):
                    memo[state] = True
                    return True
    
        memo[state] = False
        return False

    return canWin(0)


## Structure
def canIWin(maxChoosableInteger, desiredTotal):
    # Your code here

    pass