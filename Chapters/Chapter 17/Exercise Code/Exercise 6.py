"""
                        Chapter 17 - Computing k^th Roots Modulo m
Problem 17.6: Write a program to solve xk ≡ b (mod m). Give the user the option of providing
a factorization of m to be used for computing φ(m).

@Author: Hunter Matthews
@Date: 10/24/22
"""

# Calculate greatest common divisor
def gcd(a, b):
    if (a == 0):
        return b
    return gcd(b % a, a)

# Calculate Euluer's Totiet Function of a given number 'm'.
def euluers_totiet_function(m):
    result = 1
    for i in range(2, m):
        if (gcd(i, m) == 1):
            result += 1
    return result
    
# Solve the congruence and output the results.
def solve_congruence(k, b, m):
    # Declarations:
    result, u, v = 1, 1, 1
    
    # Step 1: Compute Euluer's Totiet Function.
    flag = input("Factor m before computing φ(m)? Enter 'y' or 'n': ")
    
    # If user entered 'y', use the user inputed 'm' values before computing Euluer's Totiet Function.
    if flag == 'y':
        p_factors = []
        amount_of_p_factors = int(input("Enter how many prime factors m has: "))
        for i in range(0, amount_of_p_factors):
            pf = int(input())
            p_factors.append(euluers_totiet_function(pf))
        for i in p_factors:
            result *= i
            
    # If user entered 'n', do not factor 'm' before computing Euluer's Totiet Function.
    else:
        result = euluers_totiet_function(m)
    # Step 2: Generate potential 'u' and 'v' values to solve the equation 'ku-φ(m)v = 1'
    for i in range(-1000, 1000):
        for j in range(1, 1000):
            eq = (k * i) - (result * j)
            if eq == 1:
                u = i + result
                v = (-j) + k
                break
    # Step 3: Solve the congruence and print the results.
    print(f"x ≡ {(b ** u) % m} (mod {m})")
    
# Driver
if __name__ == "__main__":
    print("Solve Congruence x^k ≡ b (mod m)")
    k, b, m = input("Enter a value for k, b, and m: ").split()
    solve_congruence(int(k), int(b), int(m))
