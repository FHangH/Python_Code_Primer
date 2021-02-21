#Author:Fang hao 
#Time:2019/4/5 17:40


'''def greet_user():
    print('Hello !') #每一段定义语句或调用语句之间空两行，以保证美观！！！


def master_user():
    print('every one')


greet_user()  #调用函数
master_user()'''


####################################################
'''def great_user(name): #name是形参，等于变量名
    print('Hello ' + name.title() + '!')
    print('Good morning!')


great_user('fh') #fh是实参，调用函数时将其值赋予形参 '''


######################################################
'''def display_message(book_name):
    print('These is ' + book_name.title() + '.''\nHope you can learning best!')


display_message('python')'''


############################################################
'''def favorite_book(title):
    print('One of my favorite book is ' + title + '.')


favorite_book('Alice in wonderland')'''


##################################################################
'''def describe_pet(animal_type, pet_name):
    print('I have a ' + animal_type + '.')
    print('My ' + animal_type + "'s name is " + pet_name.title() + '.\n')


describe_pet('hamster', 'harry')
describe_pet('dog', 'deal')'''


####################################################################
'''def describe_pet(animal_type, pet_name):
    print('I have a ' + animal_type + '.')
    print('My ' + animal_type + "'s name is " + pet_name.title() + '.\n')


describe_pet(animal_type='hamster', pet_name='harry')

describe_pet(animal_type='dog', pet_name='deal')'''


#关键字实参可以定义形参和实参的对应值


################################################################################
'''def describe_pet(pet_name, animal_type='dog'):
    #animal_type指定了默认值，所以调用函数中只有一个形参，然而python依然将实参是为位置参数，所以将pet_name放在前面
    print('I have a ' + animal_type + '.')
    print('My ' + animal_type + "'s name is " + pet_name.title() + '.\n')


describe_pet(animal_type='hamster', pet_name='harry')
describe_pet('deal')'''


#s使用默认值时，在形参列表里必须先将为取默认值的形参，保证正确读取位置实参


################################################################################
'''def make_shirt(size, letter):
    print('Here is the information of your T-shirt.')
    print('size: ', size)
    print('letter: ', letter, '\n')


make_shirt('M', 'FH')
make_shirt(letter='FH', size='M')'''


##########################################################################
'''def make_shirt(size='M', letter='I love python'):
    print('Here is the information of your T-shirt.')
    print('size: ', size)
    print('letter: ', letter, '\n')


make_shirt()
make_shirt('L')
make_shirt(letter='FH')'''


#########################################################################
'''def describe_city(city, country='China'):
    print(city.title() + ' is in ' + country)


describe_city('shanghai')
describe_city('beijing')
describe_city('reykjavik', country='Iceland')#此处country可省略'''


#######################################################################
'''def get_formatted_name(first_name, last_name):
    full_name = first_name + ' ' + last_name
    return full_name.title()


musician = get_formatted_name('jim', 'hendrix')
print(musician)


#return作为返回值，方便清晰输出大量值'''


#########################################################################
'''def get_formatted_name(first_name, middle_name, last_name):
    full_name = first_name + ' ' + middle_name + ' ' + last_name
    return full_name.title()


musician = get_formatted_name('john', 'lee', 'hooker')
print(musician)'''


###########################################################################
'''def get_formatted_name(first_name, last_name, middle_name=''):
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()


musician = get_formatted_name('f', 'h')
print(musician)

musician = get_formatted_name('c', 'y', 'l')
print(musician)'''


###########################################################################
'''def build_person(first_name, last_name, age=' '):
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person


musician = build_person('jim', 'hendrix', age=27)
print(musician)'''


#############################################################################
'''import time


def get_formatted_name(first_name, last_name):
    full_name = first_name + ' ' + last_name
    return full_name.title()


while True:
    print('\nPlease tell me your name.')

    f_name = input('First name: ')
    if f_name == 'done':
        break
    l_name = input('Last name: ')
    if l_name == 'done':
        break

    time.sleep(1)
    formatted_name = get_formatted_name(f_name, l_name)
    print('-----------------------------------')
    print('\nHello, ' + formatted_name + ' !')
    time.sleep(1)
    print('-----------------------------------')
    print("\nIf you want exit program\nPlease enter 'done'.")
    print('-----------------------------------')
time.sleep(1)
print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
time.sleep(1)
print('Exit program..................')
time.sleep(1)
print('Thank you!')'''


########################################################################
'''def city_country(city, country):
    name = city.title() + ',' + country.title()
    return name


print(city_country('shanghai', 'china'))
print(city_country('beijing', 'china'))
print(city_country('hangzhou', 'china'))'''


######################################################################
'''def make_album(singer, title, songs=0):
    if songs == 0:
        return {'singer': singer, 'title': title}
    else:
        return {'singer': singer, 'title': title, 'songs': songs}


print(make_album('清风至', '落雨残叶'))
print(make_album('山下直人', '风道', 2))
print(make_album('羽肿', 'Wind Hill', 6))

while True:
    singer = input("Please enter singer's name : ")
    title = input("Please enter title's name : ")

    print(make_album(singer, title))

    ask = input("Do you still want to continue? \n(Y / N): ")
    if ask == 'N':
        print('Thank you!')
        break'''


########################################################################
'''def greet_users(names):
    for name in names:
        msg = 'Hello ' + name.title() + ' !'
        print(msg)


user_names = ['fh', 'cyl']
greet_users(user_names)'''


###################################################################
'''unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
complete_models = []

while unprinted_designs:
    current_design = unprinted_designs.pop()

    print('Printing model: ' + current_design)
    complete_models.append(current_design)

print('\nThe following models have been printed:')

for complete_model in complete_models:
    print(complete_model)'''


#########################################################################
'''unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []


def print_models(unprinted_designs, completed_models):

    while unprinted_designs:
        current_design = unprinted_designs.pop()

        print('Printing model: ' + current_design)
        completed_models.append(current_design)


def show_completed_models(completed_models):

    print('\nThe following models have been printed.')

    for completed_model in completed_models:
        print(completed_model)


print_models(unprinted_designs[:], completed_models)
show_completed_models(completed_models)'''


#通过调用unprinted_designs列表的切片既unprinted_design列表的副本，以保证保留原列表数据不会被修改。


###########################################################################
'''def show_magicians(magicians):
    for magician in magicians:
        print(magician)


magicians = ['FH', 'CYL']
show_magicians(magicians)'''


#############################################################################
'''def show_magicians(magicians):
    for magician in magicians:
        print(magician)


def make_great(magicians):
#直接用for循环无法修改magicians内的值
    i = 0
    while magicians[i] != magicians[-1]:
        magicians[i] = 'the Great ' + magicians[i]
        i = i + 1
    magicians[-1] = 'the Great ' + magicians[-1]
    return magicians


magicians = ['FH', 'CYL']
changed_magicians = make_great(magicians[:])
show_magicians(changed_magicians)
show_magicians(magicians)'''


'''def make_great(magicians, update_magician):  #不同版本
    while magicians:
        update = 'The Great ' + magicians.pop()
        update_magician.append(update)


def show_magicians(magicians):
    for magician in magicians:
        print(magician.title())


magicians_name = ['FH', 'CYL']
update_magician = []
make_great(magicians_name, update_magician)
show_magicians(update_magician)'''


'''def make_great(magicians, update_magician):
    while magicians:
        update = 'The Great ' + magicians.pop()
        update_magician.append(update)


def show_magicians(magicians):
    for magician in magicians:
        print(magician.title())


magicians_name = ['FH', 'CYL']
update_magician = []
make_great(magicians_name[:], update_magician)
show_magicians(update_magician)
show_magicians(magicians_name)'''


#同样的结果亦可用以下方式，更简便


'''def show_magicians(magicians):
    for magician in magicians:
        print('the Great ', magician)


magicians = ['FH', 'CYL']
show_magicians(magicians)'''


########################################################################
'''def make_pizza(*toppings):
    print(toppings)


make_pizza('pepperoni')
make_pizza('mushroom', 'green peppers', 'extra cheese')'''


#传递任意数量实参给*toppings建立的元组


##########################################################################
'''def make_pizza(*toppings):
    print('\nMaking a pizza with the following toppings: ')
    for topping in toppings:
        print('-' + topping)
        

make_pizza('pepperoni')
make_pizza('mushroom', 'green peppers', 'extra cheese')'''


##########################################################################
'''def make_pizza(size, *toppings):
    print('\nMaking a ' + str(size) + '-inch pizza with the following toppings: ')
    for topping in toppings:
        print('-' + topping)


make_pizza(12, 'pepperoni')
make_pizza(16, 'mushroom', 'green peppers', 'extra cheese')'''


#当需要多个形参，将任意数量对应实参的形参放在最后，python默认将第一个值以此存储在形参中


#################################################################################
'''def build_profile(first, last, **user_info): #**user_info为创建一个可以存储任意对键—值的字典

    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last

    for key, value in user_info.items():
        profile[key] = value
    return profile


user_profile = build_profile('albert', 'einstein', location='princeton', field='physics')

print(user_profile)'''


#########################################################################
'''def make_sandwich(*foods):
    print("\nMake a sandwich with the following foods")

    for food in foods:
        print('-' + food)


make_sandwich('tuna')
make_sandwich('tomatoes', 'lecture', 'roast chicken')
make_sandwich('egg', 'butter')'''


#########################################################################
'''def build_profile(first, last, **user_info): #**user_info为创建一个可以存储任意对键—值的字典

    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last

    for key, value in user_info.items():
        profile[key] = value
    return profile


user_profile = build_profile('albert', 'einstein', location='princeton', field='physics')

print(user_profile)

my_profile = build_profile('F', 'H', age=21, height=175)
print(my_profile)'''


################################################################################################
'''def make_car(manufacture, type, **others):

    car = {}
    car['manufacture'] = manufacture
    car['type'] = type

    for key, value in others.items(): #遍历others字典，即color与tow_package的两对键值
        car[key] = value
    return car #将字典others中的键值返回存入car中


my_car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(my_car)'''


####################################################################################################


#第八章模块内容在pycharm_lesson8_mode中











