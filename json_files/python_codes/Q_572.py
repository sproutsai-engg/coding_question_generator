##Question ID: 572


```javascript
class TreeNode {
    constructor(val, left = null, right = null) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

function isSubtree(root, subRoot) {
    if (root === null) return false;
    if (isIdentical(root, subRoot)) return true;
    return isSubtree(root.left, subRoot) || isSubtree(root.right, subRoot);
}

function isIdentical(n1, n2) {
    if (n1 === null || n2 === null) return n1 === n2;
    if (n1.val !== n2.val) return false;
    return isIdentical(n1.left, n2.left) && isIdentical(n1.right, n2.right);
}
```


## Structure

    # Your code here

    pass