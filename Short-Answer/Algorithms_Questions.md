# Analysis of Algorithms

## Exercise I

Give an analysis of the running time of each snippet of
pseudocode with respect to the input size n of each of the following:

```python
a)  a = 0
    while (a < n * n * n):
      a = a + n * n
```
<h4>O(n^3)</h4>
the big O = O(n^3).  This is because for any given input size n, the amount of operations to be performed will be n^3.
so if n = 2.  a total of 2^3 operations will be performed.  the operation in this example is calculating a + n * n and setting that back to a incrementally.



```
b)  sum = 0
    for i in range(n):
      j = 1
      while j < n:
        j *= 2
        sum += 1
```
<h4>O(2n^2)</h4>
the big O time complexity is O(2n^2).  This is because for any given input n, there are n operations performed, and for each n operation, another 2n operations are performed.  The for loop will be for the 1st n operations.  and the nested while loop will be n operations for each of the for loops n operations.  And the nested while loop is doing 2 operations per n, making it a total of O(2n^2) ~ O(n^2).  In the outer for loop, the operation is setting j = 1 and then for each iteration of the for loop, the while loop will carry out a total of n times, performing the 2 calculations of j = j * 2 and sum = sum + 1


```
c)  def bunnyEars(bunnies):
      if bunnies == 0:
        return 0

      return 2 + bunnyEars(bunnies-1)
```
<h4>O(n)</h4>
the big O for this simple recursive function is simply ~ O(n).  this is because for a given input of n, the function will perform ~ n function calls, considered an operation.  when it hits the base case of n = 0, it will return 0.  


## Exercise II

Suppose that you have an n-story building and plenty of eggs. Suppose also that an egg gets broken if it is thrown off floor f or higher, and doesn't get broken if dropped off a floor less than floor f. Devise a strategy to determine the value of f such that the number of dropped + broken eggs is minimized.

Write out your proposed algorithm in plain English or pseudocode AND give the runtime complexity of your solution.
