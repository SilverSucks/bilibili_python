'''
类对象所拥有的的方法，需要用@staticmethod来表示静态方法，静态方法不需要任何参数

注意：一般不会通过实例对象访问静态方法，实例化对象会耗用一定的时间和资源

为什么要使用静态方法呢？
由于静态方法主要来存放逻辑性的代码，本身和类以及实例对象没有交互。
在静态方法中不会涉及到类中方法和属性的操作。数据资源能够得到有效的利用
'''
class Person:
    country = 'China'  # 类属性
    def __init__(self, name):
        self.name = name
        pass
    # 静态方法，用装饰器staticmethod装饰
    @staticmethod
    def get_country():  # 静态方法不用传任何参数
        return Person.country
    pass
# people = Person('xiaohong')
# result = Person.get_country()   # 获取类属性
# print(result)

# 案例二，返回当前的系统时间
import time   # 引入第三方的时间模块
class TimeNow():

    @staticmethod
    def showTime():
        return time.strftime('%H:%M:%S', time.localtime())
    pass
print(TimeNow.showTime())  # 通过类对象调用showTime()方法