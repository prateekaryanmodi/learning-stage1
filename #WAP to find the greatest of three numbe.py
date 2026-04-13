#WAP to find the greatest of three numbers entered by the user.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

# Case 1: 'a' is the smallest
if a <= b and a <= c:
    small = a
    if b <= c:
        mid, large = b, c
    else:
        mid, large = c, b

# Case 2: 'b' is the smallest
if b <= a and b <= c:
    small = b
    if a <= c:
        mid, large = a, c
    else:
        mid, large = c, a

# Case 3: 'c' must be the smallest
if c <= a and c <= b:
    small = c
    if a <= b:
        mid, large = a, b
    else:
        mid, large = b, a

print ("Greatest number:", large)
print("Sequence:", large, mid, small)
