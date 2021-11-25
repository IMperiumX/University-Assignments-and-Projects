public class OddEvenSumArray {

    public static void main(String args[]) {

        int arr[] = { 13, 44, 58, 67, 70, 85 };
        int evenSum = 0;
        int i = 0;

        while (i < 6) {

            if (arr[i] % 2 == 0) {
                evenSum = evenSum + arr[i];
            }

            i++;
        }

        System.out.println("\nSum of even is: " + evenSum);
        System.out.println("\nSum of odd is: " + oddSum);
    }
}