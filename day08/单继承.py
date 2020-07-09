'''
单继承
'''
class Animal():    # 动物类
    def eat(self):
        print('正在吃')
        pass
    def drink(self):
        print('正在喝')
        pass
    pass

class Cat(Animal):  #  继承动物类
    def song(self):
        print('喵喵叫')
        pass
    pass

class Dog(Animal): # 继承动物类
    def song(self):
        print('汪汪叫')
        pass
    pass

cat = Cat()
cat.eat()