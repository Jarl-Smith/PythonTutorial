import pickle


class Athlete(list):
	def __init__(self, a_name='default', a_dob=None, a_time=None):
		list.__init__([])
		self.name = a_name
		self.dob = a_dob
		self.extend(a_time)

	def top3(self):
		return self.name + ' : ' + str(sorted(set(self))[0:3])


# 从一个数据文件中读取数据并格式化，返回数据对象
def __get_data_from_file(filename):
	try:
		with open(filename, 'r') as file1:
			temp = file1.readline().strip().replace('-', '.').replace(':', '.').split(',')
			return Athlete(temp.pop(0), temp.pop(0), temp)
	except IOError:
		print(str(IOError))
		return None


# 接收文件列表，调用文件格式化模块，将返回的数据对象序列化到文件中
def __store_data(filelist):
	all_athlete = {}
	for file in filelist:
		athlete = __get_data_from_file(file)
		all_athlete[athlete.name] = athlete
	try:
		with open('allAthlete.pickle', 'wb') as store:
			pickle.dump(all_athlete, store)
	except IOError as ioe:
		print(str(ioe))
	except pickle.PickleError as pe:
		print(str(pe))


# 从序列化文件中读取数据
def __get_data():
	try:
		with open('allAthlete.pickle', 'rb') as get:
			all_athlete = pickle.load(get)
			return all_athlete
	except IOError as ioe:
		print(str(ioe))
	except pickle.PickleError as pe:
		print(str(pe))


# 该模块的入口
def load_data(filelist):
	__store_data(filelist)
	return __get_data()
