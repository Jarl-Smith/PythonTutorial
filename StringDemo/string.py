# 字符串在Python中作为序列，字符串是单个字符的字符串的序列，字符串一旦赋值将不可变

s = 'spam'
# 打印字符串长度
print(len(s))
# 通过索引访问单个字符
print(s[1])
# 通过反向索引来获取单个字符
print(s[-2])
# 字符串支持切片操作
print(s[1:3])

# 格式化替代操作示例
message = '{0} is a {1} year(s) old boy.'
print(message.format('John', 5))
print('%s is a %d year(s) old boy.' % ('John', 5))

# 三个引号常用于打印HTML或XML这样的内容
html = """<a href = {0}>baidu</a>""".format('www.baidu.com')
print(html)
