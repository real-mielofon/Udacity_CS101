def qsort(list, compare):
    if len(list) <= 1:
        return list
    list_left = []
    list_right = []
    node_pivot = list[0]
    for node in list[1:]:
        if compare(node, node_pivot) > 0:
            list_right.append(node)
        else:
            list_left.append(node)
    #sort parts
    list_left = qsort(list_left, compare)+[node_pivot]
    list_right = qsort(list_right, compare)
    
    #merge
    result = []
    i,j = 0,0
    for k in range(len(list)):
        if (i >= len(list_left)) or (((j < len(list_right))) and compare(list_left[i], list_right[j]) > 0):
            result.append(list_right[j])
            j = j + 1
        else:   
            result.append(list_left[i])
            i = i + 1
    return result

def compare_int(n1, n2):
    if n1 > n2:
        return 1
    if n1 < n2:
        return -1
    else:
        return 0

list = [3,2,1]
print qsort(list, compare_int)

list = [1,2,3]
print qsort(list, compare_int)

slist = []
for i in range(100):
  slist.append(i)

import random
  
list = slist  
for i in range(100):
  r1, r2 = random.randint(1, len(slist)-1), random.randint(1, len(slist)-1)  
  list[r1], list[r2] = list[r2], list[r1]

print slist
print list
print qsort(list, compare_int)
