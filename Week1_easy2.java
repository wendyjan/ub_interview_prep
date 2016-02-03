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

/** Some alternate solutions, courtesy of Dr. Alphonce!
 * 
1) Use a HashSet<Character>

public static int countUniqueChars(String word) {
       HashSet<Character> seen = new HashSet<Character>();
       for (int i = 0; i < word.length(); i++) {
               seen.add(word.charAt(i));
       }
       return seen.size();
}

2) Use an array:

public static int countUniqueChars(String word) {
       boolean[] seen = new boolean[256];  // 2^8 = 256
       int uniqueCount = 0;
       for (int i = 0; i < word.length(); i++) {
               if (! seen[word.charAt(i)]) {
                   seen[word.charAt(i)] = true;
                   uniqueCount++;
                }
       }
       return uniqueCount;
}

 * 
 * /


