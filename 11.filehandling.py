
name=input("enter your name :")

f=open('mytext.txt','a')
f.write(name + " ")
f.close()

print("hello",name,"welcome to my python program")  