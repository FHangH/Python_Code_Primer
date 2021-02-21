#Author:Fang hao 
#Time:2019/6/27 15:38


'''class Employee():
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print('name: ' + self.name)
        print('salary: ' + str(self.salary))


data = Employee('FH', 999999999)
data.display()'''


##############################################################


class Employee():
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print(self.name)
        print(self.salary)


data = Employee('FH', 999999)
data.display()


