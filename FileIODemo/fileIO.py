# 获取文件里的数据
# 1.指定打开文件模式(只读，只写等)
# 2.遍历文件里的数据
# 3.关闭文件

# python脚本会自动在windows和Unix的路径中使用斜杠表示字符串路径
# 例如打开文件的时候，'D:/new/text.dat'在window和Unix都有效

if True:
	# 该块为文件的读取实例
	man = []
	otherman = []
	try:
		file1 = open('md.txt', 'r')
		for line in file1:
			try:
				line = line.strip()
				line = line.replace(' ', '')
				(role, content) = line.split(':', 1)
				if 'Man' == role:
					man.append(content)
				elif 'OtherMan' == role:
					otherman.append(content)
			except ValueError:
				pass
		print(man)
		print(otherman)
	except IOError:
		print(str(IOError))
	finally:
		# locals()返回当前作用域中的变量集合,判断文件对象是否存在
		if 'file1' in locals():
			file1.close()
elif False:
	# 该块为文件的输入实例
	try:
		# with语句会自动处理所有以打开文件的关闭工作，即使出现异常也不例外
		with open('md.txt', 'a') as file1:
			file1.writelines('\nadditional content')
	except IOError:
		print(str(IOError))
