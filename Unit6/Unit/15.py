#Define a faster fibonacci procedure that will enable us to computer
#fibonacci(36).

def fibonacci_r(n):
    if n <= 1:
        return n
    else:
        return fibonacci_r(n-1)+fibonacci_r(n-2)

def fibonacci(n):
    a, b = 0, 1
    for i in range(0, n):
        a, b = b, a+b 
    return a    

n = 36

a = fibonacci(n-1)
print a
b = fibonacci(n-2)
print b
print fibonacci(n)
print a+b
#>>> 14930352