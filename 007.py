"""
Project Euler Problem #7
=========================

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
that the 6^th prime is 13.

What is the 10001^st prime number?
"""

def nthPrime(n):
    a = [2]
    cur = 3

    while len(a) < n:
        cur += 2

        if (cur % 2 == 0):
            continue

        for j in a:
            if ( cur % j == 0 ):
                break
        else:
            a.append(cur) 
    else:
        return max(a)
        
print(nthPrime(10001))