#List Explosion


#Define a procedure, explode_list, that takes as inputs a list and a number, n.
#It should return a list which contains each of the elements of the input list,
#in the original order, but repeated n times.

def explode_list(p,n):
    result = []
    for e in p:
        for i in range(n):
            result.append(e)
    return result


#For example,

print explode_list([1, 2, 3], 2)
#>>> [1, 1, 2, 2, 3, 3]

print explode_list([1, 0, 1], 0)
#>>> []

print explode_list(["super"], 5)
#>>> ["super", "super", "super", "super", "super"]