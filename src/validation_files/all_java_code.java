//Validating for ques 1
import java.util.HashMap;
import java.util.Map;

public int[] twoSum(int[] nums, int target) {
    Map<Integer, Integer> map = new HashMap<>();
    for (int i = 0; i < nums.length; i++) {
        int complement = target - nums[i];
        if (map.containsKey(complement)) {
            return new int[]{map.get(complement), i};
        }
        map.put(nums[i], i);
    }
    throw new IllegalArgumentException("No two sum solution");
}

import java.util.HashMap;
import java.util.Map;

public int[] twoSum(int[] nums, int target) 
    // Your code here
}

public int[] twoSum(int[] nums, int target) {
    Map<Integer, Integer> map = new HashMap<>();
    for (int i = 0; i < nums.length; i++) {
        int complement = target - nums[i];
        if (map.containsKey(complement)) {
            return new int[]{map.get(complement), i};
        }
        map.put(nums[i], i);
    }
    throw new IllegalArgumentException("No two sum solution");
}

 //******************************************************** 

//Validating for ques 3
import java.util.HashSet;
import java.util.Set;

public int lengthOfLongestSubstring(String s) {
    int left = 0, right = 0, maxLength = 0;
    Set<Character> characters = new HashSet<>();

    while (right < s.length()) {
        if (!characters.contains(s.charAt(right))) {
            characters.add(s.charAt(right));
            maxLength = Math.max(maxLength, right - left + 1);
            right++;
        } else {
            characters.remove(s.charAt(left));
            left++;
        }
    }

    return maxLength;
}

import java.util.HashSet;
import java.util.Set;

public int lengthOfLongestSubstring(String s) 
    // Your code here
}

public int lengthOfLongestSubstring(String s) {
    int left = 0, right = 0, maxLength = 0;
    Set<Character> characters = new HashSet<>();

    while (right < s.length()) {
        if (!characters.contains(s.charAt(right))) {
            characters.add(s.charAt(right));
            maxLength = Math.max(maxLength, right - left + 1);
            right++;
        } else {
            characters.remove(s.charAt(left));
            left++;
        }
    }

    return maxLength;
}

 //******************************************************** 

//Validating for ques 4
public double findMedianSortedArrays(int[] nums1, int[] nums2) {
    if (nums1.length > nums2.length) {
        return findMedianSortedArrays(nums2, nums1);
    }
    
    int x = nums1.length;
    int y = nums2.length;
    int low = 0;
    int high = x;
    
    while (low <= high) {
        int partitionX = (low + high) / 2;
        int partitionY = (x + y + 1) / 2 - partitionX;
        
        int maxLeftX = (partitionX == 0) ? Integer.MIN_VALUE : nums1[partitionX - 1];
        int minRightX = (partitionX == x) ? Integer.MAX_VALUE : nums1[partitionX];
        
        int maxLeftY = (partitionY == 0) ? Integer.MIN_VALUE : nums2[partitionY - 1];
        int minRightY = (partitionY == y) ? Integer.MAX_VALUE : nums2[partitionY];
        
        if (maxLeftX <= minRightY && maxLeftY <= minRightX) {
            if ((x + y) % 2 == 0) {
                return (double)(Math.max(maxLeftX, maxLeftY) + Math.min(minRightX, minRightY)) / 2;
            } else {
                return (double)Math.max(maxLeftX, maxLeftY);
            }
        } else if (maxLeftX > minRightY) {
            high = partitionX - 1;
        } else {
            low = partitionX + 1;
        }
    }    
    return 0;
}

public double findMedianSortedArrays(int[] nums1, int[] nums2) 
    // Your code here
}

public double findMedianSortedArrays(int[] nums1, int[] nums2) {
    if (nums1.length > nums2.length) {
        return findMedianSortedArrays(nums2, nums1);
    }
    
    int x = nums1.length;
    int y = nums2.length;
    int low = 0;
    int high = x;
    
    while (low <= high) {
        int partitionX = (low + high) / 2;
        int partitionY = (x + y + 1) / 2 - partitionX;
        
        int maxLeftX = (partitionX == 0) ? Integer.MIN_VALUE : nums1[partitionX - 1];
        int minRightX = (partitionX == x) ? Integer.MAX_VALUE : nums1[partitionX];
        
        int maxLeftY = (partitionY == 0) ? Integer.MIN_VALUE : nums2[partitionY - 1];
        int minRightY = (partitionY == y) ? Integer.MAX_VALUE : nums2[partitionY];
        
        if (maxLeftX <= minRightY && maxLeftY <= minRightX) {
            if ((x + y) % 2 == 0) {
                return (double)(Math.max(maxLeftX, maxLeftY) + Math.min(minRightX, minRightY)) / 2;
            } else {
                return (double)Math.max(maxLeftX, maxLeftY);
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
public String longestPalindromicSubstring(String s) {
    int n = s.length();
    if (n == 0) return "";

    int start = 0, maxLength = 1;

    for (int i = 0; i < n; ++i) {
        int l = i, r = i;

        while (r < n - 1 && s.charAt(r) == s.charAt(r + 1))
            r++;
        i = r;

        while (l > 0 && r < n - 1 && s.charAt(l - 1) == s.charAt(r + 1)) {
            l--;
            r++;
        }

        int length = r - l + 1;
        if (length > maxLength) {
            start = l;
            maxLength = length;
        }
    }

    return s.substring(start, start + maxLength);
}

public String longestPalindromicSubstring(String s) 
    // Your code here
}

public String longestPalindromicSubstring(String s) {
    int n = s.length();
    if (n == 0) return "";

    int start = 0, maxLength = 1;

    for (int i = 0; i < n; ++i) {
        int l = i, r = i;

        while (r < n - 1 && s.charAt(r) == s.charAt(r + 1))
            r++;
        i = r;

        while (l > 0 && r < n - 1 && s.charAt(l - 1) == s.charAt(r + 1)) {
            l--;
            r++;
        }

        int length = r - l + 1;
        if (length > maxLength) {
            start = l;
            maxLength = length;
        }
    }

    return s.substring(start, start + maxLength);
}

 //******************************************************** 

//Validating for ques 7
public int reverse(int x) {
    long res = 0;
    while (x != 0) {
        res = res * 10 + x % 10;
        x /= 10;
    }
    return (res < Integer.MIN_VALUE || res > Integer.MAX_VALUE) ? 0 : (int)res;
}

public int reverse(int x) 
    // Your code here
}

public int reverse(int x) {
    long res = 0;
    while (x != 0) {
        res = res * 10 + x % 10;
        x /= 10;
    }
    return (res < Integer.MIN_VALUE || res > Integer.MAX_VALUE) ? 0 : (int)res;
}

 //******************************************************** 

//Validating for ques 9
public boolean isPalindrome(int x) {
    if (x < 0) return false;
    int original = x, reversed = 0;
    while (x > 0) {
        reversed = reversed * 10 + x % 10;
        x /= 10;
    }
    return original == reversed;
}


public boolean isPalindrome(int x) 
    // Your code here
}


public static void main(String[] args) {
    int x = $args;
    boolean result = isPalindrome(x);
    System.out.println(result);
}

 //******************************************************** 

//Validating for ques 10
public boolean isMatch(String s, String p) {
    int m = s.length(), n = p.length();
    boolean[][] dp = new boolean[m + 1][n + 1];
    dp[0][0] = true;

    for (int j = 1; j <= n; j++) {
        if (p.charAt(j - 1) == '*' && dp[0][j - 2]) {
            dp[0][j] = true;
        }
    }

    for (int i = 1; i <= m; i++) {
        for (int j = 1; j <= n; j++) {
            if (p.charAt(j - 1) == s.charAt(i - 1) || p.charAt(j - 1) == '.') {
                dp[i][j] = dp[i - 1][j - 1];
            } else if (p.charAt(j - 1) == '*') {
                dp[i][j] = dp[i][j - 2] || (dp[i - 1][j] && (s.charAt(i - 1) == p.charAt(j - 2) || p.charAt(j - 2) == '.'));
            }
        }
    }

    return dp[m][n];
}

public boolean isMatch(String s, String p) 
    // Your code here
}

public boolean isMatch(String s, String p) {
    int m = s.length(), n = p.length();
    boolean[][] dp = new boolean[m + 1][n + 1];
    dp[0][0] = true;

    for (int j = 1; j <= n; j++) {
        if (p.charAt(j - 1) == '*' && dp[0][j - 2]) {
            dp[0][j] = true;
        }
    }

    for (int i = 1; i <= m; i++) {
        for (int j = 1; j <= n; j++) {
            if (p.charAt(j - 1) == s.charAt(i - 1) || p.charAt(j - 1) == '.') {
                dp[i][j] = dp[i - 1][j - 1];
            } else if (p.charAt(j - 1) == '*') {
                dp[i][j] = dp[i][j - 2] || (dp[i - 1][j] && (s.charAt(i - 1) == p.charAt(j - 2) || p.charAt(j - 2) == '.'));
            }
        }
    }

    return dp[m][n];
}

 //******************************************************** 

//Validating for ques 11
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

public int maxArea(int[] height) 
    // Your code here
}

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

 //******************************************************** 

//Validating for ques 8
public int myAtoi(String s) {
    long result = 0;
    int i = 0, sign = 1;
    while (i < s.length() && s.charAt(i) == ' ') i++;
    if (i < s.length() && (s.charAt(i) == '-' || s.charAt(i) == '+')) {
        sign = (s.charAt(i++) == '+') ? 1 : -1;
    }
    while (i < s.length() && Character.isDigit(s.charAt(i))) {
        result = result * 10 + (s.charAt(i++) - '0');
        if (result * sign > Integer.MAX_VALUE) return Integer.MAX_VALUE;
        if (result * sign < Integer.MIN_VALUE) return Integer.MIN_VALUE;
    }
    return (int) (result * sign);
}

public int myAtoi(String s) 
    // Your code here
}

public int myAtoi(String s) {
    long result = 0;
    int i = 0, sign = 1;
    while (i < s.length() && s.charAt(i) == ' ') i++;
    if (i < s.length() && (s.charAt(i) == '-' || s.charAt(i) == '+')) {
        sign = (s.charAt(i++) == '+') ? 1 : -1;
    }
    while (i < s.length() && Character.isDigit(s.charAt(i))) {
        result = result * 10 + (s.charAt(i++) - '0');
        if (result * sign > Integer.MAX_VALUE) return Integer.MAX_VALUE;
        if (result * sign < Integer.MIN_VALUE) return Integer.MIN_VALUE;
    }
    return (int) (result * sign);
}

 //******************************************************** 

//Validating for ques 12
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class RomanNumerals {
    public static String intToRoman(int num) {
        List<Pair> romans = Arrays.asList(
            new Pair(1000, "M"), new Pair(900, "CM"), new Pair(500, "D"), 
            new Pair(400, "CD"), new Pair(100, "C"), new Pair(90, "XC"),
            new Pair(50, "L"), new Pair(40, "XL"), new Pair(10, "X"), 
            new Pair(9, "IX"), new Pair(5, "V"), new Pair(4, "IV"),
            new Pair(1, "I")
        );
        StringBuilder roman = new StringBuilder();
        for (Pair p : romans) {
            while (num >= p.num) {
                roman.append(p.symbol);
                num -= p.num;
            }
        }
        return roman.toString();
    }
    
    private static class Pair {
        final int num;
        final String symbol;
        
        Pair(int num, String symbol) {
            this.num = num;
            this.symbol = symbol;
        }
    }
}

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class RomanNumerals 
    // Your code here
}

public static String intToRoman(int num) {
        List<Pair> romans = Arrays.asList(
            new Pair(1000, "M"), new Pair(900, "CM"), new Pair(500, "D"), 
            new Pair(400, "CD"), new Pair(100, "C"), new Pair(90, "XC"),
            new Pair(50, "L"), new Pair(40, "XL"), new Pair(10, "X"), 
            new Pair(9, "IX"), new Pair(5, "V"), new Pair(4, "IV"),
            new Pair(1, "I")
        );
        StringBuilder roman = new StringBuilder();
        for (Pair p : romans) {
            while (num >= p.num) {
                roman.append(p.symbol);
                num -= p.num;
            }
        }
        return roman.toString();
    }

 //******************************************************** 

//Validating for ques 13
public int romanToInt(String s) {
    Map<Character, Integer> romanValues = new HashMap<>();
    romanValues.put('I', 1);
    romanValues.put('V', 5);
    romanValues.put('X', 10);
    romanValues.put('L', 50);
    romanValues.put('C', 100);
    romanValues.put('D', 500);
    romanValues.put('M', 1000);

    int total = 0;
    int prevValue = 0;

    for (char c : s.toCharArray()) {
        int currValue = romanValues.get(c);
        total += currValue > prevValue ? currValue - 2 * prevValue : currValue;
        prevValue = currValue;
    }

    return total;
}


public int romanToInt(String s) 
    // Your code here
}


public int romanToInt(String s) {
    Map<Character, Integer> romanValues = new HashMap<>();
    romanValues.put('I', 1);
    romanValues.put('V', 5);
    romanValues.put('X', 10);
    romanValues.put('L', 50);
    romanValues.put('C', 100);
    romanValues.put('D', 500);
    romanValues.put('M', 1000);

    int total = 0;
    int prevValue = 0;

    for (char c : s.toCharArray()) {
        int currValue = romanValues.get(c);
        total += currValue > prevValue ? currValue - 2 * prevValue : currValue;
        prevValue = currValue;
    }

    return total;
}

 //******************************************************** 

//Validating for ques 14
public String longestCommonPrefix(String[] strs) {
    if (strs.length == 0) return "";

    for (int i = 0; i < strs[0].length(); ++i) {
        char c = strs[0].charAt(i);
        for (int j = 1; j < strs.length; ++j) {
            if (i == strs[j].length() || strs[j].charAt(i) != c) {
                return strs[0].substring(0, i);
            }
        }
    }
    return strs[0];
}

public String longestCommonPrefix(String[] strs) 
    // Your code here
}

public String longestCommonPrefix(String[] strs) {
    if (strs.length == 0) return "";

    for (int i = 0; i < strs[0].length(); ++i) {
        char c = strs[0].charAt(i);
        for (int j = 1; j < strs.length; ++j) {
            if (i == strs[j].length() || strs[j].charAt(i) != c) {
                return strs[0].substring(0, i);
            }
        }
    }
    return strs[0];
}

 //******************************************************** 

//Validating for ques 17
public List<String> letterCombinations(String digits) {
    LinkedList<String> output = new LinkedList<>();
    if(digits.isEmpty()) return output;
    
    String[] phone = new String[] {"abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"};
    output.add("");
    
    for(char d : digits.toCharArray()){
        while(output.peek().length() == digits.indexOf(d)){
            String perm = output.remove();
            for(char c : phone[d - '2'].toCharArray()){
                output.add(perm + c);
            }
        }
    }
    
    return output;
}

public List<String> letterCombinations(String digits) 
    // Your code here
}

public List<String> letterCombinations(String digits) {
    LinkedList<String> output = new LinkedList<>();
    if(digits.isEmpty()) return output;
    
    String[] phone = new String[] {"abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"};
    output.add("");
    
    for(char d : digits.toCharArray()){
        while(output.peek().length() == digits.indexOf(d)){
            String perm = output.remove();
            for(char c : phone[d - '2'].toCharArray()){
                output.add(perm + c);
            }
        }
    }
    
    return output;
}

 //******************************************************** 

