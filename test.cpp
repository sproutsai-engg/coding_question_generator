#include <iostream>
#include <string>
using namespace std;

// Function to calculate the power of a number
int power(int base, int exponent) {
    int result = 1;
    for (int i = 0; i < exponent; ++i) {
        result *= base;
    }
    return result;
}

bool isArmstrong(int n) {
    int originalNum = n;
    int numDigits = 0;
    int sumOfDigits = 0;
    
    // Count the number of digits
    int temp = n;
    while (temp != 0) {
        numDigits++;
        temp /= 10;
    }
    
    // Calculate the sum of digits raised to the power of the number of digits
    temp = n;
    while (temp != 0) {
        int digit = temp % 10;
        sumOfDigits += power(digit, numDigits);
        temp /= 10;
    }
    
    return originalNum == sumOfDigits;
}

int main() {
    int n = 153;
    bool result = isArmstrong(n);
    cout << (result ? "True" : "False") << endl;  
    return 0;
}