#PYTHON CHEAT SHEET

### ---------------------------------------- ###
### PRINT console
### ---------------------------------------- ###

print ('hello world')


### ---------------------------------------- ###
### SYNTAX
### ---------------------------------------- ###

    #indents matter in python


### ---------------------------------------- ###
### COMMENTS
### ---------------------------------------- ###

# single line comment

# block comments
"""
    multiline comment
    multiline comment
    multiline comment
"""

'''
    multiline comment
    multiline comment
    multiline comment
'''


### ---------------------------------------- ###
### VARS
### ---------------------------------------- ###

carname = "volvo"
x = 50
x, y, z = "apple", "banana", "orange"
x = y = z = "apple"


### ---------------------------------------- ###
### FUNCTIONS
### ---------------------------------------- ###

def myFunc():
    global x
    x = "fantastic"
    print(x)


### ---------------------------------------- ###
### DATATYPES
### ---------------------------------------- ###

x, y, z, i, j, k, m, n, o, p = 5, "hello", 20.5, [1,2,3,4], (1,2,3,4), {"name" : "John", "age" : 36}, {"apple", "cherry", "banana"}, frozenset({"apple", "banana", "cherry"}), True, None
print(type(x))

"""
    Text Type:	str "hello"
    Numeric Types:	int (5), float (20.5), complex
    Sequence Types:	list ([1,2,3,4]), tuple ( (1,2,3,4) ), range
    Mapping Type:	dict ({"name" : "John", "age" : 36})
    Set Types:	set ({"apple", "cherry", "banana"}), frozenset ( frozenset({"apple", "banana", "cherry"}) )
    Boolean Type:	bool (True, False)
    Binary Types:	bytes, bytearray, memoryview
    None Type:	NoneType (None)
"""

#datatype constructors
x = str("hello") 
print(x, type(x))
x = 200
print(isinstance(x, int))
print(isinstance(x, str))

x = int(5)
x = float(20.5)
x = complex(1j)
x = range(6)
x = dict(name="John", age=36)
x = bool(5)
x = bytes(5)
x = bytearray(5)
x = memoryview(bytes(5))


### ---------------------------------------- ###
### STRINGS
### ---------------------------------------- ###

#quote inside quotes
print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')
#multine str
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit
ut labore et dolore magna aliqua."""

a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit
ut labore et dolore magna aliqua.'''

#strs are arrays
a = "Hello, World!"
print(a[1])

#loop thru strs
for x in "banana":
  print(x)

#str len
a = "Hello, World!"
print(len(a))

#check str
txt = "The best things in life are free!"
print("free" in txt)

txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")
print("expensive" not in txt)

#slice str from start w/ range
b = "Hello, World!"
print(b[2:5])

#slice from start
print(b[:5])

#slice from end to start
print("ererer", b[:-1])

#slice to end
print(b[2:])

#slice from end w/range
print(b[-5:-2])

#reverse str
print(b[::-1])

#modify str
a = "Hello, World!"
print(a.upper())
print(a.lower())

#strip whitespace only from beg/end
a = "     Hello, World!       "
print(a.strip()) # returns "Hello, World!"

#str replace
a = "Hello, World!"
print(a.replace("H", "J")) #replaces H with J

#str split into array using delim
print(a.split(","))

#concat strs
a = "Hello"
b = "World"
c = a + " " + b
print(c)

#fstrings contact strs + nums
age = 36
txt = f"My name is John, I am {age}"
print(txt)

#concat strs with placeholders or modifiers
price = 59
txt = f"The price is {price} dollars"
print(txt)

txt = f"The price is {20 * 59} dollars"
print(txt)

price = 59
txt = f"The price is {price:.2f} dollars" #display price with 2decimals
print(txt)

#escape chars in str
txt = "We are the so-called \"Vikings\" from the north."


### ---------------------------------------- ###
### ARITHMETIC/OPERATORS
### ---------------------------------------- ###

x = 1
y = 5
sum = x+y
print(sum)

#operators
"""
=	x = 5	x = 5	
+=	x += 3	x = x + 3	
-=	x -= 3	x = x - 3	
*=	x *= 3	x = x * 3	
/=	x /= 3	x = x / 3	
%=	x %= 3	x = x % 3	
//=	x //= 3	x = x // 3	
**=	x **= 3	x = x ** 3	
&=	x &= 3	x = x & 3	
|=	x |= 3	x = x | 3	
^=	x ^= 3	x = x ^ 3	
>>=	x >>= 3	x = x >> 3	
<<=	x <<= 3	x = x << 3	
:=	print(x := 3)	x = 3 print(x)
"""


### ---------------------------------------- ###
### BOOLEAN True/False
### ---------------------------------------- ###

#most values are True except 0, None, and empty values of any datatype


### ---------------------------------------- ###
### ARRAYS
### ---------------------------------------- ###

mylist = ["apple", "banana", "cherry"]
mylist = list(("apple", "banana", "cherry")) # note the double round-brackets

print(mylist[1]) #index from start
print(mylist[-1]) #index from end
print(mylist[2:5]) #range
print(mylist[-4:-1]) #range from end
print(mylist[2:]) #from 2 til end
print(mylist[:2]) #from start til 4

if "apple" in mylist:
  print("Yes, 'apple' is in the fruits list")
if "apple" not in mylist:
  print("No, 'apple' is not in the fruits list")


thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1] = "blackcurrant" #change banana to currant
print(thislist)
thislist[1:3] = ["lychee", "watermelon"] #change banana cherry to lychee watermelon
print(thislist)

#INSERT/REPLACE
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"] #replace currant, watermelon where banana
print(thislist)

#REMOVE/REPLACE
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"] #replace banana cherry to watermelon
print(thislist)

#INSERT/NO REPLACE
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon") #insert melon before cherry
print(thislist)

#APPEND
thislist.append("orange")

#CONCAT LISTS 
# extend() *can concat any collection datatype
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical) #adds tropical to end
print(thislist)

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
for x in list2:
  list1.append(x)
print(list1)

#REMOVE *only removes first occur
thislist = ["apple", "banana", "cherry", "banana", "kiwi", "apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)

#REMOVE from position
thislist.pop(1)
print(thislist)

del thislist[0] #does the same thing as pop()
print(thislist)

thislist.pop() #unspecified removes from end
print(thislist)

#del entire arr
thislist = ["apple", "banana", "cherry"]
del thislist

#empty entire arr
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)


"""
List ordered, changeable. Allows duplicates.
Tuple ordered, unchangeable. Allows duplicates.
Set unordered, unchangeable, unindexed. No duplicates. Items removable.
Dictionary ordered, changeable. No duplicates. Prev vers py unordered.
"""


### ---------------------------------------- ###
### LOOPS
### ---------------------------------------- ###

#loop thru items
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

#loop using index
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])

#while
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

#COMPREHENSION shorthand for loop
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []
for x in fruits:
  if "a" in x:
    newlist.append(x)
print(newlist)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
#syntax newlist = [expression for item in iterable if condition == True]
newlist = [x for x in fruits if "a" in x] #returns new list with all fruits w/ a
print(newlist)

#filter
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if x != "apple"] #returns new list with all fruits items except apple
print(newlist)

#duplicate list
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits] #returns new list with all items in fruits
print(newlist)

thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

#fill new list with range
newlist = [x for x in range(10)] #returns new list with [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(newlist)

newlist = [x for x in range(10) if x < 5] #returns new list w [0, 1, 2, 3, 4]
print(newlist)

#modify item values in list
#uppercase all items
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x.upper() for x in fruits] 
print(newlist)

#replaces all items with "hello"
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = ['hello' for x in fruits] 
print(newlist)

#replace banana w orange
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)

#sort asc
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort() #returns ['banana', 'kiwi', 'mango', 'orange', 'pineapple']
print(thislist)

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort() #returns ['Kiwi', 'Orange', 'banana', 'cherry'] *Uppercase sort before Lowercase
print(thislist)

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower) #case insensitive sort asc returns ['banana', 'cherry', 'Kiwi', 'Orange']
print(thislist)

thislist = [100, 50, 65, 82, 23]
thislist.sort() #returns [23, 50, 65, 82, 100]
print(thislist)

#sort desc
thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True) #returns [100, 82, 65, 50, 23]
print(thislist)

#reverse order of list
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse() #returns ['cherry', 'Kiwi', 'Orange', 'banana']
print(thislist)

#custom sort
#sort based on how close num is to 50
def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc) #returns [50, 65, 23, 82, 100]
print(thislist)


### ---------------------------------------- ###
### TUPLE
### ---------------------------------------- ###

#ordered, immutable, duplicates

thistuple = ("apple",) #must include comma at end if only 1 item to become a tuple
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))

#tuple constructor
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)

thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")

#convert tuple to list to change items
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

#concat 2 tuples
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y
print(thistuple)

#del entire tuple
thistuple = ("apple", "banana", "cherry")
del thistuple
#print(thistuple) #this will raise an error because the tuple no longer exists

#unpacking tuples - assigning tuple items a variable label
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green, yellow, red)

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits #use asterisk if num vars doesnt match length
print(green, yellow, red) # returns apple banana ['cherry', 'strawberry', 'raspberry']

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(green, *tropic, red) = fruits
print(green, tropic, red) #returns apple ['mango', 'papaya', 'pineapple'] cherry

#concat/join tuple
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)

fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2 #returns ('apple', 'banana', 'cherry', 'apple', 'banana', 'cherry')
print(mytuple)

#count()
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x = thistuple.count(5) #returns num times 5 appears in tuple
print(x)

#index()
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x = thistuple.index(8) #returns index of 8
print(x)

#tuples have the same references as arrays/lists
#loooping tuples is same as list


### ---------------------------------------- ###
### SETS
### ---------------------------------------- ###

#unordered, immutable but add/remove allowed, no duplicates
#True/1, False/0 are considered same values

thisset = {"apple", "banana", "cherry"}
print(thisset)

thisset = {"apple", "apple", "banana", "cherry", False, 0, True, 1, 2}
print(thisset) #returns {False, True, 2, 'banana', 'cherry', 'apple'}
print(len(thisset)) #length
print(type(thisset))

thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)

thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)

thisset = {"apple", "banana", "cherry"}
print("banana" in thisset) #returns True

thisset = {"apple", "banana", "cherry"}
print("banana" not in thisset) #return False

thisset = {"apple", "banana", "cherry"}
thisset.add("orange") #returns {'apple', 'orange', 'banana', 'cherry'}
print(thisset)

#concat sets
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset) #returns {'apple', 'mango', 'cherry', 'pineapple', 'banana', 'papaya'}

#concat any combination of collection types
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist) #returns {'banana', 'kiwi', 'apple', 'orange', 'cherry'}
print(thisset) 

#remove item
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana") #returns {'apple', 'cherry'}
print(thisset) 
#throws error if banana does not exist

thisset = {"apple", "banana", "cherry"}
thisset.discard("banana") #returns {'apple', 'cherry'}
print(thisset) 
#does NOT throw error if banana does not exist

thisset = {"apple", "banana", "cherry"}
x = thisset.pop() #removes random item from set returns random item value
print(x, thisset)

#empty set
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset) #returns set()

#del set
thisset = {"apple", "banana", "cherry"}
del thisset
#print(thisset) #returns err

#loop sets
thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)

#join sets
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2) #returns {'c', 2, 1, 'a', 3, 'b'}
print(set3)

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1 | set2 #can use | operator instead of union constructor returns same as above
print(set3)

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}
myset = set1.union(set2, set3, set4)
print(myset)

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}
myset = set1 | set2 | set3 |set4
print(myset)

#join set + other datatypes
x = {"a", "b", "c"}
y = (1, 2, 3)
z = x.union(y)
print(z)
#cannot use | to join set/other datatypes

#update
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set1.update(set2) #insert set2 into set1
print(set1)
#does not return a value

#intersection returns items in both
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.intersection(set2) #returns set of values that occur in both {'apple'}
print(set3)
#does not modify orig sets

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1 & set2 #can use amp operator instead of constructor
print(set3)

#intersection_update
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.intersection_update(set2) #keep only duplicates, modify set1 with new results
print(set1)

#difference returns  items not in both
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.difference(set2)
print(set3)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1 - set2 #use - operator instead of difference() with sets only not mixed dtypes
print(set3)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.difference_update(set2) #update with difference only
print(set1)

#symmetric difference
#symmetric difference update

#issuperset()
#issubset()


### ---------------------------------------- ###
### DICTS ordered mutable unique
### ---------------------------------------- ###

thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
print(thisdict["brand"]) #returns "Ford"
print(len(thisdict))

thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)

x = thisdict.keys()
print(x)

x = thisdict.values()
print(x)

x = thisdict.items() #key/value pairs
print(x)

thisdict["age"] = 20

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")

#another way to add/update values
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020})

#remove specified item
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)

#remove last item
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict)

#del key/value pair
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
print(thisdict)

#delete dict
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict
#print(thisdict) #this will cause an error because "thisdict" no longer exists.

#empty dict
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
print(thisdict)

#loop dict
for x in thisdict:
  print(x)

for x in thisdict:
  print(thisdict[x])

for x in thisdict.values():
  print(x)

for x in thisdict.keys():
  print(x)

for x, y in thisdict.items():
  print(x, y)

#copy dicts
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = dict(thisdict)
print(mydict)

#nested dicts
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}
myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}

print(myfamily["child2"]["name"])

#loop nested
for x, obj in myfamily.items():
  print(x)

  for y in obj:
    print(y + ':', obj[y])

#if/else
"""
  Equals: a == b
  Not Equals: a != b
  Less than: a < b
  Less than or equal to: a <= b
  Greater than: a > b
  Greater than or equal to: a >= b
"""

a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

#shorthand if
if a > b: print("a is greater than b")

#shorthand if/else
a = 2
b = 330
print("A") if a > b else print("B")
#ternary

a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")

a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")

a = 33
b = 200
if not a > b:
  print("a is NOT greater than b")

x = 41
if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")

#pass
a = 33
b = 200
if b > a:
  pass

#while
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

i = 0
while i < 6:
  i += 1
  if i == 3:
    continue #skip current iter and continue w loop
  print(i)

i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")

#range
for x in range(2, 30, 3):
  print(x)
#print 2-29 in increments of 3

for x in range(6):
  print(x)
else:
  print("Finally finished!")

for x in range(6):
  if x == 3: break #if break will not hit else
  print(x)
else:
  print("Finally finished!")

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
for x in adj:
  for y in fruits:
    print(x, y)

#this will give err
for x in [0, 1, 2]:
  pass


### ---------------------------------------- ###
### FUNCTIONS
### ---------------------------------------- ###

def my_function():
  print("Hello from a function")
my_function()

def my_function(fname, lname):
  print(fname + " " + lname)
my_function("jane", "doe")

def my_function(*kids):
  print("The youngest child is " + kids[2])
my_function("Emil", "Tobias", "Linus")

def my_function(child3, child2, child1):
  print("The youngest child is " + child3)
my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")
#order of args doesnt matter if using key/value args

def my_function(**kid):
  print("His last name is " + kid["lname"])
my_function(fname = "Tobias", lname = "Refsnes")

def my_function(country = "Norway"):
  print("I am from " + country)
my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

def my_function(food):
  for x in food:
    print(x)
fruits = ["apple", "banana", "cherry"]
my_function(fruits)

def my_function(x):
  return 5 * x
print(my_function(3))
print(my_function(5))
print(my_function(9))

def myfunction():
  pass

#recursion calls itself
def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result
print("\n\nRecursion Example Results")
tri_recursion(6)

#lambda small anon function
x = lambda a : a + 10
print(x(5))

