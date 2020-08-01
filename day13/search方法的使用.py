'''
search在全文中匹配一次，匹配到就返回
'''
import re

# result = re.search('bc', 'abcd')  # 在整个字符串中匹配，匹配到第一个就返回
# print(result.group())
'''
re.findall() 查询字符串中某个正则表达式全部的非重复出现的情况
返回一个符合正则表达式的结果列表
'''
# print('-------------findall()方法的使用-------------')
# data = 'I love you, beause you love me and you are lovely'
# rs = re.findall('l.', data)
# research = re.search('l.', data)
# print(rs)
# print(research.group())

# 改造一下使用compile
# reobj = re.compile('l.')  # 创建一次正则对象转换
# print(reobj.search(data).group())
# print(reobj.findall(data))

'''
re.sub  将匹配到的数据进行替换
re.subn 将匹配到的数据进行替换，还返回被替换的数量，以元组的形式返回
'''
# print('-------------sub,subn根据匹配进行字符串替换-------------')
# res = re.sub('h', 'H', 'hello world,henan luohe', 2)
# res2 = re.subn('h', 'H', 'hello world, henam luohe', 2)
# print(res)
# print(res2)

print('-------split 根据匹配进行切割字符串,并返回一个列表------------')
res = re.split(',','hello,world,hello,henan', 2)  # 2 代表切割的次数为2
print(res)

