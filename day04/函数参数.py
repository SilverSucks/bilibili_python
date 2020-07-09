'''
参数的分类：
必选参数、默认参数[缺省参数]、可选参数、关键字参数
参数：函数为了实现某项特定的功能，进而为了得到实现功能所需的数据
掌握：
1.普通参数
2.可变长参数  *args   接收的类型是元组
3.关键字可选参数  **kwargs 传入类型为字典
注意使用顺序：混合使用时，把确定参数放在最前面，可选参数第二位置，关键字可选参数第三位置
'''


def printName(name):  # name 为形式参数，在定义时不占用内存地址
    '''
    用来打印名字的函数
    :param name:
    :return:
    '''
    # name = input('请输入姓名：')
    print ('输入的名字是', name)
    pass


printName ('lkl')  # 函数的调用，括号中为实际参数，是实际暂用内存地址的


# 默认参数
def sum(a=10, b=20):
    print ('缺省参数的使用：', a + b)
    pass


# 调用带有默认参数的函数，调用时如果未赋值，就会用默认的参数值
sum (15, 20)


# 可选参数（不定长参数），当参数个数不确定时使用
def getArg(*args):   # 获取参数的函数
    '''
    可变长的参数类型，获取用户输入的参数
    :param args:
    :return:
    '''
    print ('不定长的参数：', args)
    for item in args:
        print(item)
        pass
    pass

# 调用不定长的参数
getArg((1, 2, 3, 4, 5, 6, 7), [10, 20])  # 传入实参是任意的


# 关键字可变参数，参数为字典类型，键（key）是一个字符串
def keyFunc(**kwargs):   # 用**kwargs默认代表可变关键字参数
    print('关键字可变类型参数的类型为：', type(kwargs))
    print('传递的参数为；', kwargs)
    pass
keyFunc()
# 调用传递参数的keyFunc()
dict1 = {"name":"lkl", "age":23}
# keyFunc(dict1)   # 直接传递是不行的
keyFunc(**dict1)   # 正确的传参要加上**

# 一般在使用的过程中，通常混合使用，有普通参数、可变参数、关键字可变参数等
def complexFunc(name, *args, **kwargs):
    '''
    多参数的组合使用
    :param name:
    :param args:
    :param kwargs:
    :return:
    '''
    print('输入的参数为：', (name, args, kwargs))
    pass
# 调用complexFunc
complexFunc('fas', ['随意给个类表'], **{'随意给个字典':'字典1'})

# def complexFunc2(**kwargs, *args):  # error，可选参数要放在前面，关键字可选参数放在后面
#     '''
#     测试参数的顺序
#     :param kwargs:
#     :param args:
#     :return:
#     '''