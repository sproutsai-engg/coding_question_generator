#include <stdio.h>
#include <math.h>

int isArmstrong(int n) {
    int originalNum = n;
    int numDigits = 0;
    int sum = 0;
    
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
        
        // Compute digit^numDigits using a loop
        int power = 1;
        for (int i = 0; i < numDigits; i++) {
            power *= digit;
        }
        
        sum += power;
        temp /= 10;
    }
    
    return originalNum == sum;
}


int main() {
    int n = $args;
    int result = isArmstrong(n);
    printf("%s", result ? "True" : "False");
    return 0;
}