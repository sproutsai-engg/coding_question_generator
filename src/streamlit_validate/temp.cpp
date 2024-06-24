#include <iostream>
#include <unordered_map>
#include <string>

// Function to check if any permutation of the string can form a palindrome
bool canPermutePalindrome(const std::string& s) {
    std::unordered_map<char, int> count;
    
    // Count the frequency of each character in the string
    for (char c : s) {
        count[c]++;
    }

    int odd_count = 0;
    
    // Count the number of characters with odd frequencies
    for (const auto& pair : count) {
        if (pair.second % 2 != 0) {
            odd_count++;
        }
    }

    // A string can form a palindrome if it has at most one character with an odd frequency
    return odd_count <= 1;
}


int main() {
    std::string s = "aabbaa";
    bool result = canPermutePalindrome(s);
    std::cout <<"$sprouts@pankaj"<< std::boolalpha<<result<<"$sprouts@pankaj";
    return 0;
}