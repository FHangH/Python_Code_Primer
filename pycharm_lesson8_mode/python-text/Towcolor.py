#Author:Fang hao 
#Time:2019/6/27 15:37


import random


class Twocolor():
    def __init__(self):
        self.rednum = []
        self.bluenum = 0

    def generate(self):
        count = 1

        while count <= 6:
            red = random.randint(1, 33)

            if red not in self.rednum:
                self.rednum.append(red)
                count = count + 1

            else:
                self.rednum.sort()

            self.bluenum = random.randint(1, 16)


while True:
    print(' y 生成彩票号码| n 退出'.center(40, '*'))
    select = input('y | n : ')

    if select == 'y':
        computer = Twocolor()
        computer.generate()

        yours = Twocolor()
        yours.generate()

        print('兑奖号码：')
        print('红球：', computer.rednum, '蓝球：', computer.bluenum)

        print('你的号码：')
        print('红球：', yours.rednum, '蓝球：', yours.bluenum)

        rednum = 0
        bluenum = 0

        for x in computer.rednum:
            if x in yours.rednum:
                rednum = rednum + 1

        if computer.bluenum == yours.bluenum:
            bluenum = 1

        print('中奖信息：', '红球：', rednum, '蓝球；', bluenum)

        if rednum == 6 and bluenum == 1:
            print('一等奖')
        elif rednum == 6 and bluenum == 0:
            print('二等奖')
        elif rednum == 5 and bluenum == 1:
            print('三等奖')
        elif rednum == 5 and bluenum == 0 or rednum == 4 and bluenum == 1:
            print('四等奖')
        elif rednum == 4 and bluenum == 0 or rednum == 3 and bluenum == 1:
            print('五等奖')
        elif rednum == 2 and bluenum == 1 or rednum == 1 and bluenum == 1 or rednum == 0 and bluenum == 1:
            print('六等奖')

    else:
        print('欢迎下次再来！')
        break

