#MEASURING COST
#For which of these procedures does the worst-case running time scale 
#linearly in the number of elements in the input list p? 
#(You may assume that the elements in the list are all small numbers)

# sum_list
def sum_list(p):
    sum = 0
    for e in p:
        sum = sum + e
    return sum

# has_duplicate_element
def has_duplicate_element(p):
   res = []
   for i in range(0, len(p)):
       for j in range(0, len(p)):
           if i != j and p[i] == p[j]:
               return True
   return False

# mystery
def mystery(p):
   i = 0
   while True:
       if i >= len(p):
           break
       if p[i] % 2:
           i = i + 2
       else:
           i = i + 1
   return i