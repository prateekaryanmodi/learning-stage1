#search for a number in the following tuple usinf for loop
tup = (1,4,9,16,25,36,49,64,81,100)
b= int(input("enter a number"))
for a in tup:
    if (a==b):
        print ("number found")
        break
    else :
        print ("number not found")