import pickle

# 数据腌制，类似Java的序列化，文件访问模式只能是二进制模式读/写
# Python提供了一个标准库，名为pickle，他可以保存和加载几乎任何Python数据对象，包括列表
# 该模块是读取数据

message = []

try:
	with open('asd.txt', 'rb') as file:
		message = pickle.load(file)
except IOError:
	print(str(IOError))
except pickle.PickleError:
	print(str(pickle.PickleError))

print(message)
