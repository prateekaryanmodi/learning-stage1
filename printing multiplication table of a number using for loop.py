#print multiplication table of a number using loops
a= int(input("enter a number :"))
for i in range (1,11,1) :
    b = a*i
    print(a,"X",i , "=",b)