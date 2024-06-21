function largestPalindrome(n) {
    if (n === 1) return 9; // Handle 1-digit numbers
    let upper_limit = Math.pow(10, n) - 1;
    let lower_limit = Math.floor(upper_limit / 10);
    for (let i = upper_limit; i > lower_limit; i--) {
        let temp = i;
        let reverse = 0;
        while (temp !== 0) {
            reverse = reverse * 10 + temp % 10;
            temp = Math.floor(temp / 10);
        }
        let palindrome = i * Math.pow(10, n) + reverse;
        for (let j = upper_limit; j > lower_limit; j--) {
            let product = Math.floor(palindrome / j);
            if (palindrome % j === 0 && product <= upper_limit) {
                return palindrome % 1337;
            }
        }
    }
    return -1;
}



function main() {
    const n = 7;
    const result = largestPalindrome(n);
    console.log(result);
}
main();