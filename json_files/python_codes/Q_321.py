##Question ID: 321


```javascript
function maxNumber(nums1, nums2, k) {
    function maxArray(nums, k) {
        let ans = [];
        for (let i = 0; i < nums.length; i++) {
            while (nums.length - i > k - ans.length && ans.length && ans[ans.length - 1] < nums[i])
                ans.pop();
            if (ans.length < k) ans.push(nums[i]);
        }
        return ans;
    }

    function merge(nums1, nums2) {
        let ans = [], i = 0, j = 0;
        while (i < nums1.length || j < nums2.length)
            ans.push((nums1.slice(i).join('') >= nums2.slice(j).join('') ? nums1[i++] : nums2[j++]));
        return ans;
    }

    let result = [];
    for (let i = Math.max(0, k - nums2.length); i <= k && i <= nums1.length; i++) {
        const candidate = merge(maxArray(nums1, i), maxArray(nums2, k - i));
        if (candidate.join('') > result.join('')) result = candidate;
    }
    return result;
}
```


## Structure

    # Your code here

    pass