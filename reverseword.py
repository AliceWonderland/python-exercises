# reverse all words in a str keeping spaces
# "This is an example!" ==> "sihT si na !elpmaxe"
# "double  spaces"      ==> "elbuod  secaps"

def revstr(str):
    newstr = ""

    for wrds in str.split(" "):
        newstr += wrds[::-1] + " "

    return newstr[:-1]

print(revstr("This is an example!"))
print(revstr("double  spaces"))


def reverse_words(str):
    return ' '.join(s[::-1] for s in str.split(' '))

print(reverse_words("This is an example!"))
print(reverse_words("double  spaces"))


# import re
# def reverse_words2(str):
#   return re.sub(r'\S+', lambda w: w.group(0)[::-1], str)

# print(reverse_words2("This is an example!"))
# print(reverse_words2("double  spaces"))


def reverse_words(str):
  return " ".join(map(lambda word: word[::-1], str.split(' ')))

print(reverse_words("This is an example!"))
print(reverse_words("double  spaces"))




