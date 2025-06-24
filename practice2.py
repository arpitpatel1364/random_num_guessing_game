# 1)reverse string
a=str(input("enter your name"))
l1=[]
l1.extend(a)
# print(l1)
# print(l1[:3])
l1.reverse()
# print(l1)
fnstr=''.join(l1)
print(fnstr)

# 2) check string is palindrom string or not
a=str(input("enter your name"))
l1=[]
l1.extend(a)
l1.reverse()
fnstr=''.join(l1)
print(fnstr)

if a==fnstr:
    print("your string is palindrom string")
else:
    print("your string is not palindrom string")

# 3) count vowels in string

name=str(input("enter your name"))
li=[]
lv=["a","e","i","o","u","A","E","I","O","U"]

li.extend(name)
count=0
for i in li:
    if i in lv:
        count+=1
        print(i)
    else:
        continue
print(count)

# 4) sum of given digit

n1=int(input("enter your number"))
l2=[]
l2.extend(str(n1))
sum=0
for i in l2:
    sum+=(int(i))

print(sum)

# 5) reverse given number

n2=int(input("enter your number"))
l3=[]
l3.extend(str(n2))
l3.reverse()
fnstr1=''.join(l3)
print(fnstr1)

# 6) find min or maximun in given numbers
user=str(input("you want to enter number ? [Y/N]"))
num = []
while user=="Y":
    if user=="Y":
        roll = int(input("enter your stu roll"))
        if roll in num:
            print("number is already exists")
        else:
            num.append(roll)
        user = str(input("you want to enter number ? [Y/N]"))
    else:
        print(num)
        user = str(input("you want to enter number ? [Y/N]"))
else:
    print(num)
    print("Minimum:", min(num))
    print("Maximum:", max(num))

# 7)convert list into desanding order
#  can do it with sort and reverse it but learn without sort
# and learn how can we sort list with user define function

# arpit=[3,8,9,6,4,1]
# for i in range (0,len(arpit)):
#     for j in range (i+1,len(arpit)):




