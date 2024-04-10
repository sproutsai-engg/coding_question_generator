##Question ID: 1002


```javascript
function maxWidthRamp(nums) {
    const indices = [...Array(nums.length).keys()].sort((i, j) => {
        return nums[i] === nums[j] ? i - j : nums[i] - nums[j];
    });
    
    let maxWidth = 0;
    let minIndex = Infinity;
    for (const index of indices) {
        maxWidth = Math.max(maxWidth, index - minIndex);
        minIndex = Math.min(minIndex, index);
    }
    
    return maxWidth;
}
```


## Structure

    # Your code here

    pass