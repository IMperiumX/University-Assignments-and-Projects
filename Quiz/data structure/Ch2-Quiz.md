## Unordered Array Quiz [Part2 Ordered Array](./part2-Ch2-Quiz.md)            

<details>
<summary>
1- Write an algorithm for calculating a sum of the array
elements.
</summary>

```java
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

```


</details>

## 

<details>
<summary>
2- Write an algorithm that for a given array calculates and returns the product of all even array elements?
</summary>

```java
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


```

</details>

##

<details>
    <summary>
3- Write an algorithm that for a given array finds and returns
the smallest array element.
</summary>

```java
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
```

</details>

##

<details>
<summary>
4- What does method f do? If it takes 10 seconds to run f on
array of size 100, how long it takes to run it on the array of
size 400.
</summary>

<b>Answer -->  ((400 ** 3) * 10) / 100 ** 3 = 640 seconds. </p>


<p><b>Explaination:</b></p>


Time complixity: <b>O(n^3)</b>


(size = 100 : operations = 100 ^ 3, time = 10) & (size = 400 : operations = 400 ^ 3, time = <b>X</b>)

```java
public class bigOCalc {
    int f(int n, int[] a) {
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                for (int k = 0; k < n; k++) {
                    if (i != j && j != k && i != k) {
                        if (a[i] == a[j] && a[j] == a[k])
                            return 1;
                    }
                }
            }
            return 0;
        }
    }
}
```

</details>

<br>

<details>
<summary>
5- Write Java program that finds the smallest odd number in a
given array of integers. What is the running time of the
algorithm?
</summary>

<b>Running Time: O(n)</b>

```java
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

```
</details>


