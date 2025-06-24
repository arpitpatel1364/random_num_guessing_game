a=int(input("enter the first number : "))
b=int(input("enter the second number : "))

print("before swapping : a =", a, "b =", b)

# swapping the number using third variable

temp = a
a = b
b = temp
print("after swapping : a =", a, "b =", b)

# swapping the number without using third variable
a = a + b
b = a - b
a = a - b
print("after swapping without third variable : a =", a, "b =", b)
