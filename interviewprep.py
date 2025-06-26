students=[]

while len(students)<5:
    name=input("enter student name")
    marks=int(input("enter student marks"))
    students.append({"name": name,"marks":marks})

print("student =", students)

