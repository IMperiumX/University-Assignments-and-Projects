/*
Data Structures >> (CS214).

Description: Write java program to accept the width & height of rectangle from
the user and calculate the area.


*/

import java.util.Scanner;

class CalcRec {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in); // System.in is a standard input stream
        System.out.print("Enter Rectangle Width- ");
        float width = sc.nextFloat();

        System.out.print("Enter Rectangle Height- ");
        float height = sc.nextFloat();
        float area = width * height / 2;

        System.out.println("Rectangle Area: " + area);
        sc.close();
    }
}
