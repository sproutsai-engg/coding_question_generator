function twoSum(nums, target) {
    const map = new Map();
    for (let i = 0; i < nums.length; i++) {
        const complement = target - nums[i];
        if (map.has(complement)) {
            return [map.get(complement), i];
        }
        map.set(nums[i], i);
    }
    return [];
}


function main() {
    const nums = [3, 2, 4];
    const target = 6;
    const result = twoSum(nums, target);
    console.log(result);
}
main();