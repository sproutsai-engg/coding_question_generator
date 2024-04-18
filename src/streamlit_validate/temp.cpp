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


#include <iostream>
#include <string>
#include <unordered_set>

int main() {
    std::string s = "abcdeffghijklmnopqrstuvwxyz";
    int result = lengthOfLongestSubstring(s);
    std::cout << result << std::endl;
    return 0;
}