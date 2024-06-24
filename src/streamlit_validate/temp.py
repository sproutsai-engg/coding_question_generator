def canPermutePalindrome(s: str) -> bool:
    count = {}
    for c in s:
        if c in count:
            count[c] += 1
        else:
            count[c] = 1
    odd_count = 0
    for value in count.values():
        if value % 2:
            odd_count += 1
    return odd_count <= 1


if __name__ == "__main__":
    s ="abc"
    result = canPermutePalindrome(s)
    print("$sprouts@pankaj", result, "$sprouts@pankaj")