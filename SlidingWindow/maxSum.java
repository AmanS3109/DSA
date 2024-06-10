package SlidingWindow;

public class maxSum {
    public static void main(String[] args) {
        int[] array = {2, 3, 1, 9, 8, 4, 2};
        int k = 3;
        System.out.println(maximumSum(array, k));
    }
    static int maximumSum(int[] arr, int k){
        int  i = 0;
        int j = 0;
        int max = Integer.MIN_VALUE;
        int sum = 0;
        while (j < arr.length) {
            sum += arr[j];
            if (j-i+1 < k) {
                j++;
            }
            else if (j - i + 1 == k) {
                int maximum = 0; // Initialize maximum with a default value
                maximum = Math.max(maximum, sum);
                sum -= arr[i];
                i++;
                j++;
            }
        }
        return max; // Add a return statement to return the 'max' value
    }
}