


//Yusuf Adel Was Here.


import java.util.Scanner;


public class MilesConverter {

    public static void main(String[] args) {

        System.out.println("This program prints conversion tables.");
        System.out.println("Type a letter to select a conversion table");
        System.out.println("m\t\tmiles to kilometers");
        System.out.println("k\t\tkilometers to miles");
        System.out.println("p\t\tpounds to kilograms");
        System.out.println("x\t\texit the program");

        Scanner sc = new Scanner(System.in);
        String unit = sc.next();
        sc.close();
        if (unit.equals("m")) {
            double mile = 1;
            double km = 1.609 * mile;
            System.out.println("Miles\t\t Kilometers");
            for (int i = 10; i <= 100; i+=10 ) {
                System.out.printf(mile*i + "\t\t" + "%.2f %n", km*i);
            }
        } else if (unit.equals("k")) {
            double km = 1;
            double mile = 0.621*km;
            System.out.println("Kilometers\t\t Miles");
            for (int i = 10; i <= 100; i+=10 ) {
                System.out.printf(mile*i + "\t\t\t" + "%.2f %n", mile*i);
            }
        } else if (unit.equals("p")) {
            double pounds = 1;
            double kg = 0.45;
            System.out.println("Pounds\t\tKilograms");
            for(int i = 10; i <= 100; i+=10) {
                System.out.printf(pounds*i + "\t\t\t" + "%.2f %n", kg*i);
            }
        } else if (unit.equals("x")) {
            System.exit(0);
        } else {
            System.out.println("Enter a valid number, please! ");
        }
    }
}