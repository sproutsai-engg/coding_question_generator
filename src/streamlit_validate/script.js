function maxArea(height) {
    let max_area = 0, left = 0, right = height.length - 1;
    while (left < right) {
        max_area = Math.max(max_area, Math.min(height[left], height[right]) * (right - left));
        if (height[left] < height[right]) {
            left++;
        } else {
            right--;
        }
    }
    return max_area;
}


function main() {
    const height = [1, 2, 1];
    const result = maxArea(height);
    console.log("$sprouts@pankaj",result,"$sprouts@pankaj");
}
main();