#Spelling Correction

#Double Gold Star

#For this question, your goal is to build a step towards a spelling corrector,
#similarly to the way Google used to respond,

#    "Did you mean: audacity"


#when you searched for "udacity" (but now considers "udacity" a real word!).

#One way to do spelling correction is to measure the edit distance between the
#entered word and other words in the dictionary.  Edit distance is a measure of
#the number of edits required to transform one word into another word.  An edit
#is either: (a) replacing one letter with a different letter, (b) removing a
#letter, or (c) inserting a letter.  The edit distance between two strings s and
#t, is the minimum number of edits needed to transform s into t.

#Define a procedure, edit_distance(s, t), that takes two strings as its inputs,
#and returns a number giving the edit distance between those strings.

#Note: it is okay if your edit_distance procedure is very expensive, and does
#not work on strings longer than the ones shown here.

#The built-in python function min() returns the mininum of all its arguments.

#print min(1,2,3)
#>>> 1

def edit_distance(s,t):
    # algorithm Levenshtein distance
    m, n = len(s)+1, len(t)+1
    d = []
    for i in range(m):
        d.append([i])
        for j in range(1, n):
            d[i].append(0)       
    for j in range(n):
        d[0][j] = j       
    
    for i in range(1, m):
        for j in range(1, n):
            if s[i-1] == t[j-1]:
                d[i][j] = d[i-1][j-1] # no operation required
            else:
                d[i][j] = min(
                                  d[i-1][j] + 1,  # a deletion
                                  d[i][j-1] + 1,  # an insertion
                                  d[i-1][j-1] + 1 # a substitution
                                  )
    return d[m-1][n-1] 
    
def print_matrix(d):
    for i in range(len(d)):
        print d[i]


#For example:

print edit_distance('abc', 'abcde')

# Delete the 'a'
print 'audacity', 'udacity', edit_distance('audacity', 'udacity')
#>>> 1

# Delete the 'a', replace the 'u' with 'U'
print 'audacity', 'Udacity', edit_distance('audacity', 'Udacity')
#>>> 2

# Five replacements
print 'peter', 'sarah', edit_distance('peter', 'sarah')
#>>> 5

# One deletion
print 'pete', 'peter', edit_distance('pete', 'peter')
#>>> 1
