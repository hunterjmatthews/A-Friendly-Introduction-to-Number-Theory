"""
        Ch. 5: Divisibility and the Greatest Common Divisor
Write a program to implement the 3n + 1 algorithm described in the previous exercise.
The user will input n and your program should return the length L(n) and the terminating
value T(n) of the 3n + 1 algorithm. Use your program to create a table giving the length
and terminating value for all starting values 1 ≤ n ≤ 100.

@Author: Hunter Matthews
@Date: 10/19/22

"""


def step(n):
    # If n mod 2 is equal to 0... return integer division of n and 2.
    if n % 2 == 0:
        return n // 2
    # Else return 3 times n plus 1.
    else:
        return 3 * n + 1


def steps_count(n):
    # Declare length to be 0.
    length = 0
    # While n is not equal to 1
    while n != 1:
        # Print first value followed by a comma.
        print(n, end=",")
        # Length is now set to length plus 1.
        length = length + 1
        # n is now set equal to the return of the 'step' function.
        n = step(n)
    # Display the last n value and the length.
    print(f"{n} -> Length: {length}")


if __name__ == "__main__":
    # Ask for user input
    n = int(input("Input an N: "))
    # Send user input to the function 'steps_count'
    print(steps_count(n))
