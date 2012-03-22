'''
Created on 22.03.2012

@author: Admin
'''

import time

def time_execution(code):
    start = time.clock()
    result = eval(code)
    runtime = time.clock()-start
    return result, runtime

def spin_loop(n):
    i = 0
    while i<n:
        i=i+1
        
        
print time_execution('spin_loop(10**9)')
    