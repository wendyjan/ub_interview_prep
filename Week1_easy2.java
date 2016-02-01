import java.util.ArrayList;

/**
 * Created by wendyjan on 1/31/16.
 */
public class Week1_easy2 {

    public static void main(String[] args) {
        String tester = "Interview Prep";
        System.out.println(countUniqueChars(tester));
    }

    public static int countUniqueChars(String word) {
        /**
         * Counts the number of unique characters in the given string.
         *
         * @param word (String) the word that we would like to count unique characters for.
         * @return (int) the number of unique characters.
         */
        ArrayList<Character> seen = new ArrayList<Character>();
        int uniqueCount = 0;
        for (int i = 0; i < word.length(); i++) {
            char tempChar = word.charAt(i);
            if (seen.contains(tempChar)) {
                continue;
            }
            else {
                uniqueCount++;
                seen.add(tempChar);
            }
        }
        return uniqueCount;
    }
}


