#Validating for ques 1
def twoSum(nums, target):
    map = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in map:
            return [map[complement], i]
        map[num] = i
    return []

def twoSum(nums, target):
    # Your code here


if __name__ == "__main__":
    nums = $args[0]
    target = $args[1]
    result = twoSum(nums, target)
    print(result)

 #******************************************************** 

#Validating for ques 3
def length_of_longest_substring(s: str) -> int:
    left = 0
    right = 0
    max_length = 0
    characters = set()

    while right < len(s):
        if s[right] not in characters:
            characters.add(s[right])
            max_length = max(max_length, right - left + 1)
            right += 1
        else:
            characters.remove(s[left])
            left += 1

    return max_length

def length_of_longest_substring(s: str) -> int:
    # Your code here


if __name__ == "__main__":
    s = $args
    result = length_of_longest_substring(s)
    print(result)
}

 #******************************************************** 

#Validating for ques 4
def findMedianSortedArrays(nums1, nums2):
    if len(nums1) > len(nums2):
        return findMedianSortedArrays(nums2, nums1)
    
    x, y = len(nums1), len(nums2)
    low, high = 0, x

    while low <= high:
        partition_x = (low + high) // 2
        partition_y = (x + y + 1) // 2 - partition_x

        max_left_x = float('-inf') if partition_x == 0 else nums1[partition_x - 1]
        min_right_x = float('inf') if partition_x == x else nums1[partition_x]

        max_left_y = float('-inf') if partition_y == 0 else nums2[partition_y - 1]
        min_right_y = float('inf') if partition_y == y else nums2[partition_y]

        if max_left_x <= min_right_y and max_left_y <= min_right_x:
            if (x + y) % 2 == 0:
                return (max(max_left_x, max_left_y) + min(min_right_x, min_right_y)) / 2
            else:
                return max(max_left_x, max_left_y)
        elif max_left_x > min_right_y:
            high = partition_x - 1
        else:
            low = partition_x + 1
    
    return 0

def findMedianSortedArrays(nums1, nums2):
    # Your code here


if __name__ == '__main__':
    nums1 = $args
    nums2 = $args
    result = findMedianSortedArrays(nums1, nums2)
    print(result)
}

 #******************************************************** 

#Validating for ques 5
def longest_palindromic_substring(s: str) -> str:
    n = len(s)
    if n == 0: return ""

    start, max_length = 0, 1

    for i in range(n):
        l, r = i, i

        while r < n - 1 and s[r] == s[r + 1]:
            r += 1
        i = r

        while l > 0 and r < n - 1 and s[l - 1] == s[r + 1]:
            l -= 1
            r += 1

        length = r - l + 1
        if length > max_length:
            start, max_length = l, length

    return s[start:start + max_length]

def longest_palindromic_substring(s: str) -> str:
    # Your code here


if __name__ == "__main__":
    s = $args
    result = longest_palindromic_substring(s)
    print(result)

 #******************************************************** 

#Validating for ques 7
def reverse(x: int) -> int:
    sign = -1 if x < 0 else 1
    x = abs(x)
    res = 0
    while x:
        res = res * 10 + x % 10
        x //= 10
    res *= sign
    return res if -2**31 <= res <= 2**31 - 1 else 0

def reverse(x: int) -> int:
    # Your code here


if __name__ == "__main__":
    x = $args
    result = reverse(x)
    print(result)
}

 #******************************************************** 

#Validating for ques 9
def is_palindrome(x: int) -> bool:
    if x < 0:
        return False
    original, reversed = x, 0
    while x > 0:
        reversed = reversed * 10 + x % 10
        x //= 10
    return original == reversed


def is_palindrome(x: int) -> bool:
    # Your code here


if __name__ == "__main__":
    x = $args
    result = is_palindrome(x)
    print(result)


 #******************************************************** 

#Validating for ques 10
def is_match(s: str, p: str) -> bool:
    m, n = len(s), len(p)
    dp = [[False] * (n + 1) for _ in range(m + 1)]
    dp[0][0] = True

    for j in range(1, n + 1):
        if p[j - 1] == '*' and dp[0][j - 2]:
            dp[0][j] = True

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if p[j - 1] == s[i - 1] or p[j - 1] == '.':
                dp[i][j] = dp[i - 1][j - 1]
            elif p[j - 1] == '*':
                dp[i][j] = dp[i][j - 2] or (dp[i - 1][j] and (s[i - 1] == p[j - 2] or p[j - 2] == '.'))

    return dp[m][n]

def is_match(s: str, p: str) -> bool:
    # Your code here


if __name__ == '__main__':
    s = $args[0]
    p = $args[1]
    result = is_match(s, p)
    print(result)

 #******************************************************** 

#Validating for ques 11
def max_area(height):
    max_area, left, right = 0, 0, len(height) - 1
    while left < right:
        max_area = max(max_area, min(height[left], height[right]) * (right - left))
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return max_area

def max_area(height):
    # Your code here


if __name__ == "__main__":
    height = $args
    result = max_area(height)
    print(result)
}

 #******************************************************** 

#Validating for ques 8
def myAtoi(s):
    result, i, sign = 0, 0, 1
    while i < len(s) and s[i] == ' ': i += 1
    if i < len(s) and (s[i] == '-' or s[i] == '+'):
        sign = -1 if s[i] == '-' else 1
        i += 1
    while i < len(s) and s[i].isdigit():
        result = result * 10 + int(s[i])
        i += 1
        if result * sign > 2**31 - 1: return 2**31 - 1
        if result * sign < -2**31: return -2**31
    return result * sign

def myAtoi(s):
    # Your code here


if __name__ == "__main__":
    s = $args[0]
    result = myAtoi(s)
    print(result)

 #******************************************************** 

#Validating for ques 12
def int_to_roman(num):
    romans = [
        (1000, "M"), (900, "CM"), (500, "D"),
        (400, "CD"), (100, "C"), (90, "XC"),
        (50, "L"), (40, "XL"), (10, "X"), 
        (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
    ]
    roman = ""
    for value, symbol in romans:
        while num >= value:
            roman += symbol
            num -= value
    return roman

def int_to_roman(num):
    # Your code here


if __name__ == "__main__":
    num = $args[0]
    result = int_to_roman(num)
    print(result)

 #******************************************************** 

