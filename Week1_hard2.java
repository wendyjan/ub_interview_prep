/**
 * Created by wendyjan on 2/1/16.
 */
public class Week1_hard2 {

    public static void main(String[] args) {

        // TODO is there a better choice of built-in Java class to contain our matrix?
        // Using a 2D arrays of ints isn't the best, because it could allow each row to have a different # of cols.
        int[][] testerMatrix = new int[][]{
                { 1, 2, 3, 4, 5 },
                { 6, 7, 8, 9, 10 },
                { 11, 12, 13, 14, 15 },
                { 16, 17, 18, 19, 20 },
                { 21, 22, 23, 24, 25 }
        };
        printRowThenCol(testerMatrix);
    }

    public static void printRowThenCol(int[][] mat) {
        /**
         * Prints a matrix in the following fashion:
         * Starts at the top left corner of the matrix.
         * Moves horizontally across a single row, printing each element in a row.
         * Then moves down a column and prints its elements in a row,
         * skipping the element that was printed during the previous row.
         * The trick is to print each element exactly one time.
         * Notice that the number of elements in each line of output will decrease.
         *
         * For example, given matrix:
         int[][] testerMatrix = new int[][]{
         { 1, 2, 3, 4, 5 },
         { 6, 7, 8, 9, 10 },
         { 11, 12, 13, 14, 15 },
         { 16, 17, 18, 19, 20 },
         { 21, 22, 23, 24, 25 }
         };
         * The ideal output is:
         * 1, 2, 3, 4, 5
         * 6, 11, 16, 21
         * 7, 8, 9, 10
         * 12, 17, 22
         * 13, 14, 15
         * 18, 23
         * 19, 20
         * 24
         * 25
         *
         * @param starter (String) the starter word of the chain.
         * @param allWords (String[]) the list of all allowable words.
         * @return (String) a representation of the longest chain of word jumps that begins with the starter.
         */
        int currRowStart = 0;
        int currColStart = 1;
        for (int row = 0; row < mat.length; row++) {
            // Print the row first.
            int currRow = currRowStart;
            String rowToPrint = ""; // TODO this is wildly inefficient. Make it into a char ArrayList.
            while (currRow < mat.length) {
                rowToPrint += mat[row][currRow];
                rowToPrint += " ";
                currRow++;
            }
            System.out.println(rowToPrint);
            // Then print the column.
            int currCol = currColStart;
            String colToPrint = "";
            while (currCol < mat[0].length) { // Again, we're assuming all rows all have the same # of columns.
                colToPrint += mat[currCol][currRowStart];
                colToPrint += " ";
                currCol++;
            }
            System.out.println(colToPrint);
            currRowStart++;
            currColStart++;
        }
    }


}
