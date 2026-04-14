#WAP to count the no. of students with A grade in a class, and store them in a list and sort them from A to D
grades= tuple(input("Enter the grades of students from roll 1:").split(','))
print(grades.count('a'))
list1= list(grades)
list2= list1.copy()
list2.sort()
print(list2)
