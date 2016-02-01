/**
 * Created by wendyjan on 1/31/16.
 */
public class Week1_easy1 {

    public static void main(String[] args) {
        int year = 1988;
        System.out.println(Integer.toString(year) + " is the year of the " + getZodiac(year) + ".");
    }

    public static String getZodiac(int birthYear) {
        /**
         * Returns the Chinese zodiac animal of the year specified in birthYear parameter.
         *
         * @param birthYear (int) birth year with an unknown Chinese zodiac.
         * @return (String) Chinese zodiac animal of that year.
         */
        String[] zodiacs = {"Monkey", "Rooster", "Dog", "Pig",
                            "Rat", "Ox", "Tiger", "Rabbit",
                            "Dragon", "Snake", "Horse", "Goat"};
        int signIndex = birthYear % 12;
        return zodiacs[signIndex];
    }
}

