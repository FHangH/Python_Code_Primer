#author:fang hao & time:2019/3/12


'''
class Pass():
    def count_login(self, password):
        self.password = password
        input('Are you sure password: ' + str(self.password))

        if self.password == '752972182':
            print('验证成功!')
        else:
            print('密码错误，请重试')

ext = Pass()
ext.count_login(input('input password: '))
'''

#已改善
###############################################
#改善后的代码
'''password = input('password:')
password = int(password)
if password == 752972182:
    print('验证成功!')
else:
    print('密码错误，请重试')'''


##############################################
'''cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())'''


##################################################
'''words = 'A'
if words != 'B':
    print('False')
else:
    print('True')'''


##################################################
'''words = ['a', 'b', 'c', 'd']
if 'a' and 'b' in words:
    print('have')
else:
    print('none')'''


###################################################
'''name = 'Toffc Chan'
print("Is name == 'Toffc Chan' ? I predict True.")
print(name == 'Toffc Chan')

print("\nIs name == 'john'? I predict False.")
print(name == 'John')


car = 'FIT'
print("\nIs car == 'FIT'? I predict True.")
print(car == 'FIT')

print("\nIs car == 'BMW'? I predict False.")
print(car == 'BMW')'''


########################################################
'''name1 = 'Word'
name2 = 'word'
print(name1 == name2)
print(name1.lower() == 'word')'''


###########################################################
'''num1 = 6
num2 = 6.1
print(num1 == num2)
print(num1 != num2)
print(num1 > num2)
print(num1 < num2)
print(num1 >= num2)
print(num1 <= num2)'''


########################################################
'''name1 = 'Word'
name2 = 'word'

if name1 == 'word' and name2 == 'word':
    print(True)
else:
    print(False)

if name1 == 'word' or name2 == 'word':
    print('\nTrue')
else:
    print(False)'''


######################################################
'''name1 = 'FH' and 'CYL'
name2 = 'others'
name_list = ['Word', 'word', 'FH', 'CYL']
if name1 in name_list:
    print('FH CYL is in the name_list')

if name2 not in name_list:
    print('others is not in name_list')'''


##########################################################
'''age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
elif age >= 65:
    price = 5

print('Your admission cost is:' + str(price) + '.')'''


############################################################
'''age = 22

if age < 4:
    price = 0
elif age < 18:
    price = 5
else:
    price = 10

print('Your admission cost is:' + str(price) + '.')'''



#################################################################
'''names = ['FH', 'CYL']

if 'FH' in names:
    print('FH')
if 'CYL' in names:
    print('CYL')
if 'others' not in names:
    print('Here is not have others!')

print('\nHere is only have FH and CYL!')'''


####################################################################
'''alien_color = ['green', 'yellow', 'red']
alien = 'green'

if alien in alien_color:
    print('add 5')'''


#######################################################################
'''alien_color = 'green'
alien = 'red'

if alien == alien_color:
    point = 5
if alien != alien_color:
    point = 10

print('You have ' + str(point) + ' point!')'''


########################################################################
'''alien_color = 'green'
if alien_color == 'green':
    point = 5
elif alien_color == 'yellow':
    point = 10
else:
    point = 15

print('You have ' + str(point) + ' point!')


alien_color = 'yellow'
if alien_color == 'green':
    point = 5
elif alien_color == 'yellow':
    point = 10
else:
    point = 15

print('You have ' + str(point) + ' point!')


alien_color = 'red'
if alien_color == 'green':
    point = 5
elif alien_color == 'yellow':
    point = 10
else:
    point =15

print('You have ' + str(point) + ' point!')'''



########################################################
'''age = 20
if age < 2:
    word = 'baby'
elif age >= 2 and age < 4:
    word = 'learning walking'
elif age >= 4 and age < 13:
    word = 'children'
elif age >= 13 and age <20:
    word = 'teenager'
elif age >= 20 and age <65:
    word = 'adult'
else:
    word = 'elder'

print('He is ' + word + '.')'''


####################################################
'''favorite_fruits = ['banana', 'apple', 'lemon']
FF = favorite_fruits

if 'banana' in FF:
    print('You really like banana!')
if 'apple'in FF:
    print('You really like apple!')
if 'lemon' in FF:
    print('You really like lemon!')
if 'melon' in FF:
    print('You really like melon!')'''



###################################################
'''requested_toppings = ['mushroom', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print('Sorry, we are out of green peppers right now.')
    else:
        print('Adding ' + requested_topping + '.')
print('\nFinished making your pizza.')'''



########################################################
'''words = []

if words :
    for word in words :
        print('Adding ' + word + '.')
    print('\nFinished making your pizza !')
else:
    print('Are you sure you want a plain pizza !')'''




#######################################################################
'''users = ['admin', 'FH', 'CYL', 'others']
for user in users:
    print('Hello,' + user + '.')'''



###################################################################
'''users = ['admin', 'FH', 'CYL', 'others']

for user in users:
    if user == 'FH':
        print('Hello,FH would you like to see a status reports?')
    else:
        print('Hello,' + user + ' thank you for logging in again!')'''



###########################################################################
'''users = []
if users:
    for user in users:
        print('Hello!')
else:
    print('We need to find some users!')'''


#######################################################################


'''current_users = ['admin', 'FH', 'CYL', 'others', 'none']
new_users = ['FH', 'CYL', 'A', 'B', 'C']

for new_user in new_users:
    if new_user in current_users:
        print('FH and CYL are loves!')
    else:
        print('This ' + new_user + ' can be in !')'''



####################################################################
'''nums = list(range(1, 10))
for num in nums:
    if num == 1:
        print(str(num) + 'st')#print('1st')
    elif num == 2:
        print(str(num) + 'nd')#print('2nd')
    elif num == 3:
        print(str(num) + 'rd')#print('3rd')
    else:
        print(str(num) + 'th')'''



#############################################################
