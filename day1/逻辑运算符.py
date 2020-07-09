'''
逻辑运算符
and
or
not
'''

a,b,c,d = 0,1,2,3,
print(a and b)
print(a or b)
print(not a)
print(not b)
print(a<b and d<c)   # and 两边 全部微针才为真
print(a<b or d<c)    # or 两边一个为真，结果就为真
print(not a<b)       # 真假切换