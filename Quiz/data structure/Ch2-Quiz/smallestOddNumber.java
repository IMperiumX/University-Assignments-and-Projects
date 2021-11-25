public class smallestOddNumber {
    public static void main(String[] args) {
        int arr[] = { 564, 345, 345, -345, 0, 57, 76, 87, 4, 532 };
        index = 0;
        while (arr[index] % 2 == 0)
            index++; // skip even numbers
        min = arr[index++]; // first odd number
        while (index < length) {
            if (arr[index] % 2) {
                if (arr[index] < min)
                    min = arr[index];
            }
            index++;
        }
    }
}