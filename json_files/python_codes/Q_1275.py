##Question ID: 1275

def validateBinaryTreeNodes(n, leftChild, rightChild):
    parent = [-1] * n
    for i in range(n):
        if leftChild[i] != -1:
            if parent[leftChild[i]] != -1:
                return False
            parent[leftChild[i]] = i
        if rightChild[i] != -1:
            if parent[rightChild[i]] != -1:
                return False
            parent[rightChild[i]] = i
    
    root = -1
    for i in range(n):
        if parent[i] == -1:
            if root != -1:
                return False
            root = i

    return root != -1

## Structure
def validateBinaryTreeNodes(n, leftChild, rightChild):
    # Your code here

    pass