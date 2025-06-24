class ResultMaker:
    def get_personal_data(self):
        self.name = input("Enter your name: ")
        self.number = int(input("Enter your number: "))
        self.email = input("Enter your email: ")
        self.roll = int(input("Enter your roll number: "))

    def get_marks(self):
        print("Enter your marks (out of 150):")



        while True:
            self.phy = int(input("Enter your phy : "))
            if self.phy <=150 and self.phy >=0:
                break
            print("Invalid input! Marks should be between 0 and 150.")

        while True:
            self.che = int(input("Enter your che : "))
            if self.che <=150 and self.che >=0:
                break
            print("Invalid input! Marks should be between 0 and 150.")

        while True:
            self.math = int(input("Enter your math : "))
            if self.math <= 150 and self.math >= 0:
                break
            print("Invalid input! Marks should be between 0 and 150.")
    # < --- chat gpt code for better understanding --->
    # while True:
    #     self.phy = int(input("Enter your Physics marks: "))
    #     if 0 <= self.phy <= 150:
    #         break
    #     print("Invalid input! Marks should be between 0 and 150.")
    #
    # while True:
    #     self.che = int(input("Enter your Chemistry marks: "))
    #     if 0 <= self.che <= 150:
    #         break
    #     print("Invalid input! Marks should be between 0 and 150.")
    #
    # while True:
    #     self.math = int(input("Enter your Math marks: "))
    #     if 0 <= self.math <= 150:
    #         break
    #     print("Invalid input! Marks should be between 0 and 150.")


    def putdata(self):
        result = ((self.phy + self.che + self.math) * 100) / 450
        print("\n--- Personal Details ---")
        print("Name   :", self.name)
        print("Number :", self.number)
        print("Email  :", self.email)
        print("Roll   :", self.roll)

        print("\n--- Marks ---")
        print("Math       :", self.math)
        print("Physics    :", self.phy)
        print("Chemistry  :", self.che)

        print("\n--- Result ---")
        print("Percentage :", result, "%")

a=input("are you want to make results ? [y/n]")
while a!="y":
    a = input("are you want to make results ? [y/n]")
    if a == "y":
        student = ResultMaker()
        student.get_personal_data()
        student.get_marks()
        student.putdata()
    elif a == "n":
        print("thank you for using this program")
    else:
        print("enter y or n.")
