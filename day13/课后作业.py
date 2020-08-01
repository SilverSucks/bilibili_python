'''
1.长度为8-10的用户密码（以字母开头，包含字母、数字、下划线）
'''
import re
# pattern = '[a-zA-Z]\w{8,10}'
# str = 's19970127asdf'
# res = re.match(pattern, str)
# if res:
#     print(res.group())
#     pass

'''
验证用户名，长度为6-18位英文字母组成
'''
# pattern = '[a-zA-z]{6,18}'
# str = 'asdhasdfasdfsljasdlfj'
# res = re.match(pattern, str)
# if res:
#     print(res.group())
#     pass

'''
验证邮箱，126,163邮箱：6-18个字符，可使用字母、数字、下划线，需要以字母开头
'''
# pattern = '^[a-zA-Z][a-zA-Z0-9_]{6,18}@[0-9]{2,3}.com'
# reobj = re.compile(pattern)
# res = reobj.match('kangleli@126.com')
# print(res.group())

'''
匹配手机号码(11位数字)
移动号码段:139、138、137、136、135、134、150、151、152、157、158、159、182、183、187、188、147
联通号码段:130、131、132、136、185、186、145
电信号码段:133、153、180、189
'''
# inputNum = input('请输入11位手机号：')
# pattern = '[0-9]{,11}'
# if len(inputNum) == 11:
#     res = re.match(pattern, inputNum)
#     if res:
#         print(res.group())
#         pass
#     pass

'''
'Save your heart for someone who cares' 
请使用正则将文本中的"s"替换成"S",请写Python代码完成匹配替换。
'''
# str = 'Save your heart for someone who cares'
# res = re.sub('s', 'S', str)
# print(res)

'''
'<span>三生三世，十里桃花</span>
<span>九州海上牧云记</span>
<span>莫斯科行动</span>' 
请使用正则将<span>标签中的全部内容匹配出来,请写Python代码完成匹配。
'''
pattern = r'<(?P<name1>\w*)>.*</(?P=name1)>'
str = '<span>三生三世，十里桃花</span><span>九州海上牧云记</span><span>莫斯科行动</span>'
res = re.match(pattern, str)
print(res.group())








