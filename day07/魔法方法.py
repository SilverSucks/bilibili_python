print('------------------魔法方法---------------------')
'''
python中的魔法方法，格式用'__'左右包裹
__str__方法
直接打印对象，输出结果

__new__和__init__函数的区别：
__new__类的实例化方法，必须要返回该实例，否者对象创建不成功。
注意：1.不声明的情况下，由python解释器自动提供__new__方法，直接返回了。如果显示声明了，就会执行显示声明的代码
      2.至少有一个cls参数，代表要实例化的类
      3.__new__函数执行要早于__init__  只有对象存在了，才回去执行__init__函数
      
__init__ 用来做数据属性初始化的操作，类似于java中的构造函数
'''

print('使用魔法方法的情况下：')
class Animal(object):
    # 创建一个初始化方法
    def __init__(self, name, color):
        self.name = name
        self.color = color
        print('----------init--------函数执行')
        pass
    # 定义__str__方法
    def __str__(self):
        '''
        打印对象，自定义输出格式
        :return:Animal的信息
        :return:Animal的信息
        '''
        return 'name is %s , color is %s'%(self.name, self.color)
    # 创建对象实例的方法
    def __new__(cls, *args, **kwargs):
        '''
        创建对象实例的方法，调用一次就会生成一个新的对象，cls就是class的缩写
        场景：可以控制创建对象的一些属性限制，经常用来做单例模式时候使用
        :param args:
        :param kwargs:
        :return:
        '''
        print('----------------------new----------------------方法执行')
        return object.__new__(cls)   # 这里是真正创建对象实例的，程序先执行__new__方法，创建对象，然后返回
    pass
dog = Animal('旺财', 'white')  # 实例化对象
print(dog)


