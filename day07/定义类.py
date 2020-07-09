'''
# 定义类和对象
# 类结构  类名 属性 方法
class 类名：
    属性
    实例方法（类中的方法叫实例方法）
'''
# class Person(object):
#     '''
#     定义Person类封装人的特征和属性
#     '''
#     # name = 'lkl'  # 类属性 姓名
#     age = 23      # 类属性 年龄
#     '''
#     对应人的行为  实例方法
#     '''
#     def __init__(self):
#         self.name = 'lkl'  # 定义在方法里面使用self引用的属性称之为实例属性
#         pass
#     def eat(self):         # 实例方法，第一个参数默认是self（名字标识可以是其他的名字，但这个位置必须被占用）
#         print('该吃饭了')
#         pass
#     def run(self):
#         print('跑步了')
#         pass
#     def study(self):
#         print()
#     pass

# 创建一个对象[类的实例化]
# people1 = Person()
# people1.eat()
# # people1
# print(people1.name)

'''
__init__ 
1.python自带的内置函数
2.是一个初始化的方法，用来定义实例属性和初始化数据的，创建函数时自动调用
3.利用传参机制，使定义功能更加丰富
self是什么
self和对象指向同一个内存地址，可以认为self就是对象的引用
self可以理解为自己，某个对象调用其方法时，python解释器会把这个对象作为第一个参数传递给
self，开发者只需要传递后面的参数即可

小结：
1.self只有在类中定义实例方法的时候才有意义，在调用时候不必传入相应的实参，有解释器自动指向
2.self本身并不是一个关键，可以更改，只是约定俗成地定义为self
3.self指的是 类实例对象本身，相当于java中的this关键字
'''
class Animal(object):
    # 创建一个初始化方法
    def __init__(self, name, color):
        self.name = name
        self.color = color
        pass
    def changeName(self, name):
        self.name = name
    def Print(self):
        print(self.name, self.color)
    def getSelf(self):
        print('地址空间是=%s'%(id(self)))
        pass
    pass

cat = Animal('小猫', '黑白色')
print(type(cat))
cat.Print()
cat.changeName('大猫')
cat.Print()

dog = Animal('dog', '小花狗')
print('dog对象的地址空间是：', id(dog))
dog.getSelf()

