#waf to find the factorial of no. n 

def fact(a):
    factorial = 1
    for c in range(1,a+1):
        factorial *= c
    print(factorial)
    return factorial
fact(5)
   
