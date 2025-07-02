user =input("enter here ")
li=[]
l2=[]

for i in user:
    c=str(user.count(i))
    final=c+i
    li.append(final)

#fatch from li and print in l2
for x in li:
    if x not in l2:
        l2.append(x)

print(l2)

