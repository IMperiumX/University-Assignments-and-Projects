/*
Operating System(OS) >> (CS341).

Description: Program that converts a human height given in feet and inches to centimeters

Author: yusufadell
*/

import java.util.Scanner;
class Convert
{
    public static void main(String[] args)
    {
        Scanner scan = new Scanner(System.in);
        System.out.print("Please enter the height in feet: ");
        double feet = scan.nextInt();
        System.out.print("Please enter the height in inch: ");
        double inch = scan.nextInt();
        Conversion_feet_to_cm(feet);
        Conversion_inch_to_cm(inch);
        scan.close();
    }
    static double Conversion_feet_to_cm(double feet)
    {

        double centimeter  = 30.48 * feet;
        System.out.printf("Value in Centimeter is: %.2f \n", centimeter);
        return 0;
    }
    static double Conversion_inch_to_cm(double inch)
    {
        double centimeter  = 2.54 * inch;
        System.out.printf("Value in Centimeter is: %.2f \n", centimeter);
        return 0;
    }

}