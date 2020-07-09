'''
析构方法的概述
当一个对象被删除或者被销毁时，python解释器也会默认调用一个方法，
这个方法为__del__方法，也称为析构方法
'''


# 析构方法的定义
class Animal:
    def __init__(self, name):
        self.name = name
        print('这是构造方法')
        pass
    def __del__(self):
        print('这是析构方法')
        pass
    pass

cat = Animal('小花猫')

