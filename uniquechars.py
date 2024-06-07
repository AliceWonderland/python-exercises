#find unique chars in str return as list/arr

#use set()
def finduniques(inputstr):
    charset = set()
    for letter in inputstr:
        charset.add(letter)

    return charset

print(finduniques("erica"))

#check if str contains all unique chars
def allunique(inputstr):
    charset = set()
    for letter in inputstr:
        if letter in charset:
            return False
        else:
            charset.add(letter)
        
    return True

print(allunique("erica"))
print(allunique("monroe"))
