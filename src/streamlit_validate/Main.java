public int maxArea(int[] height) {
    int max_area = 0, left = 0, right = height.length - 1;
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


public static void main(String[] args) {
    int[] height = $args;
    int result = maxArea(height);
    System.out.println(result);
}