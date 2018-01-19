"""
数据腌制，类似Java的序列化，文件访问模式只能是二进制模式读/写
Python提供了一个标准库，名为pickle，他可以保存和加载几乎任何Python数据对象，包括列表
该模块是保存数据
"""

import pickle

message = ['1', 2, 'three', [20.3]]

try:
    with open('asd.txt', 'wb') as file1:
        pickle.dump(message, file1)
except IOError:
    print(str(IOError))
except pickle.PickleError:
    print(str(pickle.PickleError))
