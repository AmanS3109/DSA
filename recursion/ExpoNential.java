package recursion;

public class ExpoNential{
    public static void main(String[] args) {
        System.out.println(Raise(5, 0));
    }
    static int Raise(int base, int exp){
        if (exp == 0) {
            return 1;
        } else {
            return base * Raise(base, exp - 1);
        }
    }
}