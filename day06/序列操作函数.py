print('------------------------------all()函数的使用----------------------------')
'''
序列操作  指的是str、list、元组
all()  对象中的元素除了0、空、FALSE 外都算true。
类似于路基运算符and，所有元素都为True,结果才为True
注意：空元组、空列表返回值为True
'''
print('参数为空列表返回值为：', all([]))  #True
print('参数为空元组返回值为：', all(()))  #True
print('all((1,2,3,0))返回值为：', all((1,2,3,0)))  # 其中有一个是0，结果就为False

# any() 参数为元组或列表，其中只要有一项不是0，空，false都算True
# any()内置函数类似于逻辑运算符 or的判断
print('any(1,False)输出值为：', any([1, False]))


print('------------------------------sorted()函数的使用----------------------------')
'''
sorted()函数对多有可迭代对象进行排序操作
sort和sorted区别
1.sort是应用在list上的方法，sorted可以对所有可迭代的对象进行排序操作
2.list的sort方法返回的是对已经存在的列表进行操作，而内置函数sorted方法
返回的是一个新的list，而不是在原来的基础上进行的操作
'''
# 用内置函数sorted操作后内存地址发生变化了
a = [2, 3, 1, 5, 3]
print('a的内存地址为：{}，\n用内置函数排序后的内存地址为：{}'.format(id(a), id(sorted(a))))

print('sorted(a)输出结果为：', sorted(a))
print('sorted(a, reverse=False)', sorted(a, reverse=True)) # 倒序输出
print("sorted(['a', 'b', 'D', 'c'])结果为：", sorted(['a', 'b', 'D', 'c'], key=str.lower))


print('------------------------------zip()函数的使用----------------------------')
'''
# zip()函数用于将可迭代的对象（str,list,tuple）作为参数，将对象中对应的元素打包成一个个元组，
# 然后返回由这些元组组成的列表
'''
a = zip([1, 2, 3], ['a', 'b', 'c'])
print("zip([1, 2, 3], ['a', 'b', 'c']的结果为：", a)
print('list(a)的结果为：', list(a))

# 如果可迭代对象的元素个数不一样，那么按照最少的那个迭代压缩最少元素进行可迭代对象
b = zip([1, 2, 3], ['a', 'b', 'c', 'e'])
print("zip([1, 2, 3], ['a', 'b', 'c', 'e'])", b)
print('list(b)', list(b))

'''
案例，使用zip实现一个快递分拣功能
一次性输入快递编号、快递公司、收货地址，进行一一匹配
'''
# def ExpressClassification():
#     '''
#     使用zip实现一个快递分拣功能
#     :return:
#     '''
#     ExpressList = [] # 定义列表用来存储快递编号、快递公司、收货地址信息（相当于存储数据库）
#     num = input('请输入快递编号（每个项以空格分隔）：')
#     expressCompany = input('请输入快递公司（每个项以空格分隔）:')
#     address = input('请输入收货地址（每个项以空格分隔）：')
#     numList = num.split(' ')  # 用空格进行分割
#     ECompanyList = expressCompany.split(' ')  # 用空格进行分割
#     addressList = address.split(' ')   # 用空格进行分割
#     expressInfo = zip(numList, ECompanyList, addressList)  # 把快递单号、快递公司、收货地址打包处理
#     print(expressInfo)
#     for expressItem in expressInfo:
#         '''
#         遍历图书信息进行存储
#         '''
#         dictInfo = {'快递单号':expressItem[0], '快递公司':expressItem[1], '收货地址':expressItem[2]}
#         ExpressList.append(dictInfo)  # 把每个数据项都加到列表中
#         pass
#     # 遍历图书信息列表（存储数据库），验证是否存储成功
#     for item in ExpressList:
#         print(item)
#         pass
#     pass
#
# ExpressClassification()  # 调用图书分类函数

print('----------------------------enumerate()枚举函数的使用---------------------------------')
'''
enumerate()函数用于将一个可遍历的数据对象（如列表、元组或字符串）组合为一个索引序列
'''
listObj = ['a', 'b', 'c']
print('第一种遍历方式，索引和数据项作为一个组合接收')
for item in enumerate(listObj):  # 第一种遍历方式
    print(item)
    pass
print('第二种遍历方式，索引和数据项分别接收')
for index,item in enumerate(listObj):   # 第二种遍历方式
    print(index, item)
    pass
print('遍历枚举类型的数据，从指定的下标开始')
for item in enumerate(listObj, 5):  # 遍历枚举类型的数据，从指定的下标开始
    print(item)
    pass
print('遍历字典')
dictA = {'name':'lkl', 'age':23, 'address':'luohe'}
for item in enumerate(dictA):
    print(item[0], item[1], dictA[item[1]])# item是一个元组，元组的第一元素为自动加的索引值，第二个才是key
    pass
