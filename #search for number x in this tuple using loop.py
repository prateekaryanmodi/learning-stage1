#search for number x in this tuple using loop
a = (1, 4, 9, 16, 25, 36, 64, 81, 100)
b = int(input(""))
idx = 0
while idx < len(a):
    if (a[idx] == b):
        c=print("number found at index:",idx)
    else:
     print("number not found")   
    idx += 1
print("search completed")