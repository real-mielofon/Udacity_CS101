#Define a procedure, greatest,
#that takes as input a list
#of positive numbers, and
#returns the greatest number
#in that list. If the input
#list is empty, the output
#should be 0.

#greatest([4,23,1]) => 23
#greatest([]) => 0

def greatest(list_num):
    result = 0
    for n in list_num:
        if n > result:
            result = n
    return result
        
    
print greatest([4,23,1])
print greatest([4,23,1,2,3,4,44,1,2,3,55])
# => 23
print greatest([])
# => 0