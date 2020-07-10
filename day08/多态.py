'''
多态：顾名思义就是多种状态、形态
同一种行为对不同的子类有不同的行为表现
实现多态有两个前提：
1.必须存在继承，多态发生在父类和子类之间
2.重写，子类需要重写父类的方法

多态有什么用?
增加程序的灵活性
增加程序的扩展性

Python是弱类型语言 ，天生就支持多态，不虚言指定类型。 称 Python的鸭子类型
python中的鸭子类型，关注的不是对象的类型，而是它如何使用的
换句话说，不关注调用的对象是谁，只关注对象本身能不能使用某个方法
例如在下面的例子中，动物类【父类】中有say()方法，
                    人类【父类】中也有say()方法
就可以统一使用commonInvoke函数来调用say()方法
'''
# 案例一
class Animal:  # 父类
    '''
    动物类，父类【基类】
    '''
    def say(self):
        print('这是一个动物')
        pass
    pass

class Duck(Animal):
    '''
    鸭子类,子类，[派生类]
    '''
    def say(self):
        '''
        这部分重写父类的方法
        :return:
        '''
        print('这是一只鸭子')
    pass
class Dog(Animal):
    '''
    dog类，子类
    '''
    def say(self):
        print('这是一只牧羊犬')
        pass
    pass
class Cat(Animal):
    '''
    cat类，子类
    '''
    def say(self):
        print('这是一只波斯猫')
        pass
    pass
class People():
    '''
    人类【这是父类】
    '''
    def say(self):
        print('会说多种语言')
class Chinese(People):
    '''
    中国人【子类】
    '''
    def say(self):
        print('会说汉语')
    pass

# duck = Duck()
# dog = Dog()
# cat = Cat()
# duck.say()
# dog.say()
# cat.say()

#公共调用方法,传入不同对象，调用对象中的方法
def commonInvoke(obj):   # 多个类中有多个相同的方法是，可以把方法提取出来共同调用，提高程序的扩展性
    '''
    统一调用方法
    :param obj:
    :return:
    '''
    obj.say()
    pass
# 对象列表，用来存储对象
objList = [Duck(), Dog(), Cat(), Chinese()]
# 循环遍历列表中的对象，依次调用commonInvoke方法
for item in objList:
    commonInvoke(item)  # 调用commonInvoke方法
    pass



