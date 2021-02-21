#Author:Fang hao 
#Time:2019/4/13 19:20


'''import pizza as p #导入pizza模块

p.make_pizza(12, 'pepperoni')
p.make_pizza(16, 'mushroom', 'green peppers', 'extra cheese')'''


###################################################################
'''from pizza import make_pizza #导入特定模块，可以无需使用句点，将模块pizza导入make_pizza中

make_pizza(12, 'pepperoni')
make_pizza(16, 'mushroom', 'green peppers', 'extra cheese')'''


######################################################################
'''from pizza import make_pizza as mp

mp(12, 'pepperoni')
mp(16, 'mushroom', 'green peppers', 'extra cheese')'''


##########################################################################
'''from pizza import * #（*）可将模块中所有的函数导入，且不需要句点

make_pizza(12, 'pepperoni')
make_pizza(16, 'mushroom', 'green peppers', 'extra cheese')'''


###########################################################################

