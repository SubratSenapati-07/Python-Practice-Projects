#1
class Employee:
    name = "Subrat"
    regn_no = 2401326318
    branch = "CSE"

sr = Employee()
sr.name = "Satx"
print(sr.name)


#2

class Student:
    name = "Subrat"
    reg_no= 2401326318
    branch = "CSE"

    def info(self):
        print(f"{self.name} having registration number {self.reg_no} with {self.branch} branch.")

    @staticmethod
    def greeting():
        print("Good Day!")

new = Student()
new.info()
new.greeting()