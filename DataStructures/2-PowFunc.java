/*
Data Structures >> (CS214).

Description: Java Programm that calculate a numer $num to the power $pow 
pow(num, pow).

Author: yusufadell
*/

import java.util.Scanner;

class PowFunc {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in); // System.in is a standard input stream
        System.out.print("Enter Base Number- ");
        double base = sc.nextDouble();

        System.out.print("Enter The Power- ");
        double power = sc.nextDouble();
        sc.close();

        System.out.printf("%.2f to the power of %.2f = %.2f: ", base, power, Math.pow(base, power));

    }
}