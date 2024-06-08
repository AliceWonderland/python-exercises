#convert csv to list or tuple
csv = "apple, banana, kiwi, orange, watermelon, cherry, blackcurrant, pineapple"
lst = csv.split(',')
tpl = tuple(lst) #convert to lst first, then tpl
print(lst)
print(tpl)

#print file extension
filename = "myfile.txt"
print(filename.split('.')[-1])

#compute result of n if n = n+nn+nnn
#n=5 5+55+555
def nnn(n):
    n = str(n)
    result = 0
    result += int(n)
    result += int(n+n)
    result += int(n+n+n)

    return result

print(nnn(5))


#print user's last name first
fname = input("First Name: ")
lname = input("Last Name: ")
print("Hello,", lname, fname)

