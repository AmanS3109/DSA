public class kadanes {
    public static void main(String[] args) {
        int[] arr = {4, 2, -3, 1};
        System.out.println(largestSum(arr));
    }
    static int largestSum(int[] nums){
        int maxSum = Integer.MIN_VALUE;
        int curSum = 0;
        for (int n: nums){
            curSum = Math.max(curSum, 0);
            curSum += n;
            maxSum = Math.max(maxSum, curSum);
        }
        return maxSum;
    }
}