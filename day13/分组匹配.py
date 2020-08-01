import re
'''
分组匹配
| 匹配左右任意一个 表达式
（）将括号中字符作为一个分组
'''
# pattern = 'qwert123|qwert'
# res = re.match(pattern, 'qwert123')
# if res:
#     print(res.group())
#     pass
# print('-------------()分组匹配，将括号中字符作为一个分组----------------')
# 匹配电话号码  区号-电话号
# res = re.match('([0-9]{4})-(\d*)', '0395-1235432')
# print(res.group())
# print(res.group(1))
# print(res.group(2))

# ^ 有两种含义： 1.以XXX开头  2 表否定， ^- 代表只匹配不是横杠的字符
# res = re.match('([^-]*)-(\d*)', '0395-1235432')
# print(res.group())

# \num的使用 , 引用分组num匹配到的字符串，即前面匹配过的数据，后面可以直接来用
# htmlTag = '<html><h1>测试数据</h1></html>'
# res = re.match(r'<(.+)><(.+)>(.+)</\2></\1>', htmlTag)
# print(res.group(1))
# print(res.group(2))
# print(res.group(3))

'''
在使用组引用的时候，如果有多个组就容易造成混乱
这时候就可以给分组起别名
(?P)分组起别名
(?P=name) 引用别名为name分组匹配到的字符串
'''
print('-------------给分组起别名--------------')
pattern = r'<(?P<name1>\w*)><(?P<name2>\w*)>.*</(?P=name2)></(?P=name1)>'
res = re.match(pattern, '<div><h1>www.bytedance.com</h1></div>')
print(res.group())