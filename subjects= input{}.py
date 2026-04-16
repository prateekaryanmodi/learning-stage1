student=  {}
sub1= input("enter subject 1:")
sub2= input("enter subject 2:")
sub3= input("enter subject 3:")
marks1= int(input("enter marks of subject 1:"))
marks2= int(input("enter marks of subject 2:"))
marks3= int(input("enter marks of subject 3:"))
student.update({sub1: marks1})
student.update({sub2: marks2})
student.update({sub3: marks3})    

print(student)