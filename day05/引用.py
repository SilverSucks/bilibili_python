'''
引用的练习
'''

#可修改类型
li = []  # 全局变量
def printAddress(x):  # 为普通形参(不可变类型，数字、字符串、元组)
    print('普通形参----不重新赋值x的地址是：', id(x))
    pass
def printAddress2(*x):  # 为可变长形参
    print('可变长形参-----不重新赋值x的地址是：', id(x))
    pass
def printAddress3(params):  # 为可变形参(列表，字典)
    li.append(1)
    print('修改列表后的引用地址：', id(li))
    pass

def ChangeValueThenPrintAddress(x):  # 为普通形参
    x = 2
    print('普通形参----重新赋值后x的地址是：', id(x))
    pass

def ChangeValueThenPrintAddress2(*x): # 为可变长形参
    x = 2
    print('可变长形参----重新赋值后x的地址是：', id(x))
    pass

a = 10
print('a的地址是：', id(a))  # 打印a的地址
printAddress(a)  # 调用printAddress函数
printAddress2(a)  # 调用printAddress2函数
ChangeValueThenPrintAddress(a)  # 调用ChangeValueThenPrintAddress
ChangeValueThenPrintAddress2(a)  # 调用ChangeValueThenPrintAddress2

print('-------------------------------可修改类型（列表、元组）----------------------------------')
print('原本li的地址为：', id(li))
printAddress3(li)




'''
打印结果如下：
a的地址是： 140715645785408
普通形参----不重新赋值x的地址是： 140715645785408
可变长形参-----不重新赋值x的地址是： 2648818368640
普通形参----重新赋值后x的地址是： 140715645785152
可变长形参----重新赋值后x的地址是： 140715645785152
-------------------------------可修改类型（列表、元组）----------------------------------
原本li的地址为： 2648787935816
修改列表后的引用地址： 2648787935816

小结：
在python中，万物皆对象，在函数调用的时候，实参传递的就是对象的引用
'''
