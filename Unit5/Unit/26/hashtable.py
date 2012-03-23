#Define a procedure,

#hashtable_add(htable,key,value)

#that adds the key to the hashtable
#(in the correct bucket), with the
#correct value.

def hashtable_add(htable,key,value):
    bucket = hashtable_get_bucket(htable,key)
    for e in bucket:
        if e[0] == key:
            e[1].append(value)
            return
    bucket.append([key,[value]])        

def hashtable_get_bucket(htable,keyword):
    return htable[hash_string(keyword,len(htable))]

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

import random

nbuckets = 12
htable = make_hashtable(nbuckets)
for i in range(0, 100):
    key = ""
    for j in range(0,2):
        key += chr(random.randrange(ord('a'), ord('z'), 1))
    hashtable_add(htable, key, 'v1_'+chr(random.randrange(ord('a'), ord('z'), 1)))


for b in htable:
    print b