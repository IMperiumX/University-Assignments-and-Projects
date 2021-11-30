
1- Write the bubbleSort() **method** code in descending
order? How many comparisons does a bubble sort
perform in sorting N items?
```java
public void bubbleSort()
{
int out, in;
    for(out=nElems-1; out>1; out--)
        for(in=0; in<out; in++)
            if( a[in] < a[in+1] )
                swap(in, in+1);
}

Comparisons: N^2/2
```
## 

2- Write bubble sort algorithm that contains both
**bubbleSort1** and **bubbleSort2** methods. Where after the
first pass of bubbleSort1, the largest element is
guaranteed to be at the end of the array, after the second
pass, the second largest element is at second end of the
array, and so on. Also, after the first pass of
bubbleSort2, the smallest element is guaranteed to be at
index 0, after t he second pass, the second smallest is at
index 1, and so on.


- **bubbleSort1** >> assending order sorting.....
- **bubbleSort2** >> descending order sorting.....

##

3- A bubble sort of 10,000 elements takes about 1 second
on a certain computer. About how long will it take on
50,000 elements?


`Time complixty: O(N^2) ignoring (-1) for large size input!`

|    operations   | time|
|-----------------|:---:|
|(10 ^ 3) ^ 2     |1 sec|
|(50 * 10 ^ 3) ^ 2|x sec|

Ans: ((((50 * 10 ** 3)) ** 2 * 1) / (10 ** 3) ** 2) --> 50 ** 2 = **2500.0 sec**.

## 

4- We need sort the following array [2 1 5 4 3 6] of integers
into ascending order:

```java
public void bubbleSort()
{
int [] a = {2, 1, 5, 4, 3, 6};
int nElems = a.length;
int out, in;
    for(out=nElems-1; out>1; out--)
        for(in=0; in<out; in++)
            if( a[in] > a[in+1] )
                swap(in, in+1);
}
```

**a,b,c,d T3a 3Dny!!!!!!**

##

a- If bubble sort is chosen to sort this array, write the
contents of the array each time that the sort algorithm
changes it. How many comparison operations and how
many swaps are performed in the sorting?

##

b- If selection sort is chosen to sort this array, write the
contents of the array each time that the sort algorithm
changes it. How many comparison operations and how
many swaps are performed in the sorting?

##

c- If insertion sort is chosen to sort this array, write the
contents of the array each time that the sort algorithm
changes it. How many comparison operations and how
many swaps are performed in the sorting?

##


d- Use merge sort to sort the provided array. Be sure to
show your work. For example, show the substeps of merge sort using recursion trees.
