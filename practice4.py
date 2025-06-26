def student_data():
    names = []
    rollnos = []

    print("Enter 10 unique students (both name and roll number must be unique):")

    while len(names) < 10:
        name = input(f"\nEnter student name ({len(names) + 1}/10): ")


        if name in names:
            print(" Name already exists! Try entering a different name and roll number.")
            continue

        while True:
            try:
                roll = int(input("Enter roll number: "))
            except ValueError:
                print(" Invalid roll number! Please enter a valid number.")
                continue

            if roll in rollnos:
                print(" Roll number already exists! Enter a different roll number for this name.")
            else:
                break

        names.append(name)
        rollnos.append(roll)
        print(" Name and Roll number saved.")

    print("\n Data Entry Complete!")
    print("Names List:", names)
    print("Roll Numbers List:", rollnos)


student_data()



# 3) write a program to find factorial number
class Aaa:
    def __init__(self):
        self.n = int(input("Enter a number: "))

    def factorial(self, n):
        if n == 0 or n == 1:
            return 1
        else:
            return n * self.factorial(n - 1)

obj = Aaa()
result = obj.factorial(obj.n)
print("Factorial is:", result)

# 4) reverse given number

def reverse_number(n):
    l = list(str(n))
    l.reverse()
    reversed_str = ''.join(l)
    return int(reversed_str)

num = int(input("Enter your number: "))
reversed_num = reverse_number(num)
print("Reversed number is:", reversed_num)

# 5) wap to check howmany numbers are odd numbers between given two numbers using class
class OddC:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def count_odds(self):
        count = 0
        for num in range(self.start + 1, self.end):  # Exclude boundaries
            if num % 2 != 0:
                count += 1
        return count

# Example usage:
start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

counter = OddC(start, end)
result = counter.count_odds()
print(f"Total odd numbers between {start} and {end}  = {result}")
