# 1) 10 DATA ENTRY
def student_data():
    names = []
    rollnos = []

    print("Enter data for 10 students (unique names and roll numbers only):")

    while len(rollnos) < 10:
        name = input(f"Enter name for student {len(rollnos)+1}: ").strip()
        roll = int(input("Enter roll number: "))

        if name in names:
            print(" This name already exists! Enter a unique name.")
        elif roll in rollnos:
            print(" This roll number already exists! Enter a unique roll number.")
        else:
            names.append(name)
            rollnos.append(roll)

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
