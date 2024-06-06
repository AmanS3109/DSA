import java.util.HashMap;

public class twoSum {
    public static void main(String[] args) {
        
    }
    static String findSum(int n, int[] arr, int target){
        HashMap<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < arr.length; i++) {
            int firstNum = arr[i];
            int secNum = target - firstNum;
            if (map.find(secNum) != map.end()) {
                return "Yes";
            }
            map[firstNum] = i; 
        }
        return "No";
    }
}
