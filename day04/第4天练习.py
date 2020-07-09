'''
1，写函数，接收n个数字，求着写参数数字的和
'''
def Sum(*args):   # 定义函数，接收到的数字进行求和
    sum = 0
    for item in args:
        sum += item
        pass
    return sum
    pass
# result = Sum(1,2,3,4,5,6)
# print('累加和为：', result)

'''
2.写函数，找出传入的列表或元组的奇数位对应的元素，并返回一个新的列表
'''
def GetElem(*args):  # 对于可选输入，参数会作为一个元素放到一个元组中
    list = args[0]   # 取出所传入的参数
    # print(list)
    result = []   #定义一个空列表接收奇数位对应的元素
    for i in range(len(list)):  # 遍历接收到的列表或数组
        if i%2 == 0:  # 符合条件追加到列表result中,下标从0开始
            result.append(list[i])
            pass
        pass
    return result  # 返回列表resul
# a = [1, 2, 3, 'asdf', 234.5]   # 定义一个测试变量
# a = (1,2,4,'asdf',45.7)
# b = GetElem(a)   # 函数返回结果复制给b
# print('奇数位对应的元素为：', b)

'''
写函数，检查传入字典的每一个value的长度，如果大于2，那仅保留前两个长度的内容
并将新的内容返回给调用者。PS：字典中的value只能是字符串或列表
'''
def  dictChange(**kwargs):
    for item in kwargs: # kwargs 为字典类型
        if len(str(kwargs[item])) >= 2:  # 如果对应的value值大于2，保留前两个长度的内容
            kwargs[item] = kwargs[item][0:2]  # 前两个长度的值覆盖原有的value值
    return kwargs
    pass
# 测试数据
testdata = {'name':'jack', 'age':[23,24,28], 'phone':'19818965697'}
result = dictChange(**testdata)
print(result)


