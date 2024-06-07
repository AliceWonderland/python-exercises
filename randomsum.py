#Create a function that takes a list of numbers
#Returns the sum of all the numbers in the list.

import random

#add all nums in list
def randosum (numlist):
    print(numlist)

    sumtotal = 0
    for x in numlist:
        sumtotal += x

    return sumtotal

#create a list of random num
def randonumlist(lenlist, numstart, numend):
    
    numlist = []
    for i in range(lenlist):
        numlist.append( random.randint(numstart, numend) )
    return numlist

print(randosum(randonumlist(10, 1, 50 )))

#create a list of random nums using random.sample()
randomlist = random.sample(range(1, 50), 10)
print( randosum(randomlist) )


#tests
#how do i test if all numbers have been added?
#test with fixed arrays where you know the sum of nums
#use a variety of different numbers, number of digits, decimals to test for exceptions

#test if addition is correct?
#test diff ways of adding