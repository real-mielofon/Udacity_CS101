'''
Created on 23.03.2012

@author: Admin
'''
#Creating an Empty Hash Table
#Define a procedure, make_hashtable,
#that takes as input a number, nbuckets,
#and outputs an empty hash table with
#nbuckets empty buckets.

def make_hashtable(nbuckets):
    return [[]]*nbuckets

print make_hashtable(15)