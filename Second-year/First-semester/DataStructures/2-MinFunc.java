/*
Data Structures >> (CS214).

Description: Java Program that Takes Two parameter and return the smallest number.


*/

import java.util.Scanner;

class MinFunc {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in); // System.in is a standard input stream
        System.out.print("Enter First Number- ");
        double num1 = sc.nextDouble();

        System.out.print("Enter Second Number- ");
        double num2 = sc.nextDouble();
        sc.close();

        if (num1 < num2) {
            System.out.print("Smallest number: " + num1);
        } else {
            System.out.print("Smallest number" + num2);
        }

    }
}