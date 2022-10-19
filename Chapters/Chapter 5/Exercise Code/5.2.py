"""
        Ch. 5: Divisibility and the Greatest Common Divisor
Problem 2: Write a program to compute the greatest common divisor gcd(a, b) of
two integers a and b. Your program should work even if one of a or b is zero.
Make sure that you don’t go into an infinite loop if a and b are both zero!

@Author: Hunter Matthews
@Date: 10/19/22

"""

def gcd(a, b):
    # If the value of b is 0, return value a.
    if b == 0:
        return a
    # Else recursively call the function 'gcd' with value (b, a % b)
    else:
        return gcd(b, a % b)

if __name__ == "__main__":
    # Change values 'a' and 'b' to be anything you want.
    print(gcd(32,22))
