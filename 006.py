"""
Project Euler Problem #6
=========================

The sum of the squares of the first ten natural numbers is,
                       1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is,
                    (1 + 2 + ... + 10)^2 = 55^2 = 3025

Hence the difference between the sum of the squares of the first ten
natural numbers and the square of the sum is 3025 385 = 2640.

Find the difference between the sum of the squares of the first one
hundred natural numbers and the square of the sum.
"""

def sum_of_sq(x):
    total = 0
    for i in range(x+1):
        total += i**2
    return total

def sq_of_sum(x):
    total = 0
    for i in range(x+1):
        total += i
    return total**2

def difference(x):
    print sq_of_sum(x) - sum_of_sq(x)
    
difference(100)