## Ordered Array Quiz



1- What is the difference of big O for inserting, deleting, and
getting an item in Unordered array and ordered array?


|Algorithm |Running Time in Big(O) Notation|
|----------|:-----------------------------:|
|Insertion in **unordered** array|   O(1)  |
|Insertion in **ordered**   array|   O(N)  |
|Deletion  in **unordered** array|   O(N)  |
|Deletion  in **ordered**   array|   O(N)  |


##

<details>
<summary>
2- Write a program that implement and tests the binary search method.
<p>
The program first creates an array of ten odd
numbers from 1 to 20. It displays this array and then
prompts the user to enter a key 11 for testing binary search.
</p>

</summary>

```java
class BinarySearchExample{  
 public static void binarySearch(int arr[], int first, int last, int key){  
   int mid = (first + last)/2;  
   while( first <= last ){  
      if ( arr[mid] < key ){  
        first = mid + 1;     
      }else if ( arr[mid] == key ){  
        System.out.println("Element is found at index: " + mid);  
        break;  
      }else{  
         last = mid - 1;  
      }  
      mid = (first + last)/2;  
   }  
   if ( first > last ){  
      System.out.println("Element is not found!");  
   }  
 }
 public static void main(String args[]){  
        int arr[] = {1, 3, 5, 7, 9, 11, 13, 15, 17, 19};
        Scanner sc = new Scanner(System.in);
        int key = sc.nextInt(); // User Enter 11 to test binary search should return 5 <-- index of 11
        sc.close();
        int last=arr.length-1;  
        binarySearch(arr,0,last,key);     
 }  
}  
```

</details>

##

<details>
<summary>

3- Suppose that the array shown below has 7 sorted elements.

Which values are tested during a binary search to determine
that the value 8 is not present, and in what order are they
tested?
‫</summary>

<b>Answer: 7 --> 12 --> 9</b>

<p><b>Explination:</b></p>

```
first, last = 0, 6
mid = 3 
guess = List[mid] --> 7
key > guess || 8 > 7
first = mid + 1 <-- Cut the left side
Loop again testing the guess --> index 5 (12)
Then you end up with an Array of one element(9)
```

</details>


##

<details>
<summary>
4- Can we apply binary search algorithm when searching for
value 5 within the following array 44, 13, 1, 100, 234,
121, 55, 16? Explain why?
</summary>
<p></p>
Answer:
<p></p>

<p><b>No we can't</b></p>

<p>We can't apply binary search algorithm when searching for a value in <b>unordered</b> array.</p>


</details>


##

<details>
<summary>
5- Given an n-element array, an algorithm chooses half of the
elements from the array at random and executes an O(n)
time calculation for each element. What is the running time
of this algorithm?
</summary>

```
Running time: Logarithmic Time O(log(N))
```


</details>


##
<details>
<summary>
6- Write Big O of the following code?

```java
i = n;
while(i > 0)
{
if(binarySearch(list, i))
System.out.println("Found");
i--;
}
```
</summary>


```
Ans: O(N)
worst case here that could be no such element to Found....!
```

</details>