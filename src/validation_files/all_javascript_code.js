//Validating for ques 1
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

function twoSum(nums, target) 
    // Your code here
}

function main() {
    const nums = $args[0];
    const target = $args[1];
    const result = twoSum(nums, target);
    console.log(result);
}

 //******************************************************** 

//Validating for ques 3
function lengthOfLongestSubstring(s) {
    let left = 0, right = 0, maxLength = 0;
    const characters = new Set();

    while (right < s.length) {
        if (!characters.has(s.charAt(right))) {
            characters.add(s.charAt(right));
            maxLength = Math.max(maxLength, right - left + 1);
            right++;
        } else {
            characters.delete(s.charAt(left));
            left++;
        }
    }

    return maxLength;
}

function lengthOfLongestSubstring(s) 
    // Your code here
}

function main() {
    const s = $args;
    const result = lengthOfLongestSubstring(s);
    console.log(result);
}

 //******************************************************** 

//Validating for ques 4
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


function findMedianSortedArrays(nums1, nums2) 
    // Your code here
}


function findMedianSortedArrays(nums1, nums2) {
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

 //******************************************************** 

//Validating for ques 5
function longestPalindromicSubstring(s) {
  let n = s.length;
  if (n === 0) return "";

  let start = 0, maxLength = 1;

  for (let i = 0; i < n; ++i) {
    let l = i, r = i;

    while (r < n - 1 && s[r] === s[r + 1])
      r++;
    i = r;

    while (l > 0 && r < n - 1 && s[l - 1] === s[r + 1]) {
      l--;
      r++;
    }

    let length = r - l + 1;
    if (length > maxLength) {
      start = l;
      maxLength = length;
    }
  }

  return s.substring(start, start + maxLength);
}

function longestPalindromicSubstring(s) 
    // Your code here
}

function main() {
  const s = $args;
  const result = longestPalindromicSubstring(s);
  console.log(result);
}

 //******************************************************** 

//Validating for ques 7
function reverse(x) {
    let sign = x < 0 ? -1 : 1;
    x = Math.abs(x);
    let res = 0;
    while (x !== 0) {
        res = res * 10 + x % 10;
        x = Math.floor(x / 10);
    }
    res *= sign;
    return (res < -(2 ** 31) || res > 2 ** 31 - 1) ? 0 : res;
}

function reverse(x) 
    // Your code here
}

function main() {
    const x = $args;
    const sign = x < 0 ? -1 : 1;
    x = Math.abs(x);
    let res = 0;
    while (x !== 0) {
        res = res * 10 + x % 10;
        x = Math.floor(x / 10);
    }
    res *= sign;
    const result = (res < -(2 ** 31) || res > 2 ** 31 - 1) ? 0 : res;
    console.log(result);
}

 //******************************************************** 

//Validating for ques 9
function isPalindrome(x) {
    if (x < 0) return false;
    let original = x, reversed = 0;
    while (x > 0) {
        reversed = reversed * 10 + x % 10;
        x = Math.floor(x / 10);
    }
    return original === reversed;
}


function isPalindrome(x) 
    // Your code here
}


function main() {
    const x = $args;
    const result = isPalindrome(x);
    console.log(result);
}


 //******************************************************** 

//Validating for ques 10
function isMatch(s, p) {
    const m = s.length, n = p.length;
    const dp = Array.from({ length: m + 1 }, () => Array(n + 1).fill(false));
    dp[0][0] = true;

    for (let j = 1; j <= n; j++) {
        if (p[j - 1] === '*' && dp[0][j - 2]) {
            dp[0][j] = true;
        }
    }

    for (let i = 1; i <= m; i++) {
      for (let j = 1; j <= n; j++) {
          if (p[j - 1] === s[i - 1] || p[j - 1] === '.') {
              dp[i][j] = dp[i - 1][j - 1];
          } else if (p[j - 1] === '*') {
              dp[i][j] = dp[i][j - 2] || (dp[i - 1][j] && (s[i - 1] === p[j - 2] || p[j - 2] === '.'));
          }
      }
    }

    return dp[m][n];
}

function isMatch(s, p) 
    // Your code here
}

function main() {
    const s = $args[0];
    const p = $args[1];
    const result = isMatch(s, p);
    console.log(result);
}

 //******************************************************** 

//Validating for ques 11
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

function maxArea(height) 
    // Your code here
}

function main() {
    const height = $args;
    const result = maxArea(height);
    console.log(result);
}

 //******************************************************** 

//Validating for ques 8
function myAtoi(s) {
    let result = 0, i = 0, sign = 1;
    while (s[i] === ' ') i++;
    if (s[i] === '-' || s[i] === '+') sign = (s[i++] === '+') ? 1 : -1;
    while (!isNaN(s[i]) && s[i] !== ' ') {
        result = result * 10 + parseInt(s[i++], 10);
        if (result * sign > 2147483647) return 2147483647;
        if (result * sign < -2147483648) return -2147483648;
    }
    return result * sign;
}

function myAtoi(s) 
    // Your code here
}

function main() {
    const s = $args;
    const result = myAtoi(s);
    console.log(result);
}

 //******************************************************** 

//Validating for ques 12
function intToRoman(num) {
    const romans = [
        [1000, "M"], [900, "CM"], [500, "D"],
        [400, "CD"], [100, "C"], [90, "XC"],
        [50, "L"], [40, "XL"], [10, "X"], 
        [9, "IX"], [5, "V"], [4, "IV"], [1, "I"]
    ];
    let roman = "";
    for (const [value, symbol] of romans) {
        while (num >= value) {
            roman += symbol;
            num -= value;
        }
    }
    return roman;
}

function intToRoman(num) 
    // Your code here
}

function main() {
    const num = $args;
    const result = intToRoman(num);
    console.log(result);
}

 //******************************************************** 



 