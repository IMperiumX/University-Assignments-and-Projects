/*

Operating System(OS) >> (CS341).

Description: Write a program in Java that user submit three numbers and find
the maximum and minimum and the average of them.


*/

import java.util.Scanner;

public class MaxMinAvr {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.print("Enter the first number: ");
        int num1 = scan.nextInt();
        System.out.print("Enter the second number: ");
        int num2 = scan.nextInt();
        System.out.print("Enter the third number: ");
        int num3 = scan.nextInt();
        scan.close();
        int[] nums = { num1, num2, num3 };
        System.out.println("The smallest of entered numbers is: " + getMinValue(nums));
        System.out.println("The largest of entered numbers is: " + getMaxValue(nums));
        System.out.println("The average of entered numbers is: " + avr(num1, num2, num3));
    }

    public static int avr(int a, int b, int c) {
        return (a + b + c) / 3;
    }

    public static int getMaxValue(int[] numbers) {
        int maxValue = numbers[0];
        for (int i = 1; i < numbers.length; i++) {
            if (numbers[i] > maxValue) {
                maxValue = numbers[i];
            }
        }
        return maxValue;
    }

    public static int getMinValue(int[] numbers) {
        int minValue = numbers[0];
        for (int i = 1; i < numbers.length; i++) {
            if (numbers[i] < minValue) {
                minValue = numbers[i];
            }
        }
        return minValue;
    }
}
