bool isPalindrome(int x) {
    if (x < 0) return false;
    int original = x, reversed = 0;
    while (x > 0) {
        reversed = reversed * 10 + x % 10;
        x /= 10;
    }
    return original == reversed;
}



#include <iostream>
using namespace std;

int main() {
    int n = 1234321;
    bool result = isPalindrome(n);
    cout <<std::boolalpha<< result << endl;
    return 0;
}