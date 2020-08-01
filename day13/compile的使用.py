'''
compile将正则表达式模式编译成一个正则表达式对象
优点：在使用正则表达式进行match操作是，python会将字符串转为正则表达式对象
如果使用compile则只需要完成一次转换即可，以后再使用模式对象的话无需重复转换
'''
import re
pattern = '\d{4}'
reobj = re.compile(pattern)    # 先去创建模式对象
result = reobj.match('12345')
print(result.group())