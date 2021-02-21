#Author:Fang hao
#Time:2019/5/2 18:45


'''class Dog():
  #Dog首字母大写在python中默认为类

    def __init__(self, name, age):  #self形参必不可少,且必须位于最前面,当python调用init时，自动传入实参self
        self.name = name  #获取存储在name中的值，并将其存储在变量name中，变量再被关联到当前创建的实例中
        self.age = age

    def sit(self):  #不需要额外的参数信息，所以只需要self即可
        print(self.name.title() + ' is now siting.')

    def roll_over(self):
        print(self.name.title() + ' is rolled over!')


my_dog = Dog('cyl', 6)  #my_dog为变量名，在Dog类中建立形参cyl, 6
your_dog = Dog('fh', 8)

print('My dog name is ' + my_dog.name.title() + ' .')
print('My dog is ' + str(my_dog.age) + ' years old.\n')

my_dog.sit()  #通过‘.’的方法直接调用已经创建好的方法
my_dog.roll_over()

print('#'*36)
print('Your dog name is ' + your_dog.name.title() + ' .')
print('Your dog is ' + str(your_dog.age) + ' years old .\n')

your_dog.sit()
your_dog.roll_over()'''


########################################################################


'''class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(self.restaurant_name)
        print('Main: ' + self.cuisine_type.title())

    def open_restaurant(self):
        print(self.restaurant_name + ' is running now!')


FH = Restaurant("FH's ", 'chinese cooking')
print(FH.restaurant_name)
print(FH.cuisine_type.title())
print('#'*36)
FH.describe_restaurant()
FH.open_restaurant()'''


##########################################################################


'''class User():

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def describe_user(self):
        print('Information:')
        print('\t' + self.first_name.title() + ' ' + self.last_name.title())
        print('\tAge: ' + str(self.age))

    def greet_user(self):
        print('Hello ' + self.first_name.title() + '!')
        print('\tNice to meet you!')


FH = User('fang', 'hao', 20)
CYL = User('cheng', 'ya li', 18)


FH.describe_user()
FH.greet_user()
print('#'*36)
CYL.describe_user()
CYL.greet_user()'''


############################################################################


'''class Car():

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 2019

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()  #类无法使用title()，所以和形参使用,当调用类时，自动返回使用了title()的形参值

    def read_odometer(self):
        print('This car has ' + str(self.odometer_reading) + ' miles on it.')


my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()'''


#另外一种写法


'''class Car():

    def __init__(self, make, model, year, odometer):
        self.make = make
        self.model = model
        self.year = year
        self.odometer = odometer

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()  #类无法使用title()，所以和形参使用,当调用类时，自动返回使用了title()的形参值

    def read_odometer(self):
        print('This car has ' + str(self.odometer) + ' miles on it.')


my_new_car = Car('audi', 'a4', 2016, 2019)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()'''


#另一种


'''class Car():

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()  #类无法使用title()，所以和形参使用,当调用类时，自动返回使用了title()的形参值

    def read_odometer(self):
        print('This car has ' + str(self.odometer_reading) + ' miles on it.')


my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
my_new_car.odometer_reading = 2019
my_new_car.read_odometer()'''


#另一种


'''class Car():

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 2019

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()  #类无法使用title()，所以和形参使用,当调用类时，自动返回使用了title()的形参值

    def read_odometer(self):
        print('This car has ' + str(self.odometer_reading) + ' miles on it.')


my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()'''


####################################################################################


'''class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(self.restaurant_name)
        print('Main: ' + self.cuisine_type.title())

    def open_restaurant(self):
        print(self.restaurant_name + ' is running now!')

    def set_number_served(self, number):
        self.number_served = number

    def describe_number(self):
        print('Served customer number ' + str(self.number_served) + ' .')

    def increment_number_served(self):
        self.number_served += 1


FH = Restaurant("FH's ", 'chinese cooking')
FH.describe_number()

FH.number_served = 5  #直接修改值并打印
FH.describe_number()

FH.set_number_served(8)  #通过修改这个名的值，传递到number_served中，并打印
FH.describe_number()

while FH.number_served < 108:  #通过循环使值递增，并设定一个值，是的打印出这个最大值
    FH.increment_number_served()
FH.describe_number()'''


##################################################################################


'''class User():

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.login_attempts = 0

    def describe_user(self):
        print('Information:')
        print('\t' + self.first_name.title() + ' ' + self.last_name.title())
        print('\tAge: ' + str(self.age))

    def greet_user(self):
        print('Hello ' + self.first_name.title() + '!')
        print('\tNice to meet you!')

    def increment_login_attempts(self):  #使login_attempts的值递增
        self.login_attempts += 1

    def reset_login_attempts(self):  #将Login_attempts的值修改为0，并传递给原值
        self.login_attempts = 0


FH = User('fang', 'hao', 20)

for i in range(10):
    FH.increment_login_attempts()
    print('Login attempts: ' + str(FH.login_attempts))

FH.reset_login_attempts()
print('Login attempts: ' + str(FH.login_attempts))'''


###########################################################################


'''class Car():  #父类

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()  #类无法使用title()，所以和形参使用,当调用类时，自动返回使用了title()的形参值

    def read_odometer(self):
        print('This car has ' + str(self.odometer_reading) + ' miles on it.')

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print('You can not roll back an odometer!')

    def increment_odometer(self, miles):
        self.odometer_reading += miles


class ElectricCar(Car):  #子类，并在其中指定父类Car

    def __init__(self, make, model, year):  #初始化父类属性
        super().__init__(make, model, year)  #super可以将子类和父类关联，时子类可使用__init__方法
        self.battery_size = 70  #在子类中添加新属性

    def describe_battery(self):  #添加一个新的方法
        print('This car has a ' + str(self.battery_size) + '-KWH battery.')


my_car = ElectricCar('tesla', 'model s', 2019)
print(my_car.get_descriptive_name())
my_car.describe_battery()'''


################################################################################################


'''class Square:
    def __init__(self, length):
        self.length = length

    def zc(self):
        zc = str(self.length*4)
        return zc

    def mj(self):
        mj = str(self.length**2)
        return mj


class Rec(Square):
    def __init__(self, width, height):
        super().__init__(self)
        self.width = width
        self.height = height

    def zc(self):
        zc = str((self.width + self.height)*2)
        return zc

    def mj(self):
        mj = str(self.width * self.height)
        return mj


squ = Square(100)
print('正方形的周长：' + squ.zc())
print('正方形的面积：' + squ.mj())
print('#'*36)
squ = Rec(100, 200)
print('长方形的周长：' + squ.zc())
print('长方形的面积：' + squ.mj())'''



#############################################################################


'''import random


class Twocolor:
    def __init__(self):
        self.balllist = []

    def prize(self, prizenumberlist):
        tempprizelist = prizenumberlist[:-1]
        tempyourlist = self.balllist[:-1]
        redprizelist = []
        blueprizelist = []
        redcount = 0
        bluecount = 0


        for e in tempyourlist:
            if e in tempprizelist:
                redprizelist.append(e)
                redcount += 1

        if prizenumberlist[-1] == self.balllist[-1]:
            bluecount += 1
            blueprizelist.append(prizenumberlist[-1])


        print('红色中奖号码:', redprizelist)
        print('蓝色中奖号码:', blueprizelist)
        print('红球:', redcount)
        print('蓝球:', bluecount)

        if redcount == 0 and bluecount == 1:
            print('中了六等奖 5元')
        elif redcount == 1 and bluecount == 1:
            print('中了六等奖 5元')
        elif redcount == 2 and bluecount == 1:
            print('中了六等奖 5元')
        elif redcount == 3 and bluecount == 1:
            print('中了五等奖 10元')
        elif redcount == 4 and bluecount == 0:
            print('中了五等奖 10元')
        elif redcount == 5 and bluecount == 0:
            print('中了四等奖 200元')
        elif redcount == 4 and bluecount == 1:
            print('中了四等奖 200元')
        elif redcount == 5 and bluecount == 1:
            print('中了三等奖 3000')
        elif redcount == 6 and bluecount == 0:
            print('中了二等奖 10000')
        elif redcount == 6 and bluecount == 1:
            print('中了一等奖  3000000000')
        else:
            print('别灰心！ 再买一次！！！')

    def generate(self):
        while len(self.balllist) < 6:
            red_ball = random.randint(1, 34)
            if red_ball not in self.balllist:
                self.balllist.append(red_ball)
        self.balllist.sort(reverse=0)
        blue_ball = random.randint(1, 16)
        self.balllist.append(blue_ball)


# 假设兑奖号码
prizenumber = Twocolor()
prizenumber.generate()
print('兑奖号码:', prizenumber.balllist)
print(' y 生成彩票号码| n 退出'.center(40, '*'))


while True:
    select = input('Please input:')

    if select == 'y':
        twocolor = Twocolor()
        twocolor.generate()
        print('机选号码:', twocolor.balllist)
        print('兑奖号码:', prizenumber.balllist)
        twocolor.prize(prizenumber.balllist)
        print(' y 生成彩票号码| n 退出'.center(40, '*'))
    else:
        print('欢迎下次再来送钱！！！')
        break'''


#########################################################################################

'''
class Car():  #父类

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()  #类无法使用title()，所以和形参使用,当调用类时，自动返回使用了title()的形参值

    def read_odometer(self):
        print('This car has ' + str(self.odometer_reading) + ' miles on it.')

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print('You can not roll back an odometer!')

    def increment_odometer(self, miles):
        self.odometer_reading += miles


class ElectricCar(Car):

    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery_size = 70

    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "-KWH battery. ")


my_tesla = ElectricCar('tesla', "model's", 2016)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()
'''

#################################################################################


'''
class Car():  #父类

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()  #类无法使用title()，所以和形参使用,当调用类时，自动返回使用了title()的形参值

    def read_odometer(self):
        print('This car has ' + str(self.odometer_reading) + ' miles on it.')

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print('You can not roll back an odometer!')

    def increment_odometer(self, miles):
        self.odometer_reading += miles

class Battery():
    def __init__(self, battery_size=70):
        self.battery_size = battery_size

    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "-KWH battery. ")


class ElectriCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()


my_tesla = ElectriCar('tesla', "model's", 2016)

print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
'''


###################################################################################


'''
class Car():  #父类

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()  #类无法使用title()，所以和形参使用,当调用类时，自动返回使用了title()的形参值

    def read_odometer(self):
        print('This car has ' + str(self.odometer_reading) + ' miles on it.')

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print('You can not roll back an odometer!')

    def increment_odometer(self, miles):
        self.odometer_reading += miles


class Battery():
    def __init__(self, battery_size=85):
        self.battery_size = battery_size

    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "-KWH battery. ")

    def get_range(self):
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270

        message = "This car can go approximately " + str(range)
        message += " mile on a full charge"
        print(message)


class ElectriCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()


my_tesla = ElectriCar('tesla', "model's", 2016)

print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
'''


#################################################################################################

'''
from collections import OrderedDict

favorite_language = OrderedDict()

favorite_language['fh'] = 'python'
favorite_language['cyl'] = 'java'
favorite_language['other'] = 'c'
favorite_language['FhCyl'] = 'c++'

for name, language in favorite_language.items():
    print(name.title() + "'s favorite_language is " + language.title() + '.')
'''

########################################################################################

'''
from collections import OrderedDict

alien = OrderedDict()

alien_1 = {'color': 'green', 'points': 5}
alien_2 = {'color': 'yellow', 'points': 10}
alien_3 = {'color': 'red', 'points': 15}

alien = [alien_1, alien_2, alien_3]

for message in alien:
    print(message)
'''

#########################################################################################

'''
from random import randint


class Die():
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        print(randint(1, self.sides))


six_die = Die()
print("Here are 10 rolling of 6 face die : ")
for i in range(10):
    six_die.roll_die()

print('\n')
ten_die = Die(10)
print("Here are 10 rolling of 10 face die : ")
for i in range(10):
    ten_die.roll_die()

print('\n')
twenty_die = Die(20)
print("Here are 10 rolling of 20 face die : ")
for i in range(10):
    twenty_die.roll_die()
'''


#################################################################################





































