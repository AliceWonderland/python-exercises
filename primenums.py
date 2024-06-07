#find all prime nums in list
#prime num can only be divided by 1 * itself
#if n is divisible by any num from 2 to n then it is not prime
#time iteration, space constant variables
#not efficient

#test only odd numbers from 3 to n

def isprime(num):
    for n in range(2,num,1):
        if num%n == 0: return False
        continue

    return True

def getprimes(lst):
    primeset = set()
    for n in lst:
        if isprime(n):
            primeset.add(n)

    return primeset

numlist = [0,1,2,3,4,5,11,19,44,66]
print(getprimes(numlist))
print(isprime(3))

#recursion
def recurseprime(num, iterator=2):
    print(num, iterator, num%iterator)
    if num == 0 or num == 1 or num < 0: return False
    if num == 2 or num == 3: return True
    if num == iterator: return True

    if num%iterator == 0:
            return False

    return recurseprime(num, iterator+1)

x=4
print("isprime", x, recurseprime(x))

#tests
#???

