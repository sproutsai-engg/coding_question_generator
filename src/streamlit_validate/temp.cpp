#include <iostream>
#include <vector>
#include <algorithm> 
using namespace std;

int maxArea(vector<int>& height) {
    int max_area = 0, left = 0, right = height.size() - 1;
    while (left < right) {
        max_area = max(max_area, min(height[left], height[right]) * (right - left));
        if (height[left] < height[right]) {
            left++;
        } else {
            right--;
        }
    }
    return max_area;
}


#include <iostream>
#include <vector>
#include <algorithm> 
using namespace std;

int main() {
    vector<int> height = {1, 8, 6, 2, 5, 4, 8, 3, 7};
    int result = maxArea(height);
    cout << result << endl;
    return 0;
}