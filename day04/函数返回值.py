'''
函数返回值
函数执行完会返回一个对象，如果在函数的内部有return 就可以返回实际的值，否则返回None
类型：可以返回任意类型，返回类型应该取决于return后面的类型
用途：给调用方返回数据
在一个函数体内可以出现多个return语句，但是只能返回一个
如果执行了return，以为函数执行完成，return后面的代码不会执行
'''
def Sum(a, b):
    sum = a + b
    return sum
    pass
print(Sum(10, 20))