#find longest word in list of words

#get len, if len > than prev save word
#if more than one longest word?

def longestword(wordlist):
    finalword = ""
    finallen = 0

    for word in wordlist:
        print(finallen, len(word), finalword)
        if len(word) > finallen:
            finallen = len(word)
            finalword = word

    return finalword

words = ["", "a", "ab", "abc", "apple", "banana", "cherry", "kiwi", "mango", "watermelon", "blackcurrant", "orange", "lychee"]
print(longestword(words))


#return max num in list using max()
a = (1, 5, 3, 9)
print(max(a))
print(max(words)) #does not work

#tests
#try words upper/lowercase, special chars
#test diff word lens
#make sure all words are tested
#what if all words are equal
#what if no words
#what if only 1 word
#only gives first word with longest len, if subsequent words with same len, does not register



