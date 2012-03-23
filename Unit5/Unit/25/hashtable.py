'''
Created on 23.03.2012

@author: Admin
'''
#Define a procedure, hashtable_get_bucket,
#that takes two inputs - a hashtable, and
#a keyword, and outputs the bucket where the
#keyword could occur.

#hash_string(keyword,nbuckets) => index of bucket

def hashtable_get_bucket(htable,keyword):
   hash = hash_string(keyword, len(htable))
   return htable[hash]


def hash_string(keyword,buckets):
    out = 0
    for s in keyword:
        out = (out + ord(s)) % buckets
    return out

def make_hashtable(nbuckets):
    table = []
    for unused in range(0,nbuckets):
        table.append([])
    return table

