#waf to print n to 1 backwards using recursions
n= int(input("enter a number:"))
def show(n):
    if(n==0):
        return
    print(n)
    show(n-1)
show(n)