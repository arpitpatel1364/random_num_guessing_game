# 1)remove duplicates from list
my_list = [1, 2, 2, 3, 4, 4, 5]
new_list = []
for item in my_list:
    if item not in new_list:
        new_list.append(item)
print(new_list)

# 2)count odd or even in list
# Input: [1, 2, 3, 4, 5]
# Output: Even = 2, Odd = 3

l1=[1,2,3,4,5]
odd=0
even=0
for i in l1:
    if i %2==0:
        even+=1
    else:
        odd+=1

print(even)
print(odd)

# 3) Convert Celsius to Fahrenheit
# Formula: F = (C * 9/5) + 32
print(" if you want to convert celsius to fahrenheit then enter 'F' and if you want to convert fahrenheit then enter 'C'")
user1=input("enter your ans")
if user1=="F":
    user=float(input("enter tem in celsius"))
    F=(user*9)/5+32
    print(F)
else:
    F=float(input("enter tem in fahrenheit"))
    C= (F - 32) * 5 / 9
    print(C)

# 4) sort list using udf & desanding oder also in it
l2=[]

while len(l2)<=5:
    a = int(input("enter number for list "))
    l2.append(a)
    print(l2)

for i in range(0,len(l2)):
    for j in range(i+1,len(l2)):
        if l2[i]>l2[j]:
            c=l2[i]
            l2[i]=l2[j]
            l2[j]=c

print(l2)

# factorial of n
def fact(n):
    if n ==0 or n == 1:
        return 1
    else :
        return n * fact(n - 1)
n = int(input())
print(fact(n))


# sum of n numbers
def sum(a):
    if a==1:
        return 1
    else :
        return a + sum(a-1)

a=int(input())
print(sum(a))