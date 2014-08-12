"""
Project Euler Problem 10
========================

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

nonprimes = []

n = 3
while n < 2000000:
	for i in range(3,n):
		if n % i != 0:
			nonprimes.append(n)
		n += 1


primes = [x for x in range(2000000) if x not in nonprimes]

final = 0
for i in primes:
	final += i

return final