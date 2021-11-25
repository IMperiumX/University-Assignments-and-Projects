public class SmallestInArrayExample {
    public static void main(String args[]) {
        int a[] = { 564, 345, 345, -345, 0, 57, 76, 87, 4, 532 };

        int smallest = a[0];
        for (int i = 0; i < a.length; i++) {
            if (a[i] < smallest) {
                smallest = a[i];
            }

        }
        System.out.println("Smallest element in array is: " + smallest);
    }
}