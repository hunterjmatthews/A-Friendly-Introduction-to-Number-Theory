"""
                        Chapter 15: Mersenne Primes and Perfect Numbers
Problem #7:
(a) Write a program to compute sigma(n), the sum of all the divisors of n (including 1 and n itself).
You should compute sigma(n) by using a factorization of n into primes, not by actually finding all
the divisors of n and adding them up.

(b) As you know, the Greeks called n perfect if sigma(n) = 2n. They also called n abundant if sigma(n) > 2n,
and they called n deficient if sigma(n) < 2n. Count how many n's between 2 and 100 are perfect, abundant, and
deficient. Clearly, perfect numbers are very rare. Which do you think are more common, abundant numbers or
efficient numbers? Extend your list for 100 < n <= 200 and see if your guess still holds.

@Author = Hunter Matthews
@Date = 10/19/22

"""


def find_sum(n):
    d = [0] * (n + 1)
    result = 1

    find_prime_factors(n, d)

    current_factor = d[n]

    power = 1
    while n > 1:
        n //= d[n]

        if current_factor == d[n]:
            power += 1
            continue

        sum = 0

        for i in range(power + 1):
            sum += pow(current_factor, i)

        result *= sum

        current_factor = d[n]
        power = 1

    return result


def find_prime_factors(n, d):
    # Creates a boolean list of primes[0...n] and initializes all entries as false.
    prime = [False] * (n+1)

    for i in range(2, n+1, 2):
        d[i] = 2

    for i in range(3, n+1, 2):
        if prime[i] == False:
            d[i] = i
            for j in range(i, (n+1) // i, 2):
                if prime[i*j] == False:
                    prime[i * j] = True

                    d[i*j] = i


def the_greeks():
    # Declarations:
    perfect, abundant, deficient = 0, 0, 0

    for i in range(2, 200):
        sigma = find_sum(i)
        if sigma == 2 * i:
            print(f"{i} is perfect!")
            perfect += 1
        if sigma > 2 * i:
            print(f"{i} is abundant!")
            abundant += 1
        if sigma < 2 * i:
            print(f"{i} is deficient!")
            deficient += 1
    print(f"There are {perfect} perfect numbers, {abundant} abundant numbers, and {deficient} deficient numbers.")

if __name__ == "__main__":
    # Part (a)
    n = 28
    print(f"The sum of the factors is: {find_sum(n)}")
    # Part (b)
    the_greeks()
