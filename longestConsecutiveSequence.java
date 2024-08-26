import java.util.*;

public class longestConsecutiveSequence {
    public static void main(String[] args) {
        int[] arr = {11, 7, 1, 17, 6, 2, 3, 16, 8, 4, 9, 10, 15};
        System.out.println(lcs(arr));
    }

    static int lcs(int[] arr) {
        HashMap<Integer, Boolean> map = new HashMap<>();
        for (int num : arr) {
            map.put(num, true);
        }

        int maxLen = 0;
        for (int num : map.keySet()) {
            if (!map.containsKey(num - 1)) {
                int currLen = 1;
                int val = num;
                while (map.containsKey(val + 1)) {
                    currLen++;
                    val++;
                }
                maxLen = Math.max(maxLen, currLen);
            }
        }
        return maxLen;
    }
}