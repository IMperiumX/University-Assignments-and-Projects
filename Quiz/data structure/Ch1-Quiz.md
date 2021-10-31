## Chapter 1 Quiz


<details>
<summary>1- Define data structure and algorithm.</summary>
<br>
<a href="https://www.geeksforgeeks.org/data-structures/" target="_blank">Data Structure</a>: Data organization, management, and storage format that enables efficient access and modification.

<p></p>

<a href="https://www.geeksforgeeks.org/introduction-to-algorithms/" target="_blank">Algorithm</a>: A finite sequence of well-defined instructions, typically used to solve a class of specific problems or to perform a computation
</details>

<br>

<details>
https://www.freecodecamp.org/news/big-o-notation-why-it-matters-and-why-it-doesnt-1674cfa8a23c/
<summary>
3- Using the <a href="https://www.freecodecamp.org/news/big-o-notation-why-it-matters-and-why-it-doesnt-1674cfa8a23c/" target="_blank">big-O notation</a> write the asymptotic upper bounds for the following expressions:

```
a- n^3 + 10n + 100n

b- 40n^5 + 3n

c- n log(n) + 200 log(n)
```
</summary>
<br>

```
a- n^3

b- n ^ 5

c- n log(n)
```
</details>

<details>
<summary>

4- Sort Ascending: 
```
[200 log(log(n)), log(n), n!, n^3]
``` 
</summary>
<br>
Sorted:-

```
[200 log(log(n)), log(n), n^3, n!]
```

</details>



<details>
<summary>5- Explain time complexity of:

```java
int sum = 0;
for(int i=0; i<n; i++)
for(int i=0; i<n*n; i++)
sum++;
```
</summary>
<br>
Complexity: O(n^2) Two nested for loops
<p></p>

</details>


<details>
<summary>6- Explain time complexity of:

```java
int x,j,k = 0;
for(int i=0; i<n; i++)
for(int j=0; j<n; j++)
for(int k=0; k<n; k++)
x = x + 1;
```
</summary>
<br>
Complexity: O(n^3) Three nested for loops
<p></p>
</details>




</details>
<details>
<summary>7- Order the following functions by ascending growth.
a- c3n^8,  n^3,  n^2 + c2n,  n!,  n log(n),  2^n,  log(n)
</summary>
<br>
Ascending Growth: log(n), n log(n), n, c2n, n^2, n^3, c3n^8.
</details>
