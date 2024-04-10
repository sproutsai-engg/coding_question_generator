#include <iostream>
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


int main() {
  std::string s = "babad";
  

  std::cout << longestPalindromicSubstring(s);

  return 0;
}