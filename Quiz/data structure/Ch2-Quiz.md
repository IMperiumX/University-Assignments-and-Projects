## Unordered Array Quiz

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
<br>

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
<br>

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

<br>

<details>
<summary>
4- What does method f do? If it takes 10 seconds to run f on
array of size 100, how long it takes to run it on the array of
size 400.
</summary>

<b>Ans -->  ((400 ** 3) * 10) / 100 ** 3 = 640 seconds.

<br>
Explaination:
</b>
Time complixity: <b>O(n^3)</b>

<br>
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


## Ordered Array Quiz

1- What is the difference of big O for inserting, deleting, and
getting an item in Unordered array and ordered array?


2- Write a program that implement and tests the binary search
method. The program first creates an array of ten odd
numbers from 1 to 20. It displays this array and then
prompts the user to enter a key 11 for testing binary search.


3- Suppose that the array shown below has 7 sorted elements.
Which values are tested during a binary search to determine
that the value 8 is not present, and in what order are they
tested?
‫
+----+----+----+----+----+----+----+
| 3 | 5 | 6 |
7 | 9 | 12 | 17 |
+----+----+----+----+----+----+----+


4- Can we apply binary search algorithm when searching for
value 5 within the following array 44, 13, 1, 100, 234,
121, 55, 16? Explain why?


5- Given an n-element array, an algorithm chooses half of the
elements from the array at random and executes an O(n)
time calculation for each element. What is the running time
of this algorithm?


6- Write Big O of the following code?

i = n;
while(i > 0)
{
if(binarySearch(list, i))
System.out.println("Found");
i--;
}