# 字符串在Python中作为序列，字符串是单个字符的字符串的序列，字符串一旦赋值将不可变

s = 'spam'
# 打印字符串长度
print(len(s))
# 通过索引访问单个字符
print(s[1])
# 通过反向索引来获取单个字符,字符串长度与反响索引值的和就是正向索引值
print(s[-2])
# 字符串支持切片操作
print(s[1:3])
print(s[-len(s):])
print(s[:-1])

# 格式化替代操作示例
# 转换目标的通用结构： %[(name)][flags][width][.precision]typecode 例如：%(salary)+6.2f
print('{0} is a {1} year(s) old boy.'.format('John', 5))
print('%s is a %d year(s) old boy.' % ('John', 5))
print('%(name)s is a %(age)s year(s) old boy.' % {'name': 'John', 'age': 5})

# 三个引号常用于打印HTML或XML这样的内容
html = """<a href = {0}>baidu</a>""".format('www.baidu.com')
print(html)

# windows路径以反斜杠划分子目录，以绝对路径作为字符串可能会发生转义
# windows路径示例：D:\new\text.dat
# 字符串前边加'r'可以将字符串里的所有转义字符转化为字面量，实质就是添加'\'将转义字符的'\'进行转义
directory = r'D:\new\text.dat'
try:
	with open(directory, 'w') as file1:
		file1.writelines(r'\t\r\n')
except IOError as ioe:
	print(str(ioe))

# 一个raw字符串不能以奇数个反斜杠结束，如果需要用单个的反斜杠结束一个raw字符串，
# 可以使用两个反斜杠并分片掉第二个反斜杠(r'1\nb\tc\\'[:-1])、手动添加一个反斜杠(r'1\nb\tc'+'\\')、
# 或者忽略raw字符串语法并在常规字符串中把反斜杠改为双反斜杠('1\\nb\\tc\\')

# 切片操作的第三个值为步进(stride),表示每隔k个元素索引一次
s = '1A2B3C4D5F'
print(s[::2])

# 函数和方法的参数可以使用位置或关键字名称来传递
print('{motto},{pork} and {food}'.format(motto='spam', pork='ham', food='spam'))

# 替代目标语法格式
# {fieldname!conversionflag:formatspec}
# fieldname是指定参数的一个数字或关键字，后面跟着可选的'.name'或'[index]'成分引用
# conversionflag可以是r、s或者a分别是在该值上对repr、str或ascii内置函数的一次调用
# formatspec指定了如何表示该值，包括字段宽度、对齐方式、补零、小数点精度等细节，并且以一个可选的数据类型编码结束
# 冒号后的formatspec组成形式上的描述如下：[[fill]align][sign][#][0][width][.precision][typecode]
