'''
python中的多继承
'''

# class Bicycle():   # 自行车类
#     def function(self):
#         print ('能骑')
#         pass
#     pass
#
# class Battery():   # 电池类
#     def electric(self):
#         print('能提供动力')
#         pass
#     pass
# class ElectricVehicle(Bicycle, Battery):  # 电动车继承了自行车和电池
#     def __int__(self):
#         print('电动车继承了自行车和电池的功能')
#         pass
#     pass
#
# EV = ElectricVehicle()
# EV.electric()
# EV.function()

'''
当多个父类中存在相同方法的时候，应该去调用哪一个

采取就近调用原则
首先会到C（自身）里面去查找，如果C中没有，就去继承类中去找
'''
# class A():
#     def shpe(self):
#         print('这是一个正方形')
#         pass
#     pass
#
# class B():
#     def shpe(self):
#         print('这是一个三角形')
#         pass
#     pass
# class C(B, A):  # 当两个或两个以上父类出现相同方法是，调用跟书写方式有关，谁在前调用谁
#     def shpe(self):
#         print('正方形和三角形的结合')
#     pass
# c = C()
# c.shpe()
# print(C.mro())   # 相同方法的执行顺序是C-B-A

'''
间接的级联继承
父类的调用中，可以跨级调用吗？
案例三，A是祖父类，B是父类，C是儿子类，祖父类中有eat()方法，父类中没有，那儿子类继承后能使用eat()方法吗
下面的例子，表示孙子类可以使用爷爷类中的方法
'''
# class A(object):
#     def eat(self):
#         print('eat方法')
#         pass
#     pass
# class B(A):
#     pass
# class C(B):
#     pass
# c = C()
# c.eat()
# print(C.mro())

'''
'''

