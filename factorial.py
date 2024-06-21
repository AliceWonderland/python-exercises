#return a factorial (product of all numbers from 1 to x)

import math

def gimmefactorial(startnum):
    if startnum < 0: return None

    product = 1
    for num in range(startnum, 0, -1): #decrements from startnum to 1
        product *= num

    return product

print(gimmefactorial(5))
print(gimmefactorial(3))
print(gimmefactorial(0))
print(gimmefactorial(-1))
print(gimmefactorial(-4))
# print(gimmefactorial())

factorial = math.factorial(4)
print(factorial)

#recursion
def recursefactorial(n):
    if n < 0: return None

    if n == 1 or n == 0:
        return n
    else:
        return n*recursefactorial(n-1)

print(recursefactorial(3))
print(recursefactorial(0))
print(recursefactorial(-4))
print(recursefactorial(-1))