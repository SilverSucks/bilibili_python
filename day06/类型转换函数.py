'''
强制类型转化，根据需要把数据转换成我们想要的类型
'''
# char() 数字转字符
print('数字转字符串chr(65)=', chr(65))

# bin() 转换为二进制的函数
print('十进制转二进制bin(10)=', bin(10))
print('十进制转十六进制hex(16)', hex(16))
# list()元组转为列表
tuple1 = ('asd', 1, 23.4, [6,7,8])
b = list(tuple1)
print('将元组转换为列表：', b)
print('将列表转换为元组：', tuple(b))

# 用dict创建一个字典
dict1 = dict(a=1,b='hello',c=[1,2,3])
print(dict1)