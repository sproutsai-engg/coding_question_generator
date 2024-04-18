import java.util.LinkedList;
import java.util.regex.Pattern;
import java.util.regex.Matcher;
import java.util.HashMap;
import java.util.Set;
import java.util.HashSet;
import java.util.Map;
import java.util.ArrayList;
import java.util.List;
import java.util.Arrays;
import java.util.Collections;
import java.util.stream.Collectors;
import java.util.stream.IntStream;


public class Main {
public static int lengthOfLongestSubstring(String s) {
    int left = 0, right = 0, maxLength = 0;
    Set<Character> characters = new HashSet<>();

    while (right < s.length()) {
        if (!characters.contains(s.charAt(right))) {
            characters.add(s.charAt(right));
            maxLength = Math.max(maxLength, right - left + 1);
            right++;
        } else {
            characters.remove(s.charAt(left));
            left++;
        }
    }

    return maxLength;
}


public static void main(String[] args) {
        String input ="abcdeffghijklmnopqrstuvwxyz";
        int result = lengthOfLongestSubstring(input);
        System.out.println(result);
    }
}