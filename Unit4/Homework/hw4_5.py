#1 Gold Star

#The built-in <string>.split() procedure works
#okay, but fails to find all the words on a page
#because it only uses whitespace to split the
#string. To do better, we should also use punctuation
#marks to split the page into words.

#Define a procedure, split_string, that takes two
#inputs: the string to split and a string containing
#all of the characters considered separators.

#out = split_string("This is a test-of the,string separation-code!", " ,!-")
#print out => ['This', 'is', 'a', 'test', 'of', 'the', 'string', 'separation', 'code']

#out = split_string("After  the flood   ...  all the colors came out."," .")
#print out => ['After', 'the', 'flood', 'all', 'the', 'colors', 'came', 'out']

def split_string(source,splitlist):
    result = [source]
    for splititem in splitlist:
        result2 = []
        for entry in result:
            splittedentry = entry.split(splititem)
            result2 = result2+splittedentry
        result = []
        for entry in result2:
            if entry != '':
                result = result + [entry]    
    return result    

out = split_string("This is a test-of the,string separation-code!", " ,!-")
print out
# => ['This', 'is', 'a', 'test', 'of', 'the', 'string', 'separation', 'code']

out = split_string("After  the flood   ...  all the colors came out."," .")
print out
# => ['After', 'the', 'flood', 'all', 'the', 'colors', 'came', 'out']
