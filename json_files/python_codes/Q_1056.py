##Question ID: 1056


```javascript
function shipWithinDays(weights, days) {
    let left = Math.max(...weights), right = weights.reduce((a, b) => a + b, 0);
    while (left < right) {
        let mid = left + ((right - left) / 2) | 0;
        let day_count = 1, curr_capacity = 0;
        for (const w of weights) {
            curr_capacity += w;
            if (curr_capacity > mid) {
                day_count++;
                curr_capacity = w;
            }
        }
        if (day_count > days) {
            left = mid + 1;
        } else {
            right = mid;
        }
    }
    return left;
}
```

## Structure

    # Your code here

    pass