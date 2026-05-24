# შექმენით თანამშრომლების მართვის სისტემა:
# შექმენით მთავარი კლასი Employee, რომელსაც ექნება შემდეგი ატრიბუტები:
# name
# salary (ხელფასი არ უნდა იყოს უარყოფითი)

# ამ კლასში შექმენით შემდეგი მეთოდები:

# show_info — დაბეჭდოს თანამშრომლის სახელი და ხელფასი
# work — დაბეჭდოს: Employee is working
# raise_salary - ეს მეთოდი უნდა ზრდიდეს თანამშრომლის ხელფასს გადაცემული რაოდენობით.

# შექმენით შვილობილი კლასი Developer, რომელიც მემკვიდრეობით მიიღებს Employee კლასს.

# ამ კლასს დამატებით უნდა ჰქონდეს:
# programming_language ატრიბუტი

# ასევე შექმენით:
# code() მეთოდი, რომელიც დაბეჭდავს: Writing code...

# Developer კლასში გადაფარეთ (override) work() მეთოდი ისე, რომ დაბეჭდოს:
# Developer is coding

# შექმენით შვილობილი კლასი Designer, რომელიც მემკვიდრეობით მიიღებს Employee კლასს.

# ამ კლასს დამატებით უნდა ჰქონდეს:

# design_tool ატრიბუტი

# ასევე შექმენით:

# create_design() მეთოდი, რომელიც დაბეჭდავს: Creating design...

# Designer კლასში გადაფარეთ (override) work() მეთოდი ისე, რომ დაბეჭდოს:
# Designer is designing

# პროგრამაში შექმენით:
# მინიმუმ ერთი Developer ობიექტი
# მინიმუმ ერთი Designer ობიექტი
# თითოეული ობიექტისთვის გამოიძახეთ:
# show_info()
# work()
# შესაბამისი დამატებითი მეთოდი




class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        if value < 0:
            raise ValueError("ხელფასი უარყოფითი ვერ იქნება")
        self._salary = value

    def show_info(self):
        print(f"სახელი: {self.name}, ხელფასი: {self.salary}")

    def work(self):
        print("Employee is working")

    def raise_salary(self, amount):
        self.salary += amount


class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        super().__init__(name, salary)
        self.programming_language = programming_language

    def code(self):
        print("Writing code...")

    def work(self):
        print("Developer is coding")


class Designer(Employee):
    def __init__(self, name, salary, design_tool):
        super().__init__(name, salary)
        self.design_tool = design_tool

    def create_design(self):
        print("Creating design...")

    def work(self):
        print("Designer is designing")


dev = Developer("Giorgi", 5000, "Python")
designer = Designer("Nino", 4000, "Figma")

dev.show_info()
dev.work()
dev.code()

designer.show_info()
designer.work()
designer.create_design()

გამოსავალი:

სახელი: Giorgi, ხელფასი: 5000
Developer is coding
Writing code...

სახელი: Nino, ხელფასი: 4000
Designer is designing
Creating design.

