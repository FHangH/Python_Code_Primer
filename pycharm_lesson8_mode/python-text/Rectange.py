#Author:Fang hao 
#Time:2019/6/27 15:36


class Rectange():
    def __init__(self, weight, height):
        self.weight = weight
        self.height = height

    def zc(self):
        zc = str((self.weight + self.height)*2)
        return zc

    def mj(self):
        mj = str(self.weight * self.height)
        return mj


data = Rectange(100, 200)
print('长方体的周长： ' + data.zc())
print('长方形的面积： ' + data.mj())


#########################################################################


'''class Rectange():
    def __init__(self, weight, height):
        self.weight = weight
        self.height = height

    def zc(self):
        zc = (self.height + self.weight)*2
        return zc

    def mj(self):
        mj = (self.weight * self.height)
        return mj


data = Rectange(100, 100)
print(data.zc())
print(data.mj())'''




