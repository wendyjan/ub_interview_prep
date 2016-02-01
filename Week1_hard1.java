/**
 * Created by wendyjan on 1/31/16.
 */
import java.util.LinkedList;
import java.util.Stack;

public class Week1_hard1 {

    public static void main(String[] args) {
        String[] allWords = {"a", "ab", "aba", "abba", "abc", "abcd", "abcde", "abcddd", "abcdee", "abcdeef"};
        String starterWord = "ab";
        System.out.println(longestChain(starterWord, allWords));
    }

    public static String longestChain(String starterWord, String[] allWords) {
        /**
         * Finds the longest chain of "jumps" from the starter word to the longer words in a list,
         * where each valid jump is where a single character has been added anywhere in the word.
         *
         * This can be treated as a breadth-first search. If multiple chains with the same number of words are found,
         * then only the first of these is returned.
         *
         * @param starter (String) the starter word of the chain.
         * @param allWords (String[]) the list of all allowable words.
         * @return (String) a representation of the longest chain of word jumps that begins with the starter.
         */
        // Create a queue to manage breadth-first search.
        // Each stack that we push onto the queue represents a chain of words, with the longest word on top.
        LinkedList<Stack<String>> queue = new LinkedList();
        // Create the starter chain, with only the starter word on it.
        Stack<String> starterChain = new Stack();
        starterChain.push(starterWord);
        queue.add(starterChain);
        Stack<String> temp = starterChain;
        while (queue.size() > 0) {
            for (int i = 0; i < queue.size(); i++) {
                temp = queue.remove();
                for (int j = 0; j < allWords.length; j++) {
                    if (allWords[j].length() == temp.peek().length() + 1) {
                        if (isValidJump(temp.peek(), allWords[j])) {
                            // TODO I'm no Java expert-- is there a more efficient way to store our chains?
                            // The current method requires a copy each time a new word can be added.
                            Stack<String> newChain =  (Stack<String>)temp.clone();
                            newChain.push(allWords[j]);
                            queue.add(newChain);
                        }
                    }
                }
            }

        }
        return temp.toString();
    }

    public static boolean isValidJump(String w1, String w2) {
        /**
         * Determines whether a jump between two words is valid,
         * which means that the two words differ by only a single character addition anywhere in the shorter word.
         *
         * @param w1 (String) word #1 to check, must be shorter word.
         * @param w2 (String) word #2 to check, must be longer word.
         * @return (boolean) true if jump is valid, false if not.
         */
        if (w2.length() - w1.length() != 1) {
            return false;
        }
        int mismatches = 0;
        int offset = 0;
        for (int i = 0; i < w1.length(); i++) {
            if (w1.charAt(i) != w2.charAt(i + offset)) {
                mismatches++;
                offset++;
            }

            if (mismatches > 1) {
                return false;
            }
        }
        if (mismatches == 1 && offset > 0) {
            // If the longer word has an extra char at the end after the loop ends, there might be two mismatches.
            return false;
        }
        return true;
    }
}
