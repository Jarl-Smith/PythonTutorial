# 类定义
class Man:
	# 定义基本属性
	number = 0
	# 定义私有属性,私有属性在类外部无法直接进行访问
	__number = 0

	# 定义构造方法
	def __init__(self, name='default', age=0):
		Man.number += 1
		self.__number = Man.number
		self.name = name
		self.age = age

	def sayHi(self):
		print('%d %s(%d years old) says Hi.' % (self.__number, self.name, self.age))
