function isValidParenthesis(s) {
    const stack = [];
    const mapping = {')': '(', ']': '[', '}': '{'};
    for (let char of s) {
        if (char in mapping) {
            if (!stack.length || stack.pop() !== mapping[char]) {
                return false;
            }
        } else {
            stack.push(char);
        }
    }
    return !stack.length;
}
console.log(isValidParenthesis('(])')); // true