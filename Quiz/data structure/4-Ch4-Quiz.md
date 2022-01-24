# Stack Quiz

## 1- What is the basic difference between a stack and a queue?

```
A stack allows access to only one data item which is the last item
inserted.
If you remove this item, then you can access the next-to-last item inserted, and so on.
```

##

## 2- Scientific applications for the stack are ----- ,and -----?

>> [**Reverse a word**](https://www.codingame.com/playgrounds/6527/stack-reverse-a-string-using-stack) and [**check valid parentece**](https://www.geeksforgeeks.org/check-for-balanced-parentheses-in-an-expression/).

##

### 3- Assume that numbers 10, 22, 33, 48, 11 are pushed on a stack, two numbers are popped, then numbers 18, 444 are pushed on the stack, and three numbers are popped. What remains on the stack?

```
two numbers are popped >> 10, 22, 33

numbers 18, 444 are pushed >> 10, 22, 33, 18, 444

three numbers are popped >> **10, 22**
```

##

## 4- Write the complexity or big O of stack?

**Space and Time**

|operation |big(O)|
|:--------:|:----:|
|   pop    | O(1) |
|   push   | O(1) |
|   peek   | O(1) |

`B.S: O(1) has nothing to do with time!!`

#### It means the number of operations is not changing with the incearsing of stack size

##

## 5- For the class Stack, write method displayStackStartingAtBottom() that displays the content of the stack starting from the element on the bottom

```

**implement another stack and what you pop from the first one you push it to the other stack.**
```

>> What is the running time of the algorithm?

```
O(1)

```

# Queue Quiz

**TODO**
