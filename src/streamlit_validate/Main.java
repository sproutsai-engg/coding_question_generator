import java.util.*;
import java.util.regex.Pattern;

public class Main {
public static boolean canPermutePalindrome(String s) {
    HashMap<Character, Integer> count = new HashMap<>();
    for(char c : s.toCharArray()) {
        count.put(c, count.getOrDefault(c, 0) + 1);
    }
    int odd_count = 0;
    for(int value : count.values()) {
        if (value % 2 != 0) {
            odd_count++;
        }
    }
    return odd_count <= 1;
}


public static void main(String[] args) {
        String s = "carerac";
        boolean result = canPermutePalindrome(s); // Use nthUglyNumber instead of addDigits
        System.out.println("$sprouts@pankaj"+result+"$sprouts@pankaj");
    }
}