# 1)write a programe to find howmany numbers between two numbers
a=int(input("enter a number"))
b=int(input("enter a number"))

if a > b:
    ans=a-b
    print(ans)
elif a < b:
    ans=b-a
    print(ans)
else :
    print(" number are equal")

# 2) write a program to find factorial number
n = int(input("enter a number"))
def factorial(n):
    if n==1 or n==0:
        return 1
    else:
        return n*factorial(n-1)

print(factorial(n))

# 3) wap to how many odd numbers between three numbers
# a=int(input("enter a number"))
# b=int(input("enter a number"))
# c=int(input("enter a number"))
#
# if a>b and a>c :
#     print("a is gretest number")
# elif b>a and b>c:
#     print("b is gretest number")
# else:
#     print("c is gretest number")
#
# if a<c and a<b:
#     print("a is smaller number")
# elif b<a and b<c :
#     print("b is smaller number")
# else:
#     print("c is smaller number")

def findodd(a,b,c):
    num=sorted([a,b,c])
    srt=num[0]
    end=num[2]

    count=0
    for i in range(srt,end):
        if i%2 != 0:
            count+=1

    print(count)

a=int(input("enter a number"))
b=int(input("enter b number"))
c=int(input("enter c number"))
result=findodd(a,b,c)
print(result)

# 4) print all numbers between three numbers

def between3(x,y,z):
    num1=sorted([x,y,z])
    srt1=num1[0]
    end1=num1[2]

    for i in range(srt1,end1+1):
        print(i)

x=int(input("enter a number"))
y=int(input("enter a number"))
z=int(input("enter a number"))
print(between3(x,y,z))

# 5) print table of any number
T=int(input("enter a number"))
list=[]
for i in range(1,11):
    cal=(T*i)

    list.append(cal)


print(list)










