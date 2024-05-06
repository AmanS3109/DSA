public class highestAltitude {
    public static void main(String[] args) {
        System.out.println(largestAltitude(new int[] {-5, 1, 5, 0, -7}));
    }
    static int largestAltitude(int[] gain) {
        int max = 0;
        int current = 0;
        for (int i = 0; i < gain.length; i++) {
            current += gain[i];
            if (current > max) {
                max = current;
            }
        }
        return max;
    }
}