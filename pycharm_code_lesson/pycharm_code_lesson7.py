#Author:fanghao & Time:2019/3/30 13:59
'''name = input('What is your name : ')
print('Hello, ' + name + ', nice to meet you!')'''


#####################################################
'''list = 'If you tell your name, we can help you .'
list += '\nWhat is your name ? ' + '\nPlease enter your name: '

name = input(list)
print('\tHello ' + name + ' nice meet you !')'''


################################################################
'''print('Hello ,what are type cars for you want?')
car = input("Please enter car's name : ")
print('Let me see if I can find you a ' + car + ' .')'''


################################################################
'''print('Hello, are you want to eat some foods !' + '\nNow ,please tell me how many people?')
numbers = input('How many people: ')
numbers = int(numbers)

if numbers > 8:
    print('Sorry , is not desk for you!')
else:
    print('Yes , please in here!')'''



###########################################################################
'''print("When you enter a numbers , I can tell you it's 10 times as 10 or not")
numbers = input('Enter numbers: ')
numbers = int(numbers)
if numbers % 10 == 0:
    print('\tThe numbers' + str(numbers) + ' is 10 times as 10 .')
else:
    print('\tThe numbers ' + str(numbers) + ' is not .')'''



##########################################################################
'''import time

print("Start : %s" % time.ctime())
time.sleep(0.8)
print("End : %s" % time.ctime())'''


##########################################################################
'''number = 1
while number <= 5:
    print(number)
    number += 1'''



############################################################################
'''print('Tell me something ,and I will repeat it to you!' +
      "\nEnter 'quit' to end the program." )

message = ''
while message != 'quit':
    message = input('Please enter : ')

    if message != 'quit':
        print(message)
    else:
        print('Program is done!')'''



##############################################################################
'''number = 0
while number < 10:
    number += 1
    if number % 2 == 0:
        continue
    print(number)'''



##############################################################################
'''x = 1
while x <= 5:
    print(x)
    #x += 1'''
#中断无限循环可用Ctrl + F2


#################################################################################
'''lists = 'where are you live in ?'
print("Enter 'quit' end this program!")
while True:
    city = input(lists + '\nEnter city: ')

    if city == 'quit':
        print('Program is done!')
        break
    else:
        print('Oh ! that ' + city.title() +' is so good !')'''



#################################################################################
'''import time
print('你好 ！！傻逼！！！')
time.sleep(1)
print('呦吼！！！')
time.sleep(1)
print('怎么！！不爽？？！！')
time.sleep(1)
print('不爽你干我啊！！！')
time.sleep(1)
print('哈哈哈哈！！！！！')
time.sleep(1)
while True:
    x = '嘤~嘤~嘤~嘤~嘤~嘤~嘤~嘤~嘤~嘤~嘤~嘤~嘤~嘤~嘤~嘤~嘤~嘤~嘤~嘤~嘤~嘤~'
    print(x)'''

#中断无限循环可用Ctrl + F2


#####################################################################################
'''print("Tell us would you want to add orders" +
      "\nWhen you enter 'OK', the program will be done.")

while True:
    msg = input('Would you want add : ')
    if msg == 'OK':
        print('Thank you !')
        break
    else:
        print('We will add ' + msg + ' into pizzas.')'''



#######################################################################################
'''print("May you tell me your age ?")

while True:
    age = input('Please enter your age : ')
    age = int(age)
    if age < 3:
        print('You are free of charge.')
    elif age >= 3 and age <= 12:
        print('You need to pay 10 dollars.')
    else:
        print('You need to pay 15 dollars.')

    buy = input('Do you still need to buy tikects ?\n(Y / N):')
    if buy == 'N':
        print('Thank you !')
        break'''


#####################################################################################
'''unconfirmed_users = ['alien', 'brian', 'candace']
confirmed_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print('Verifying user : ' + current_user.title())

    confirmed_users.append(current_user)
print('\nThe following users have been confirmed: ')

for confirmed_user in confirmed_users:
    print(confirmed_user.title())'''


##################################################################################
'''pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')
print(pets)'''


###################################################################################
'''responses = {}
polling_active = True

while polling_active:
    name = input('\nWhat is your name?\nEnter your name:  ')
    response = input('Which mountain would you like to climb someday?\nPlease enter:  ')

    responses[name] = response

    repeat = input('Would you like to let another person respond?\n(Yes | No): ')
    if repeat == 'No':
        polling_active = False

print('\n--- Poll Results ---')

for name, responses in responses.items():
    print(name + 'Would like to climb ' + responses + '.' )'''


#################################################################################
