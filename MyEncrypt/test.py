# 自定义加密解密程序
# 加密：将明文每个字符的ASCII码存储，每个字符之间以自定义分隔符来分割
# 解密：以分隔符来拆解密文保存到列表里，将最后一个空字符剔除,将ASCII码转换为字符保存到需要显示的变量中

message = 'The Elder Scroll V Skyrim'  # 明文
store = []  # 需要显示的变量
splitter = '%%'  # 分隔符

# 加密过程
if False:
	for c in message:
		store.append(str(ord(c)))  # 将明文的单个字符转换为ASCII码存储到列表中
	temp = splitter.join(store)  # 相邻两个元素添加分隔符保存到打印变量中
	try:
		with open('demo.txt', 'w') as file1:
			file1.write(temp)  # 将打印变量输出到文件中
		print('storage success')
	except IOError as ioe:
		print(str(ioe))
# 解密过程
else:
	try:
		with open('demo.txt', 'r') as file1:
			for line in file1:
				list_temp = line.split(splitter)  # 最后的空字符会保存到列表里
				for c in list_temp:
					store.append(chr(int(c)))  # 转换空字符会报错ValueError
	except IOError as ioe:
		print(str(ioe))
	except ValueError:
		pass
	finally:
		print(store)
