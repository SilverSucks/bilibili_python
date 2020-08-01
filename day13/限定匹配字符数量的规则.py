import re
'''
* 匹配前一个字符出现0次或无限次，即可有可无
'''
# result = re.match('[a-z]*[A-Z]*', 'faAsfAWFS _123')
# print(result.group())
'''
+ 匹配前一个字符出现1次或无限次，即至少要匹配一次
'''
# result2 = re.match('[a-z]+[A-Z]+', 'aA')
# print(result2.group())

# 变量名的正则表达式
# pattern = '[a-zA-Z_]+[\w]*'
# res = re.match(pattern, 'Name3')
# print(res.group())
'''
? 匹配前一个字符出现1次或0次,表示可选
'''
# result3 = re.match('P?y', 'Python')
# print(result3.group())
'''
花括号的使用：{min, max}  匹配前导字符min次到max次，min和max必须都是非负整数
{min,} max被省略的话，表示max没有限制了
{,max} min被省略的话，表示只有max起作用
'''
# result = re.match('\d{,6}', '12345678')
# if result:
#     print('匹配成功{}'.format(result.group()))

# 匹配邮箱   XXXX@XXX.com
print(re.match('[A-Za-z_.0-9]{6,20}@qq.com', 'kangleli.vip@qq.com').group())
