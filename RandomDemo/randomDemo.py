import random

poker = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

ro = random.Random()

# random()函数返回[0,1)之间的浮点数
print(ro.random())

# 从给定的序列中随机取出一个元素
print(ro.choice(poker))

# randint(a,b)函数返回[a,b]之间的整数
print(ro.randint(2, 4))
