## Chapter 1 Quiz

<details>
<summary>1- Define data structure and algorithm.</summary>
<br>

<a href="https://www.geeksforgeeks.org/data-structures/" target="_blank">Data Structure</a>: A data structure is the organization of data in a computer's memory or in a disk file

<p></p>

<a href="https://www.geeksforgeeks.org/introduction-to-algorithms/" target="_blank">Algorithm</a>: An algorithm is a procedure for carrying out a particular task
<p></p>
</details>

##

<details>
<summary>
2- What is the difference between program and algorithm?

</summary>

```
- An algorithm is more like an idea, a way to solve a problem.

- A program is more linked to the execution of one or more tasks by a computer.
```

<p></p>
</details>

##

<details>
<summary>
3- Using the <a href="https://www.freecodecamp.org/news/big-o-notation-why-it-matters-and-why-it-doesnt-1674cfa8a23c/" target="_blank">big-O notation</a> write the asymptotic upper bounds for the following expressions:

```
a- n^3 + 10n + 100n

b- 40n^5 + 3n

c- n log(n) + 200 log(n)
```

</summary>

Answer:

```
a- n^3

b- n ^ 5

c- n log(n)
```

</details>

##

<details>
<summary>
4- Sort Ascending:
<<<<<<< HEAD
=======

>>>>>>> 638adae (Section 9 (Functions) tasks)
```
[200 log(log(n)), log(n), n!, n^3]
```
</summary>

Sorted:

```
200 log(log(n)) < log(n) < n^3 < n!
```

<p></p>
</details>

##

<details>
<summary>5- Explain time complexity of:

```java
int sum = 0;
for(int i=0; i<n; i++)
for(int i=0; i<n*n; i++)
sum++;
```

</summary>

Complexity: O(n^2) Two nested for loops
<p></p>

</details>

##

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

Complexity: O(n^3) Three nested for loops
<p></p>
</details>

##

<details>
<summary>7- Order the following functions by ascending growth.

```
a- c3n^8,  n^3,  n^2 + c2n,  n!,  n log(n),  2^n,  log(n)
```

</summary>

Ascending Growth:

`log(n) < n log(n) < n < c2n < n^2 < n^3 < c3n^8.`
<p></p>
</details>
