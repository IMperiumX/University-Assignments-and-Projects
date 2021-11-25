import java.util.Scanner;

class SumOfElementsOfAnArray {
    public static void main(String[] args) {
        System.out.println("Enter the required size of the array :: ");
        Scanner s = new Scanner(System.in);
        int size = s.nextInt();
        int myArray[] = new int[size];
        int sum = 0;
        System.out.println("Enter the elements of the array one by one ");
        for (int i = 0; i < myArray.length; i++) {
            myArray[i] = s.nextInt();
            sum = sum + myArray[i];
        }

        System.out.println("The sum of array elements is: " + sum);
    }

}