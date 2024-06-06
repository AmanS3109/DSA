import java.util.HashMap;

public class twoSum {
    public static void main(String[] args) {
        int[] book = {2, 3, 4, 5, 6, 7, 8, 11};
        System.out.println(findSum(8, book, 14));
    }
    static String findSum(int n, int[] book, int target){
        HashMap<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < book.length; i++) {
            int firstNum = book[i];
            int secNum = target - firstNum;
            if (map.containsKey(secNum)) {
                return "YES";
            }
            map.put(firstNum, i);
        }
        return "NO";
    }
}
