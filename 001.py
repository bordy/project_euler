"""
Project Euler Problem #1
=========================

If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""


def FindNumbers(amount):
  """Finds all numbers from 0 to amount, above which are multiples of 3 or 5
  and adds them together"""
  
  correct = []
  total = 0
  digits = amount
  
  for i in range(amount):
    if ((i % 3 == 0) or (i % 5 == 0)):
      correct.append(i)
  
  for o in correct:
    if correct.count(o) > 1:
      o.remove(i)
    total += o
    
  print total()
  return total()

FindNumbers(1000)