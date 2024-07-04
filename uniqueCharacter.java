//determine if a string has all unique characters or not

public class uniqueCharacter {
    public static void main(String[] args) {
        String str = "Aman";
        System.out.println(isUnique(str));
    }
    static boolean isUnique(String str){
        str = str.toLowerCase();
        if (str.length() > 128) {
            return false;
        }
        boolean[] char_set = new boolean[128];
        for (int i = 0; i < str.length(); i++) {
            int val = str.charAt(i);
            if (char_set[val]) {
                return false;
            }
            char_set[val] = true;
        }
        return true;
    }
}