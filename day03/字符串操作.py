'''
字符串操作

'''
# 首字母变大写
str = 'hello'
# print(str.capitalize())

# 是否以什么结束/开始
# print(str.endswith('O'))
# print(str.startswith('h'))

# 判断是否是字母和数字
# print(str.isalnum())

# 判断是否是字母
# print(str.isalpha())

# 判断是否是数字
# print(str.isdigit())

# 判断是否是小写
# print(str.islower())

# 循环取出所有值用 - 去连接

# 去除字符串中的空格
# a = '    nihao   '
# b = a.strip()
# print(b)

#复制字符串
# str = '你好'
# str2 = str   # str2 复制了 str,用的是同一个地址空间
# print('str的内存地址是%d'%id(str))  # id()函数 可以查看一个对象的内存地址
# print('str2的内存地址是：%d'%id(str2))

# find()函数，查找x是否在字符串中，返回所在字符串中的第一个位置，如果没有找到返回-1
datastr = 'Python Programming'
# print(datastr.find('p'))
# 使用index函数，检测字符串中是否包含子字符串，如果没有找到对应的字符串会报异常
# print(datastr.index('o'))

# 转换成小写
# print(datastr.lower())
# 转换成大写
# print(datastr.upper())

# 字符串切片
# [start:end:step]  左闭右开，左边包括，右边不包括
print(datastr[2:5])   # 输出下标2-5之间的字符串
print(datastr[:5])    # 输出前5个字符
print(datastr[5:])    # 输出下标从5开始到结束的字符串
print(datastr[::-1])  # 倒序输出字符串