/*
Operating System(OS) >> (CS341).

Description: Program that Check if the number is even or odd.

Author: yusufadell
*/

import java.util.Scanner;

public class FindEvenOrOdd {
    public static void main(String[] args) {
        int a;
        Scanner sc = new Scanner(System.in);
        System.out.println("Please enter a number to check even or odd: ");
        a = sc.nextInt();
        if (a % 2 == 0) {
            System.out.println("Entered number is an even number.");
        } else {
            System.out.println("Entered number is an odd number.");
        }
        sc.close();
    }
}