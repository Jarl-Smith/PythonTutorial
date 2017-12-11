from OOPDemo.Man import Man
from OOPDemo.Student import Student

# 实例化类
john = Man('John', 22)
alice = Man('Alice', 22)
john.sayHi()
alice.sayHi()

# 实例化子类
a = Student('Jane', 15, 'middle school')
a.sayHi()
