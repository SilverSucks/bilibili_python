'''
正则表达式的练习
'''
import re
# 示例1
str = 'Python languge is strong'
# match 只能以xxx开头的字符串，第一个参数是正则，第二个参数是需要匹配的字符串
res = re.match('P', str)
print(res.group())  # 匹配成功使用group方法取出字符串
print(re.match('p', str, re.I).group())