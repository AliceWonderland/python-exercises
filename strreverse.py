#reverse str

def reversestr(strtoreverse):
    newstr = ""
    indexstart = len(strtoreverse)-1
    indexend = -1 #must use -1 to get 0
    step = -1

    #decrement through str step by 1
    for i in range(indexstart, indexend, step):
        newstr += strtoreverse[i]

    return newstr

print(reversestr("hello"))

#reverse str using range()
strtoreverse = "red"
print(strtoreverse[::-1])

#tests
#test with upper/lower case, diff lengths, special chars, lengths

#test for all letters included
