'''
字典是python中重要的数据类型，可以存储任意对象。字典是以键值对的形式创建的
创建方式：{'key':'value'}利用大括号包裹着。
字典中找某个元素时，根据键、值

注意：
1.字典不能通过索引访问。
2.字典的键（key）不能重复，值（value）可以重复。一般通过键（key）来访问
3.字典的键（key）只能是不可变类型，如数字，字符串，元组。

字典中常用的操作，增删改查都可
'''
# 创建字典
dict1 = {}  # 创建一个空的字典
print('创建的这个对象的类型是：', type(dict1))
# 向字典中增加元素
print('原有字典中的元素：', dict1)
dict1['name'] = '李易峰'
dict1['类型'] = '影视明星'
dict1['sex'] = '男'
print('向字典中添加一些个键值对后：', dict1)

# 通过键来取出字典中的元素（查询）
name = dict1.get('name')
print('name键 对应的值是：', name)

# 根据键依次取出字典中对应的值，并打印（查询）
for item in dict1:
    print('{}----->{}'.format(item,dict1.get(item)))
    pass
# 获取所有的键值对（查询）
print(dict1.items())

# 按照key排序 （排序）
print('按照key进行排序', sorted(dict1.items(), key=lambda d:d[0]))

# 修改字典中的元素（修改）
dict1['name'] = '段奕宏'
print('修改name键对应的值为"段奕宏"后', dict1)

# 删除字典中的元素（删除）
dict1.pop('sex')
print('删除字典中sex键对应的元素', dict1)


