##Question ID: 563

def findTilt(self, root):
    def findTiltUtil(node):
        if not node: return 0, 0
        
        leftSum, leftTilt = findTiltUtil(node.left)
        rightSum, rightTilt = findTiltUtil(node.right)
    
        return (node.val + leftSum + rightSum, abs(leftSum - rightSum) + leftTilt + rightTilt)

    return findTiltUtil(root)[1]


## Structure
def findTilt(self, root):
    # Your code here

    pass