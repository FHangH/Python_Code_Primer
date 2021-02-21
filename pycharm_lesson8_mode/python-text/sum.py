#Author:Fang hao 
#Time:2019/6/27 15:37


'''from functools import reduce

list = [-1, 12, 3, 4, 5, -9]
flist = filter(lambda x: x > 0, list)
sum = reduce(lambda x, y: x + y, flist)

print('列表中的正数和为： ' + str(sum))'''


##################################################################\


from functools import reduce

list = [-1, 12, 3, 4, 5, -9]
flist = filter(lambda x: x > 0, list)
sum = reduce(lambda x, y: x + y, flist)

print(sum)








