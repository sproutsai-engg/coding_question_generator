function findMedianSortedArrays(nums1, nums2) {
    if (nums1.length > nums2.length) {
        return findMedianSortedArrays(nums2, nums1);
    }
    
    const x = nums1.length;
    const y = nums2.length;
    let low = 0;
    let high = x;
    
    while (low <= high) {
        const partitionX = Math.floor((low + high) / 2);
        const partitionY = Math.floor((x + y + 1) / 2) - partitionX;
        
        const maxLeftX = (partitionX === 0) ? Number.NEGATIVE_INFINITY : nums1[partitionX - 1];
        const minRightX = (partitionX === x) ? Number.POSITIVE_INFINITY : nums1[partitionX];
        
        const maxLeftY = (partitionY === 0) ? Number.NEGATIVE_INFINITY : nums2[partitionY - 1];
        const minRightY = (partitionY === y) ? Number.POSITIVE_INFINITY : nums2[partitionY];
        
        if (maxLeftX <= minRightY && maxLeftY <= minRightX) {
            if ((x + y) % 2 === 0) {
                return (Math.max(maxLeftX, maxLeftY) + Math.min(minRightX, minRightY)) / 2;
            } else {
                return Math.max(maxLeftX, maxLeftY);
            }
        } else if (maxLeftX > minRightY) {
            high = partitionX - 1;
        } else {
            low = partitionX + 1;
        }
    }    
    return 0;
}



function main(){
    const inputs = $args;
    const nums1 = inputs[0];
    const nums2 = inputs[1];
    const result = findMedianSortedArrays(nums1, nums2);
    console.log(result);
}
main();