print("enter any number i will tell you you are aligible or not for voting")
a=int(input("enter the first number"))
b=int(input("emter the second number"))

if a>b:
    print("a is greater then b")
elif b>a:
    print("b is greater then a")
elif a==b:
    print("those numbers are equal")
else:
    print("enter valid numbers")