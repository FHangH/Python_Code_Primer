#author:fang hao & time:2019/3/5

'''words = {'color': 'green', 'point': 5}

print(words['color'])
print(words['point'])'''


###################################################
'''words = {'color': 'green', 'point': 5}
new_point = words['point']

print('You just earned ' + str(new_point) + ' points!')'''



###############################################################
'''words = {'color': 'green', 'point': 5}
print(words)

words['X_position'] = 0
words['Y_position'] = 25
print(words)'''



##############################################################
#当字典键中包含多个子值时，子值需要用（）括起来
'''words = {'name': ('FH', 'CYL')}

words['color'] = 'green', 'yellow'
words['point'] = 5

print(words)'''



###############################################################
'''words = {'color': 'green'}
print('The color is ' + words['color'] + '.')

words['color'] = 'yellow and green'
print('These color is ' + words['color'] + '.')'''
#如何将多个子值替换原键中的子值



##########################################################
'''words = {'X_position': 0, 'Y_position': 25, 'speed': 'medium'}
print('Old X_position :' + str(words['X_position']))

if words['speed'] == 'slow':
    X_increment = 1
elif words['speed'] == 'medium':
    X_increment = 2
else:
    X_increment = 3

words['X_position'] = words['X_position'] + X_increment

print('New X_position :' + str(words['X_position']))'''



#############################################################
'''words = {'color': 'green', 'point': 5}
print(words)

del words['color']
print(words)'''



############################################################
'''language = {
    'FH': 'python',
    'CYL': 'c',
    'Others': 'java'
    }

print('FH favorite language is ' +
      language['FH'].title() +
      ' !')'''
#拆分打印时，在末尾加上‘+’


#############################################################
'''list = {}

list['first_name'] = ' f'
list['last_name'] = ' h'
list['city'] = 'wuhu'
list['age'] = 21
print(' first name is ' + list['first_name'].title() +
      '\n last name is' + list['last_name'].title() +
      '\n city is ' + list['city'].title() +
      '\n age is ' + str(list['age'])
      )'''
#待改善

#改善后
'''list = {}

list['first_name'] = ' f'
list['last_name'] = ' h'
list['city'] = ' wuhu'
#list['age'] = 21
#for循环输出不适应字符串和数字混合字典内容

for key, value in list.items():
    print(key + ' is' + value.title())'''

#依然有待改善，寻找可以解决可以用循环语句输出字符串和数字混合的字典内容


###################################################################
'''numbers = {'FH': 24,
           'CYl': 24,
           'Others': 233
           }

for name, value in numbers.items():
    print(name + "'s favorite num is " + str(value) + '.')'''



#######################################################################
'''voc = {
    'print': 'Display information in one line',
    'if': 'Run the language in the following indentation if the condition matches.',
    'for': 'Traverse the element in the list or tuple , etc.',
    'while': 'Loop until the condition matches',
    'range': 'Create an integer list object.'
    }

print('print:' + voc['print'])
print('if:' + voc['if'])
print('for:' + voc['for'])
print('while:' + voc['while'])
print('range:' + voc['range'])'''


#改善后

'''voc = {
    'print': 'Display information in one line',
    'if': 'Run the language in the following indentation if the condition matches.',
    'for': 'Traverse the element in the list or tuple , etc.',
    'while': 'Loop until the condition matches',
    'range': 'Create an integer list object.'
    }

for key, value in voc.items():
    print(key + ':' + value)'''

#for后key为 键位， value为对应键值


######################################################################################
'''users = {
    'name': 'fh',
    'first': 'f',
    'last': 'h'
    }

for uer, value in users.items():
    print(uer.title() + ': ' + value.title() + '.')'''



###################################################################################
'''users = {
    'name': 'fh',
    'first': 'f',
    'last': 'h'
    }

for use in users.keys():
    print(use.title())

print('\n')

for value in users.values():
    print(value.title())'''



#######################################################################################
'''favorite_language = {
    'fh': 'python',
    'cyl': 'c',
    'ken': 'python',
    'others': 'java'
    }

friends = ['fh', 'cyl']

for name in favorite_language.keys():
    print(name.title())

    if name in friends:
        print('Hi ' +
              name.title() +
              ',I see your favorite language is ' +
              favorite_language[name].title() +
              '!'
              )'''



####################################################################
'''favorite_language = {
    'fh': 'python',
    'cyl': 'c',
    'ken': 'python',
    'others': 'java'
    }

if 'Erin' not in favorite_language.keys():
    print('Erin ,please take our poll!')'''



##########################################################################
'''favorite_language = {
    'fh': 'python',
    'cyl': 'c',
    'ken': 'python',
    'others': 'java'
    }

for name in sorted(favorite_language.keys()):
    print(name.title() + ' ,thank you for talking the poll.')'''
#sorted()将将键以首字母顺序输出



############################################################################
'''favorite_language = {
    'fh': 'python',
    'cyl': 'c',
    'ken': 'python',
    'others': 'java'
    }

print('The following languages have been mentioned:')

for language in set(favorite_language.values()):
    print(language.title())'''
#set()可以去除值中重复的项



################################################################################
'''favorite_language = {
    'fh': 'python',
    'cyl': 'c',
    'ken': 'python',
    'others': 'java'
    }

names = ['fh', 'cyl', 'ken', 'others', 'bob', 'john']

for name in names:
    if name in favorite_language.keys():
        print(name.title() + ' ,thank you for taking the poll!')
    else:
        print(name.title() + ' ,may you do  a simple poll?')'''



#######################################################################
'''alien1 = {'color': 'green', 'points': 5}
alien2 = {'color': 'yellow', 'points': 10}
alien3 = {'color': 'red', 'points': 15}

aliens = [alien1, alien2, alien3]

for alien in aliens:
    print(alien)'''



########################################################################
'''aliens = []

for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[:5]:
    print(alien)
print('.....')

print('Total number of aliens: ' + str(len(aliens)))'''



###########################################################################
'''aliens = []

for alien_number in range(0, 30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15
for alien in aliens[0:5]:
    print(alien)
print('......')'''



##########################################################################
'''pizza = {'crust': 'thick',
         'toppings': ['mushroom', 'extra cheese'], }

print('You ordered a ' + pizza['crust'] + '-crust pizza ' +
      'with the following topping:')

for topping in pizza['toppings']:
    print('\t' + topping)'''



#############################################################################
'''favorite_language = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell']
    }

for name, languages in favorite_language.items():
    print('\n' + name.title() + "'s favorite languages are: ")

    if len(languages) <= 1:
        print('\n' + name.title() + "'s favorite languages is C ")
    else:
        for language in languages:
            print('\t' + language.title())'''


#################################################################################
'''users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'eninstein',
        'location': 'princeton'
        },

    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris'
        }

    }

for username, user_info in users.items():
    print('\nUsername: ' + username)
    full_name = user_info['first'] + ' ' + user_info['last']
    location = user_info['location']

    print('\tFull name: ' + full_name .title())
    print('\tLocation: ' + location.title())'''



######################################################################

