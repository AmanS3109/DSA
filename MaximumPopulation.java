public class MaximumPopulation {
    public static void main(String[] args) {
        System.out.println(maximumPopulation(new int[][] {{1993, 1999}, {2000, 2010}}));
    }
    static int maximumPopulation(int[][] logs) {
        int[] freq = new int[2051];
        for (int[] log : logs) {
            int birth = log[0];
            int death = log[1];
            freq[birth]++;
            freq[death]--;
        }
        int max = 0;
        int year = 0;
        int current = 0;
        for (int i = 1950; i <= 2050; i++) {
            current += freq[i];
            if (current > max) {
                max = current;
                year = i;
            }
        }
        return year;
    }
}