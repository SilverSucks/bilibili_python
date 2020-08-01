'''
. 的使用，匹配除了换行符以外的任意字符，一个点匹配一个字符
'''
import re
# data = 'adfasd'
# pattern = '..' # 匹配规则
# pattern2 = '李.'
# names = '小明', '小红', '小天', '李哥'  # 相当于一个列表
# res = re.match(pattern, data)
# print(res.group())
# for name in names:
#     res2 = re.match(pattern2, name)
#     if res2:
#         print(res2.group())
'''
[]中括号的使用，匹配中括号中的任意字符
'''
# print('--------------------[]中括号的使用-------------------')
# str1 = 'hello,Python'
# res = re.match('[he]', str1)  # 使用中括号括起来的内容，代表一个集合
# print(res.group())
#
# for i in range(0, len(str1)):
#     result = re.match('[a-z]', str1[i])
#     if result:   # 如果匹配上了，打印匹配上的字符
#         print(result.group(), end='')
#         pass
#     pass

'''
有标志位的匹配
re.match(pattern, string, flags),flags为标志位，用于控制正则表达式的匹配方式
如：区分大小写，多行匹配等
'''
# print('-------------有标志位的匹配----------------')
# str = 'Python is the best language iN the world'
# for i in str:
#     res = re.match('n', i, re.I)  # re.I 表示不区分大小写
#     if res:
#         print(res.group())
#         pass
#     pass

# print('-------------\d匹配一个数字  0-9 --------------')
# str = '123456789'
# for i in range(0, len(str)):
#     res = re.match('\d', str[i])
#     if res:
#         print(res.group(), end=' ')
#         pass
#     pass

# print('----------- \D匹配非数字----------------')
# str = 'asdfa1234234'
# pattern = '\D\D\D\D'
# res = re.match(pattern, str)
# print(res.group())

# print('----------- \s匹配空白，即空格和tab键----------------')
# str = 'asd  fa123   4234'
# pattern = '\s'
# for i in range(len(str)):
#     res = re.match(pattern, str[i])
#     if res:
#         print(res.group())
#         pass
#     else:
#         print('此处不是空格')
#     pass
# print('--------------\w 匹配单词字符，即a-z、A-Z、0-9---------------')
# str = 'asd_1fa123   4234'
# pattern = '\w\w\w\w\w'
# res = re.match(pattern, str)
# print(res.group())

'''
匹配字符串的开头 用 ^ 号
'''
# res = re.match('^P.*','Python is language')  # 匹配以P开头的字符串
# res = re.match('^P\w{5}', 'Python is language')  # 匹配以P开头的长度为5的字符串
# if res:
#     print(res.group())
'''
$ 匹配邮箱的结尾
'''
print('----------------限定匹配邮箱的结尾为.com----------------')
res = re.match('[a-zA-Z.]{6,20}@[\w]{2,5}.com$', 'kangleli.vip@gmail.com')
if res:
    print(res.group())


