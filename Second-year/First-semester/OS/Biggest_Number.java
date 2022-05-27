/*
Operating System(OS) >> (CS341).

Description: Write a java program that accepts 3 numbers from user and pringt the largest.


*/

import java.util.Scanner;

public class Biggest_Number {
    public static void main(String[] args) {
        int x, y, z;
        Scanner s = new Scanner(System.in);
        System.out.print("Enter the first number:");
        x = s.nextInt();
        System.out.print("Enter the second number:");
        y = s.nextInt();
        System.out.print("Enter the third number:");
        z = s.nextInt();
        s.close();
        if (x > y && x > z) {
            System.out.println("Largest number is: " + x);
        } else if (y > z) {
            System.out.println("Largest number is: " + y);
        } else {
            System.out.println("Largest number is: " + z);
        }

    }
}