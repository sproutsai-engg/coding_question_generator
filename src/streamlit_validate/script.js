function lengthOfLongestSubstring(s) {
    let left = 0, right = 0, maxLength = 0;
    const characters = new Set();

    while (right < s.length) {
        if (!characters.has(s.charAt(right))) {
            characters.add(s.charAt(right));
            maxLength = Math.max(maxLength, right - left + 1);
            right++;
        } else {
            characters.delete(s.charAt(left));
            left++;
        }
    }

    return maxLength;
}


function main() {
    const s = "abcdeffghijklmnopqrstuvwxyz";
    const result = lengthOfLongestSubstring(s);
    console.log(result);
}
main();