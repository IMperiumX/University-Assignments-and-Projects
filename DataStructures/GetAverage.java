/*
Data Structures >> (CS214).

Description: Write a program that calculates and print out the average grade
for 6 stuents.

Code Overview:

3 main methods:

0)GetAverage() >> initialize the program by running the following 3 functions.

1)getUserNums() >> capture the user input as a one line of numbers seperated by spaces.
                    e.g1 2 3 4 5"

2)userAvg() >>  get list of strings(numbers) by splitting on space " "
        e.g "1 2 3 4 5" becomes ["1","2","3","4","5"]
        Then get the sum of the numbers in the list and devide over their count.

3)printAverage >> print formatted string with the average of the numbers

##format string is like a template for hard coded string with a variables inside


Author: yusufadell
*/

import java.util.Scanner;

public class GetAverage {

    public GetAverage() {
        String getStr = getUserNums();
        double result = userAvg(getStr);
        printAverage(getStr, result);

    }

    public String getUserNums() {
        Scanner in = new Scanner(System.in);
        System.out.println("Please enter six numbers separated by spaces: ");
        in.close();
        return in.nextLine();

    }

    public static double userAvg(String str) {
        String[] arr = str.split(" ");
        double sum = 0.0;
        double average = 0.0;
        for (int i = 0; i < arr.length; i++) {
            sum += Integer.parseInt(arr[i]);
        }
        if (arr.length > 0) {
            average = sum / arr.length;
        }

        return average;
    }

    public static void printAverage(String userNumInput, double average) {
        System.out.printf("The average of the numbers " + userNumInput + " is %.2f", average);

    }

    public static void main(String[] args) {
        new GetAverage();

    }
}