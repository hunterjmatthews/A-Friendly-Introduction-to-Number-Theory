# Linear Equations and the Greatest Common Divisor
### Problem 3
The method for solving $ax + by = gcd(a, b)$ described in this chapter involves a considerable amount of manipulation and back substitution. This exercise describes an alternative way to compute $x$ and $y$ that is especially easy to implement on a computer.
- __(A)__. Show that the algorithm described in Figure 1 computes the greatest common divisor $g$ of the positive integers $a$ and $b$, together with a solution $(x,y)$ in integers to the equation $ax+by=gcd(a,b$)
- __(B)__. Implement the algorithm on a computer using the computer language of your choice.
- __(C)__. Use your program to compute $g = gcd(a,b)$ and integer solutions to $ax+by=g$ for the following pairs $(a,b)$
  - __(1)__. $(19789, 23548)$ 
  - __(2)__. $(31875, 8387)$ 
  - __(3)__. $(22241739, 19848039)$
- __(D)__. What happens to your program if $b = 0$? Fix the program so that it deals with this case correctly. 
- __(E)__. For later applications, it is useful to have a solution with $x > 0$. Modify your program so that it always returns a solution with $x > 0$.
