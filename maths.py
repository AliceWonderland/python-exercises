import math
#from math import pi to use reference pi instead of math.pi

#area circle based on radius
#A = pi r^2
radius = 6
print(math.pi * radius ** 2)

#calculate the diff between n and 17
#if diff > than 17, return twice absolute difference
def ifdiff(n):
    if (n < 0): return "None"

    diff = abs(n-17) #no need for abs() since neg*neg = pos number!
    if diff > 17:
        return diff*2
    else:
        return diff

print(ifdiff(40))


#sum of three given numbers
#if values are equal, return three times their sum
#1,2,3 vs 3,3,3
def summm(x,y,z):
    if (x == y == z):
        return (x+y+z)*3
    else:
        return x+y+z

print(summm(3,3,3))

