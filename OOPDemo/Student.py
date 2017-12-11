from OOPDemo.Man import Man


# 单继承示例
class Student(Man):

	def __init__(self, name='default', age=0, grade='high school'):
		# 调用父类的构函
		Man.__init__(self, name, age)
		self.grade = grade

	# 覆写父类的方法
	def sayHi(self):
		print('%d %s(%d years old) , grade : %s says Hi' % (self.number, self.name, self.age, self.grade))
