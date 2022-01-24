/*
Data Structures >> (CS214).

Description: Write java program that accept numbers from the user and check
chice:

--Choice= 1 >> num1 + num2
--Choice= 2 >> num1 * num2
--Choice= 3 >> num1 % num2


Author: yusufadell
*/

import java.util.Scanner;

class CheckChoice {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter  First Number- ");
        float num1 = sc.nextFloat();

        System.out.print("Enter  Second Number- ");
        float num2 = sc.nextFloat();

        System.out.print("Enter A Chice(1-3) 1- (+), 2- (*), 3- (%)");
        int choice = sc.nextInt();
        sc.close();
        switch (choice) {
        case 1:
            System.out.printf("%.2f + %.2f = %.2f", num1, num2, num1 + num2);
            break;
        case 2:
            System.out.printf("%.2f * %.2f = %.2f", num1, num2, num1 * num2);
            break;
        case 3:
            System.out.printf("%.2f mod %.2f = %.2f", num1, num2, num1 % num2);
            break;

        }

        /*
         * Hard Coded Solution (not recommended!)
         * 
         * if (choice == 1){ System.out.println(num1 + " + " + num2 + " = " + addition);
         * 
         * }else if (choice == 2){
         * 
         * System.out.println(num1 + " * " + num2 + " = " + num1 * num2);
         * 
         * }else if (choice == 3){ System.out.println(num1 + " % " + num2 + " = " + num1
         * % num2); }
         */
    }
}
