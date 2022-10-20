"""
                        Chapter 16: Powers Modulo m and Successive Squaring
Problem 16.2:
The method of successive squaring described in the text allows you to compute ak (mod m) quite efficiently,
but it does involve creating a table of powers of a modulo m.

(b) Implement the above algorithm on a computer using the computer language of your choice.

(c) Use your program to compute the following quantities:
(i) 21000 (mod 2379) (ii) 5671234 (mod 4321) (iii) 47258008 (mod 1315171)

@Author = Hunter Matthews
@Date = 10/19/22

"""

# Part (b)
def successive_squaring(a, k, m):
    b = 1
    while k >= 1:
        if k % 2 != 0:
            b = (a * b) % m
        a = pow(a, 2)
        k = k // 2
    return b

if __name__ == "__main__":
    # Part (c.i)
    a, k, m = 2, 1000, 2379
    print(f"{a}^{k} ≡ {successive_squaring(a, k, m)} (mod {m})")
    # Part (c.ii)
    a, k, m = 567, 1234, 4321
    print(f"{a}^{k} ≡ {successive_squaring(a, k, m)} (mod {m})")
    # Part (c.iii)
    a, k, m = 47, 258008, 1315171
    print(f"{a}^{k} ≡ {successive_squaring(a, k, m)} (mod {m})")
