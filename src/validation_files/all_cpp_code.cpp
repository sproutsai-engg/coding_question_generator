//Validating for ques 1
#include <vector>
#include <unordered_map>

std::vector<int> twoSum(std::vector<int>& nums, int target) {
    std::unordered_map<int, int> map;
    for (int i = 0; i < nums.size(); i++) {
        int complement = target - nums[i];
        if (map.find(complement) != map.end()) {
            return {map[complement], i};
        }
        map[nums[i]] = i;
    }
    return {};
}

#include <vector>
#include <unordered_map>

std::vector<int> twoSum(std::vector<int>& nums, int target) 
    // Your code here
}

#include <vector>
#include <unordered_map>
#include <iostream>

int main() {
    std::vector<int> nums = $args;
    int target = $args;
    std::vector<int> result = twoSum(nums, target);
    for (int i : result) {
        std::cout << i << " ";
    }
    std::cout << std::endl;
    return 0;
}

 //******************************************************** 

//Validating for ques 3
#include <string>
#include <unordered_set>

int lengthOfLongestSubstring(std::string s) {
    int left = 0, right = 0, maxLength = 0;
    std::unordered_set<char> characters;

    while (right < s.size()) {
        if (characters.find(s[right]) == characters.end()) {
            characters.insert(s[right]);
            maxLength = std::max(maxLength, right - left + 1);
            right++;
        } else {
            characters.erase(s[left]);
            left++;
        }
    }

    return maxLength;
}

#include <string>
#include <unordered_set>

int lengthOfLongestSubstring(std::string s) 
    // Your code here
}

#include <string>
#include <unordered_set>
#include <iostream>

int main() {
    std::string s = $args;
    int result = lengthOfLongestSubstring(s);
    std::cout << result << std::endl;
    return 0;
}

 //******************************************************** 

//Validating for ques 4
double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
    if (nums1.size() > nums2.size()) {
        return findMedianSortedArrays(nums2, nums1);
    }
    
    int x = nums1.size();
    int y = nums2.size();
    int low = 0;
    int high = x;
    
    while (low <= high) {
        int partitionX = (low + high) / 2;
        int partitionY = (x + y + 1) / 2 - partitionX;
        
        int maxLeftX = (partitionX == 0) ? INT_MIN : nums1[partitionX - 1];
        int minRightX = (partitionX == x) ? INT_MAX : nums1[partitionX];
        
        int maxLeftY = (partitionY == 0) ? INT_MIN : nums2[partitionY - 1];
        int minRightY = (partitionY == y) ? INT_MAX : nums2[partitionY];
        
        if (maxLeftX <= minRightY && maxLeftY <= minRightX) {
            if ((x + y) % 2 == 0) {
                return (double(max(maxLeftX, maxLeftY) + min(minRightX, minRightY))) / 2;
            } else {
                return double(max(maxLeftX, maxLeftY));
            }
        } else if (maxLeftX > minRightY) {
            high = partitionX - 1;
        } else {
            low = partitionX + 1;
        }
    }    
    return 0;
}

double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) 
    // Your code here
}

double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
    if (nums1.size() > nums2.size()) {
        return findMedianSortedArrays(nums2, nums1);
    }
    
    int x = nums1.size();
    int y = nums2.size();
    int low = 0;
    int high = x;
    
    while (low <= high) {
        int partitionX = (low + high) / 2;
        int partitionY = (x + y + 1) / 2 - partitionX;
        
        int maxLeftX = (partitionX == 0) ? INT_MIN : nums1[partitionX - 1];
        int minRightX = (partitionX == x) ? INT_MAX : nums1[partitionX];
        
        int maxLeftY = (partitionY == 0) ? INT_MIN : nums2[partitionY - 1];
        int minRightY = (partitionY == y) ? INT_MAX : nums2[partitionY];
        
        if (maxLeftX <= minRightY && maxLeftY <= minRightX) {
            if ((x + y) % 2 == 0) {
                return (double(max(maxLeftX, maxLeftY) + min(minRightX, minRightY))) / 2;
            } else {
                return double(max(maxLeftX, maxLeftY));
            }
        } else if (maxLeftX > minRightY) {
            high = partitionX - 1;
        } else {
            low = partitionX + 1;
        }
    }    
    return 0;
}

 //******************************************************** 

//Validating for ques 5
#include <string>

std::string longestPalindromicSubstring(std::string s) {
  int n = s.size();
  if (n == 0) return "";
  int start = 0, maxLength = 1;

  for (int i = 0; i < n; ++i) {
    int l = i, r = i;

    while (r < n - 1 && s[r] == s[r + 1])
      r++;
    i = r;

    while (l > 0 && r < n - 1 && s[l - 1] == s[r + 1]) {
      l--;
      r++;
    }

    int length = r - l + 1;
    if (length > maxLength) {
      start = l;
      maxLength = length;
    }
  }

  return s.substr(start, maxLength);
}

#include <string>

std::string longestPalindromicSubstring(std::string s) 
    // Your code here
}

#include <string>

int main() {
  std::string s = $args;
  std::string result = longestPalindromicSubstring(s);
  std::cout << result << std::endl;
  return 0;
}

 //******************************************************** 

//Validating for ques 7
int reverse(int x) {
    long long res = 0;
    while (x != 0) {
        res = res * 10 + x % 10;
        x /= 10;
    }
    return (res < INT_MIN || res > INT_MAX) ? 0 : res;
}

int reverse(int x) 
    // Your code here
}

int main() {
    int x = $args;
    int result = reverse(x);
    cout << result << endl;
    return 0;
}

 //******************************************************** 

//Validating for ques 9
bool isPalindrome(int x) {
    if (x < 0) return false;
    int original = x, reversed = 0;
    while (x > 0) {
        reversed = reversed * 10 + x % 10;
        x /= 10;
    }
    return original == reversed;
}


bool isPalindrome(int x) 
    // Your code here
}


int main() {
    int x = $args;
    bool result = isPalindrome(x);
    cout << boolalpha << result << endl;
    return 0;
}

 //******************************************************** 

//Validating for ques 10
bool isMatch(std::string s, std::string p) {
    int m = s.length(), n = p.length();
    std::vector<std::vector<bool>> dp(m + 1, std::vector<bool>(n + 1, false));
    dp[0][0] = true;

    for (int j = 1; j <= n; j++) {
        if (p[j - 1] == '*' && dp[0][j - 2]) {
            dp[0][j] = true;
        }
    }

    for (int i = 1; i <= m; i++) {
        for (int j = 1; j <= n; j++) {
            if (p[j - 1] == s[i - 1] || p[j - 1] == '.') {
                dp[i][j] = dp[i - 1][j - 1];
            } else if (p[j - 1] == '*') {
                dp[i][j] = dp[i][j - 2] || (dp[i - 1][j] && (s[i - 1] == p[j - 2] || p[j - 2] == '.'));
            }
        }
    }

    return dp[m][n];
}

bool isMatch(std::string s, std::string p) 
    // Your code here
}

bool isMatch(std::string s, std::string p) {
    int m = s.length(), n = p.length();
    std::vector<std::vector<bool>> dp(m + 1, std::vector<bool>(n + 1, false));
    dp[0][0] = true;

    for (int j = 1; j <= n; j++) {
        if (p[j - 1] == '*' && dp[0][j - 2]) {
            dp[0][j] = true;
        }
    }

    for (int i = 1; i <= m; i++) {
        for (int j = 1; j <= n; j++) {
            if (p[j - 1] == s[i - 1] || p[j - 1] == '.') {
                dp[i][j] = dp[i - 1][j - 1];
            } else if (p[j - 1] == '*') {
                dp[i][j] = dp[i][j - 2] || (dp[i - 1][j] && (s[i - 1] == p[j - 2] || p[j - 2] == '.'));
            }
        }
    }

    return dp[m][n];
}

 //******************************************************** 

//Validating for ques 11
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

int maxArea(vector<int>& height) 
    // Your code here
}

int main() {
    vector<int> height = $args;
    int result = maxArea(height);
    cout << result << endl;
    return 0;
}

 //******************************************************** 

//Validating for ques 6
#include <string>
#include <vector>

std::string convert(std::string s, int numRows) {
    if (numRows == 1 || numRows >= s.size()) return s;

    std::vector<std::string> rows(std::min(numRows, int(s.size())));
    int curRow = 0;
    bool goingDown = false;

    for (char c : s) {
        rows[curRow] += c;
        if (curRow == 0 || curRow == numRows - 1) goingDown = !goingDown;
        curRow += goingDown ? 1 : -1;
    }

    std::string result;
    for (std::string row : rows) result += row;
    return result;
}

#include <string>
#include <vector>

std::string convert(std::string s, int numRows) 
    // Your code here
}

#include <string>
#include <vector>

int main() {
    std::string s = $args;
    int numRows = 3;
    std::string result = convert(s, numRows);
    std::cout << result << std::endl;
    return 0;
}

 //******************************************************** 

//Validating for ques 8
int myAtoi(string s) {
    long result = 0;
    int i = 0, sign = 1;
    while (s[i] == ' ') i++;
    if (s[i] == '-' || s[i] == '+') sign = (s[i++] == '+') ? 1 : -1;
    while (isdigit(s[i])) {
        result = result * 10 + (s[i++] - '0');
        if (result * sign > INT_MAX) return INT_MAX;
        if (result * sign < INT_MIN) return INT_MIN;
    }
    return result * sign;
}

int myAtoi(string s) 
    // Your code here
}

int myAtoi(string s) {
    long result = 0;
    int i = 0, sign = 1;
    while (s[i] == ' ') i++;
    if (s[i] == '-' || s[i] == '+') sign = (s[i++] == '+') ? 1 : -1;
    while (isdigit(s[i])) {
        result = result * 10 + (s[i++] - '0');
        if (result * sign > INT_MAX) return INT_MAX;
        if (result * sign < INT_MIN) return INT_MIN;
    }
    return result * sign;
}

 //******************************************************** 

//Validating for ques 12
#include <vector>
#include <string>

std::string intToRoman(int num) {
    std::vector<std::pair<int, std::string>> romans = {
        {1000, "M"},
        {900, "CM"},
        {500, "D"},
        {400, "CD"},
        {100, "C"},
        {90, "XC"},
        {50, "L"},
        {40, "XL"},
        {10, "X"},
        {9, "IX"},
        {5, "V"},
        {4, "IV"},
        {1, "I"}
    };
    std::string roman = "";
    for (const auto& p : romans) {
        while (num >= p.first) {
            roman += p.second;
            num -= p.first;
        }
    }
    return roman;
}

#include <vector>
#include <string>

std::string intToRoman(int num) 
    // Your code here
}

#include <iostream>
using namespace std;

int main() {
    int num = $args;
    string result = intToRoman(num);
    cout << result << endl;
    return 0;
}

 //******************************************************** 

//Validating for ques 13
int romanToInt(string s) {
    unordered_map<char, int> roman_values = { {'I', 1}, {'V', 5}, {'X', 10}, {'L', 50}, {'C', 100}, {'D', 500}, {'M', 1000} };
    int total = 0;
    int prev_value = 0;

    for (char c : s) {
        int current_value = roman_values[c];
        if (current_value > prev_value)
            total += current_value - (2 * prev_value);
        else
            total += current_value;
        prev_value = current_value;
    }

    return total;
}


int romanToInt(string s) 
    // Your code here
}


int main() {
    string s = $args;
    int result = romanToInt(s);
    cout << result << endl;
    return 0;
}

 //******************************************************** 

//Validating for ques 14
#include <vector>
#include <string>
using namespace std;

string longestCommonPrefix(vector<string>& strs) {
    if (strs.empty()) return "";

    for (int i = 0; i < strs[0].size(); ++i) {
        char c = strs[0][i];
        for (int j = 1; j < strs.size(); ++j) {
            if (i == strs[j].size() || strs[j][i] != c) {
                return strs[0].substr(0, i);
            }
        }
    }
    return strs[0];
}

#include <vector>
#include <string>
using namespace std;

string longestCommonPrefix(vector<string>& strs) 
    // Your code here
}

#include <vector>
#include <string>
using namespace std;

string longestCommonPrefix(vector<string>& strs) {
    if (strs.empty()) return "";

    for (int i = 0; i < strs[0].size(); ++i) {
        char c = strs[0][i];
        for (int j = 1; j < strs.size(); ++j) {
            if (i == strs[j].size() || strs[j][i] != c) {
                return strs[0].substr(0, i);
            }
        }
    }
    return strs[0];
}

int main() {
    vector<string> strs = $args;
    string result = longestCommonPrefix(strs);
    cout << result << endl;
    return 0;
}

 //******************************************************** 

//Validating for ques 15
#include <vector>
#include <algorithm>

std::vector<std::vector<int>> threeSum(std::vector<int>& nums) {
    std::vector<std::vector<int>> result;
    std::sort(nums.begin(), nums.end());

    for (int i = 0; i < (int)nums.size() - 2; ++i) {
        if (i == 0 || nums[i] != nums[i - 1]) {
            int j = i + 1, k = nums.size() - 1;
            while (j < k) {
                int sum = nums[i] + nums[j] + nums[k];
                if (sum == 0) {
                    result.push_back({nums[i], nums[j], nums[k]});
                    while (j < k && nums[j] == nums[j + 1]) ++j;
                    while (j < k && nums[k] == nums[k - 1]) --k;
                    ++j;
                    --k;
                } else if (sum < 0) {
                    ++j;
                } else {
                    --k;
                }
            }
        }
    }

    return result;
}

#include <vector>
#include <algorithm>

std::vector<std::vector<int>> threeSum(std::vector<int>& nums) 
    // Your code here
}

#include <vector>
#include <algorithm>
#include <iostream>

std::vector<std::vector<int>> threeSum(std::vector<int>& nums);

int main() {
    std::vector<int> nums = $args;
    std::vector<std::vector<int>> result = threeSum(nums);

    for (const auto& triplet : result) {
        for (const auto& num : triplet) {
            std::cout << num << " ";
        }
        std::cout << std::endl;
    }

    return 0;
}

std::vector<std::vector<int>> threeSum(std::vector<int>& nums) {
    std::vector<std::vector<int>> result;
    std::sort(nums.begin(), nums.end());

    for (int i = 0; i < (int)nums.size() - 2; ++i) {
        if (i == 0 || nums[i] != nums[i - 1]) {
            int j = i + 1, k = nums.size() - 1;
            while (j < k) {
                int sum = nums[i] + nums[j] + nums[k];
                if (sum == 0) {
                    result.push_back({nums[i], nums[j], nums[k]});
                    while (j < k && nums[j] == nums[j + 1]) ++j;
                    while (j < k && nums[k] == nums[k - 1]) --k;
                    ++j;
                    --k;
                } else if (sum < 0) {
                    ++j;
                } else {
                    --k;
                }
            }
        }
    }

    return result;
}

 //******************************************************** 

//Validating for ques 16
#include <algorithm>
#include <vector>

int threeSumClosest(std::vector<int>& nums, int target) {
    std::sort(nums.begin(), nums.end());
    int closest = nums[0] + nums[1] + nums[2];
    for (int i = 0; i < nums.size() - 2; ++i) {
        int left = i + 1;
        int right = nums.size() - 1;
        while (left < right) {
            int sum = nums[i] + nums[left] + nums[right];
            if (sum == target) {
                return sum;
            }
            if (abs(target - sum) < abs(target - closest)) {
                closest = sum;
            }
            if (sum < target) {
                left++;
            } else {
                right--;
            }
        }
    }
    return closest;
}

#include <algorithm>
#include <vector>

int threeSumClosest(std::vector<int>& nums, int target) 
    // Your code here
}

#include <algorithm>
#include <vector>
#include <iostream>

int main() {
    std::vector<int> nums = $args;
    int target = $args;
    int result = threeSumClosest(nums, target);
    std::cout << result << std::endl;
    return 0;
}

 //******************************************************** 

//Validating for ques 17
#include <vector>
#include <string>
using namespace std;

vector<string> letterCombinations(string digits) {
    if(digits.empty()) return {};
    vector<string> phone = {"abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"};
    vector<string> result = {""};

    for (char d : digits) {
        vector<string> temp;
        for (const string &s : result) {
            for (char c : phone[d - '2']) {
                temp.push_back(s + c);
            }
        }
        result.swap(temp);
    }
    return result;
}

#include <vector>
#include <string>
using namespace std;

vector<string> letterCombinations(string digits) 
    // Your code here
}

#include <vector>
#include <string>
using namespace std;

int main() {
    string digits = $args;
    vector<string> result = letterCombinations(digits);
    for (const string &s : result) {
        cout << s << " ";
    }
    cout << endl;
    return 0;
}

 //******************************************************** 

//Validating for ques 24
ListNode* swapPairs(ListNode* head) {
    if (!head || !head->next) return head;

    ListNode* second = head->next;
    head->next = swapPairs(second->next);
    second->next = head;
    
    return second;
}

ListNode* swapPairs(ListNode* head) 
    // Your code here
}

ListNode* swapPairs(ListNode* head) {
    if (!head || !head->next) return head;

    ListNode* second = head->next;
    head->next = swapPairs(second->next);
    second->next = head;
    
    return second;
}

 //******************************************************** 

