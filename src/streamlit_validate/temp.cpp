#include <iostream>
#include <cmath>

int largestPalindrome(int n) {
    if (n == 1) return 9;
    int upper_limit = pow(10, n) - 1;
    int lower_limit = upper_limit / 10;
    for (int i = upper_limit; i > lower_limit; --i) {
        long long temp = i;
        long long reverse = 0;
        while (temp != 0) {
            reverse = reverse * 10 + temp % 10;
            temp /= 10;
        }
        long long palindrome = i * pow(10, n) + reverse;
        for (long long j = upper_limit; j > lower_limit; --j) {
            long long product = palindrome / j;
            if (palindrome % j == 0 && product <= upper_limit) {
                return palindrome % 1337;
            }
        }
    }
    return -1;
}


int main() {
    int n = 7;
    int result = largestPalindrome(n);
    std::cout << result << std::endl;
    return 0;
}