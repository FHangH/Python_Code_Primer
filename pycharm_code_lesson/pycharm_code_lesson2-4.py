#author:fang hao & time:2019/3/5


'''name = 'cyl i love you'
print(name.title())
print(name.upper())
print(name.lower())'''


######################
'''frist = 'hello,'
second = 'world!'
name = frist + second
print(name.title())'''


########################
'''print('FH\nCYL')'''

##########################
'''text_language = '   hello,world!   '
print(text_language.rstrip())
print(text_language.lstrip())
print(text_language.strip())'''


######################
'''age = 22
message = ' Happy ' + str(age) + 'rd birthday! '
print(message)'''


##################
'''names = ['fh', ' cyl', 'none']
word = ' love'
print(names[0] + word + names[1])
print(names[-1])
print(names[0].title() + word + names[1].title())'''


######################
'''Lists = ['name', 'CYL', 'none']
print(Lists)

Lists = ['name', 'CYL', 'none']
Lists[0] = 'FH'
print(Lists)

Lists = ['name', 'CYL']
Lists.append('FH ')
print(Lists)

Lists = ['FH', 'CYL']
Lists.insert(1, 'Love')
print(Lists)

Lists = ['FH', 'CYL', 'others']
del Lists[2]
print(Lists)

Lists = ['FH', 'CYL', 'others']
popped_Lists = Lists.pop()
print(Lists)
print(popped_Lists)

Lists = ['FH', 'CYL', 'others']
Lists.remove('others')
print(Lists)'''

##########################
'''Lists = ['FH', 'CYL', 'others']
words = 'others'
Lists.remove(words)
print('Here is not ' + words)'''

###############################
'''words = ['a', 'b', 'd', 'e', 'c']
words.sort()
print(words)

words.sort(reverse=True)
print('\n', words)'''

#################################
'''words = ['a', 'b', 'd', 'e', 'c']
print(words)
print('\n', sorted(words))
print(words)'''

################################
'''words = ['a', 'b', 'c', 'd', 'e']
print(words)

words.reverse()
print('\n', words)

words.reverse()
print(words)

print(len(words))'''


########################################
'''for numbers in range(1, 21):
    print(numbers)'''


##################################
'''for numbers in range(1, 1000001):
    print(numbers)'''


################################
'''numbers = list(range(1, 1000001))
print(min(numbers))
print(max(numbers))
print(sum(numbers))'''


###################################
'''numbers = [value*1 for value in range(1, 20, 2)]
print(numbers)'''

'''numbers = list(range(1, 21, 2))
print(numbers)'''


##################################
'''numbers = [value*1 for value in range(3, 31, 3)]
print(numbers)'''

'''numbers = []
for value in range(3, 31, 3):
    numbers.append(value)
    print(numbers)'''


#########################################
'''sum = 0
for i in range(1, 11):
    sum += i*i
    print(sum)'''

'''numbers = [value**2 for value in range(1, 11)]
list = []
for n in numbers:
    list.append(int(n))
numbers = list
sum(numbers)
print(sum)'''
#待改善

'''numbers = [value**2 for value in range(1, 11)]
print(sum(numbers))'''

###############################
'''numbers = [value**3 for value in range(1, 11)]
print(numbers)'''

'''numbers = []
for value in range(1, 11):
    numbers.append(value**3)
    print(numbers)'''


##############################
'''players = ['a', 'b', 'c', 'd', 'e']
print(players[0:3])
print(players[1:4])
print(players[:4])
print(players[2:])
print(players[-3:])'''


#####################################
'''words = ['a', 'b', 'c', 'd', 'e']
print('This words:')
for word in words:
    print(word.title())'''


#####################################
'''words = ['a', 'b', 'c']
english = words[:]

print('This words are:')
print(words)

print("\nNew words are:")
print(english)'''


'''words = ['a', 'b', 'c']
new_words = words[:]

words.append('d')
new_words.append('e')

print('This words are:')
print(words)

print('\nNew words are:')
print(new_words)'''


#将new_words = words[:]改为new_words = words
'''words = ['a', 'b', 'c']
new_words = words

words.append('d')
new_words.append('e')

print('This words are:')
print(words)

print('\nNew words are:')
print(new_words)'''


'''list_f = ['FH', 'CYL',]
list_s = list_f[:]

list_f.append('Others')
list_s.append('He')

print('First names:')
print(list_f)

print('\nSecond names:')
print(list_s)'''


######################################
'''math = (200, 50)
print(math[0])
print(math[1])'''


#元组的值不可修改，试图修改后，运行结果显示错误
'''math = (200, 50)
math[0] = 100
print(math[0])'''


'''maths = (200, 50)
for math in maths:
    print(math)'''


'''words = ('a', 'b', 'c', 'd')
print('This words:')
for word in words:
    print(word.title())

words = ('a', 'b', 'e', 'f')
print('\nNew words:')
for word in words:
    print(word.title())'''


#################################
'''value = input('输入：')
answer = eval(value)
print('计算结果：%s = %d' % (value, answer))'''


##############################################
'''year = input('输入年份：')
year = int(year)
if (year % 400 == 0) or (year % 4 == 0) and (year % 100 != 0):
    print('%d is a leap year' % year)
else:
    print('%d is not a leap year' % year)'''


################################################################
'''print('输入done终止程序！')

while True:
    year = input('请输入年份：')
    if year == 'done':
        print('程序已终止！！！')
        break
    year = int(year)
    if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
        print(str(year) + '是闰年')
    else:
        print(str(year) + '不是闰年')'''


#######################################################
'''print('按done结束程序')
while True:
    x = input('请输入数字：')
    if x == 'done':
        print('exit')
        break
    else:
        x = int(x)
        if (x % 2 == 0):
            print(str(x) + ' 是偶数')
        else:
            print(str(x) + ' 是奇数')'''


############################################################
'''import datetime
d = datetime.datetime.now()
num = d.weekday()

if num == 0:
    tips = '星期一'
elif num == 1:
    tips = '星期二'
elif num == 2:
    tips = '星期三'
elif num == 3:
    tips = '星期四'
elif num == 4:
    tips = '星期五'
elif num == 5:
    tips = '星期六'
else:
    tips = '星期日'
print('今天是：' + tips)'''



#####################################################
'''import time

today = int(time.strftime('%w'))
print('今天是：星期' + str(today))'''


#################################################
'''for x in range(1, 10):
    for y in range(1, x+1):
            print('%s×%s = %s ' % (x, y, x * y), end='')
    else:
        print()'''

'''s = ''
for x in range(1, 10):
    s = ''
    for y in range(1, x+1):
        s = s + str(x) + '*' + str(y) + '=' + str(x*y) + ' '
        print(s)'''


#############################################################
'''n = 0
x = 1
list1 = []
print(x)
while n <= 7:
    n = n + 1
    x = x + n
    if x <= 29:
        print(x)'''


###############################################################
'''try:
    alp = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'R', 'S', 'T', 'U', 'V']
    idx = eval(input('Enter: '))
    print(alp[idx])
except NameError:
    print('please enter numbers!')
except IndexError:
    print('The index can not across 21 !')
else:
    print('The program is done!')
finally:
    print('Thank you !')'''



###################################################################
'''list2 = ['CPU', '内存'], ['硬盘', '声卡']
for i in range(len(list2)):
    for j in range(len(list2[i])):
        print(list2[i][j], end=' ')'''


###################################################################
'''list1 = range(10)
list2 = range(11, 20)

for index, value in enumerate(list1):
    print('list1的第%d个元素是【%s】'%(index, value))
for index, value in enumerate(list2):
    print('list2的第%d个元素是【%s】'%(index, value))'''


#######################################################################
'''numbers = range(10)

for index, value in enumerate(numbers):
    print('numbers的第%d个元素是【%s】' % (index, value))'''


#for语句和enumerate()函数同时遍历列表的元素索引和元素值

##########################################################################
'''t = ('A', 'B', 'C')
print('t元组： ', t)
L = list(t)
print('L的元素： ', L)'''


###################################################################
'''prime_number = []

n = input('Please enter numbers:\nn =  ')
m = input('m = ')
n = int(n)
m = int(m)

for i in range(n, m):
    for j in range(2, i):
        if i % j == 0:
            break
    if i == j + 1:
        prime_number.append(i)
print('prime number : ', prime_number)'''


###################################################################
'''def sum(list):
    total = 0
    ouput = ' '
    for x in range(len(list)):
        ouput = ouput + str(list[x]) + ' + '
        total += list[x]

    print(ouput.rstrip(' + '), '=', total)


list = [15, 25, 35, 65]
sum(list)'''


################################################################
'''def delRepeat(str):
    str = 'aabbccddeefab'
    str1 = set(str)
    str2 = list(str1)
    str2.sort()
    str1 = ''.join(str2)
    print(str1)


delRepeat('aabbccddeefab')'''



