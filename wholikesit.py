# take an array containing the names of people that like an item
# return the display text as shown

"""

[]                                -->  "no one likes this"
["Peter"]                         -->  "Peter likes this"
["Jacob", "Alex"]                 -->  "Jacob and Alex like this"
["Max", "John", "Mark"]           -->  "Max, John and Mark like this"
["Alex", "Jacob", "Mark", "Max"]  -->  "Alex, Jacob and 2 others like this"

"""

def numlikes(ppl):
    msg = ""
    numppl = len(ppl)

    if (numppl==0):
        msg = "no one likes this"
    elif(numppl==1):
        msg = ppl[0] + " likes this"
    elif(numppl==2):
        msg = ppl[0] + " and " + ppl[1] + " like this"
    elif(numppl==3):
        msg = ppl[0] + ", " + ppl[1] + " and " + ppl[2] + " like this"
    elif(numppl>3):
        msg = ppl[0] + ", " + ppl[1] + " and " + str(numppl-2) + " others like this"
    else:
        return None

    return msg

print(numlikes([]))
print(numlikes(["Peter"]))
print(numlikes(["Jacob", "Alex"]))
print(numlikes(["Max", "John", "Mark"]))
print(numlikes(["Alex", "Jacob", "Mark", "Max"]))

def likes(names):
    n = len(names)
    return {
        0: 'no one likes this',
        1: '{} likes this', 
        2: '{} and {} like this', 
        3: '{}, {} and {} like this', 
        4: '{}, {} and {others} others like this'
    }[min(4, n)].format(*names[:3], others=n-2)

def likes(names):
    match names:
        case []: return 'no one likes this'
        case [a]: return f'{a} likes this'
        case [a, b]: return f'{a} and {b} like this'
        case [a, b, c]: return f'{a}, {b} and {c} like this'
        case [a, b, *rest]: return f'{a}, {b} and {len(rest)} others like this'

def likes(names):
    total = len(names)
    return ( 'no one likes this' if total == 0 else
        '%s likes this' % names[0] if total == 1 else
        '%s and %s like this' % (names[0], names[1]) if total == 2 else
        '%s, %s and %s like this' % (names[0], names[1], names[2]) if total == 3 else
        '%s, %s and %s others like this' % (names[0], names[1], total-2) )