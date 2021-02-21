#Author:Fang hao 
#Time:2019/4/13 19:47


import hello
hello.hello_world()

from hello import hello_world
hello_world()

from hello import hello_world as say_hello_world
say_hello_world()

import hello as greeting
greeting.hello_world()

from hello import *
hello_world()