/*
Data Structures >> (CS214).

Description: Write a program that accept an integer number from user in case
these number is positive check and print number is even or odd.

Author: yusufadell

*/

import java.util.Scanner;

class PostTest {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.println("Enter A Number- ");
        int num = sc.nextInt();
        sc.close();

        if (num > 0 && num % 2 == 0) {
            System.out.println(num + " is even");

        } else if (num > 0 && num % 2 == 1) {
            System.out.println(num + " is odd");

        } else {
            System.out.println("Your number: " + num);

        }
    }
}