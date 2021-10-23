/*
Data Structures >> (CS214).

Description: Write a program that accept 10numbers from the user and print out
sum of even numbers and sum of odd numbers.

Author: yusufadell
*/



import java.util.Scanner;


// foor loop

class OddEvenSum
{
    public static void main (String args[])
    {
        int i, num; //declare variable i,num
        int oddSum = 0, evenSum = 0;
        //declare and initialize variables oddSum,evenSum
        Scanner scan = new Scanner(System.in);
        //create a scanner object for input
        System.out.print("Enter the number for num: \n");
        num = scan.nextInt(); //reads num1 from user
        for(i = 1; i <= num; i++)
        {
            if(i % 2 == 0)
                evenSum = evenSum + i;
            else
                oddSum = oddSum + i;
        }
        System.out.println("Sum of all odd numbers are: " + oddSum);
        System.out.println("Sum of all even numbers are: " + evenSum);
    }
}


// While loop

/*import java.util.Scanner;
class OddEvenSumWhile
{
    public static void main (String args[])
    {
        int i, num; //declare variable i,num
        int oddSum = 0, evenSum = 0;
        //declare and initialize variables oddSum,evenSum

        Scanner scan = new Scanner(System.in);
        //create a scanner object for input

        System.out.print("Enter the number for num: \n");
        num = scan.nextInt(); //reads num1 from user

        i = 1;
        while(i <= num)
        {
            if(i % 2 == 0)
                evenSum = evenSum + i;
            else
                oddSum = oddSum + i;
            i++
        }
        System.out.println("Sum of all odd numbers are: " + oddSum);
        System.out.println("Sum of all even numbers are: " + evenSum);
    }
}
*/

// using do-while loop


/*import java.util.Scanner;
class OddEvenSumWhile
{
    public static void main (String args[])
    {
        int i, num; //declare variable i,num
        int oddSum = 0, evenSum = 0;
        //declare and initialize variables oddSum,evenSum

        Scanner scan = new Scanner(System.in);
        //create a scanner object for input

        System.out.print("Enter the number for num: \n");
        num = scan.nextInt(); //reads num1 from user

        i = 1;
        while(i <= num)
        {
            if(i % 2 == 0)
                evenSum = evenSum + i;
            else
                oddSum = oddSum + i;
            i++
        }
        System.out.println("Sum of all odd numbers are: " + oddSum);
        System.out.println("Sum of all even numbers are: " + evenSum);
    }
}*/