#Author:Fang hao 
#Time:2019/4/13 19:19


def make_pizza(size, *toppings):
    print('\nMaking a ' + str(size) + '-inch pizza with the following toppings: ')
    for topping in toppings:

        print('-' + topping)
#以pizza为此模块的名称