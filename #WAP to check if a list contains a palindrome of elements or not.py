#WAP to check if a list contains a palindrome of elements or not.
list1= input([]).split(',')
list2= list1.copy()
list2.reverse()
if list1==list2:
    print("The list contains a palindrome of elements.")
else:    print("The list does not contain a palindrome of elements.")
print(list2)