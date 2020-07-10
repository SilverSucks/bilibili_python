'''
重写父类中的方法
使用父类中已经使用的变量，同时也可以在子类中添加新的变量
第一种方式：
使用  父类名.__init__()
第二种方式：
使用  super().__init__()
'''
# class A:
#     def __int__(self, price):
#         self.price = price
#     def chouyan(self):
#         print('抽帝豪烟')
#         pass
#     pass
# class B(A):
#     def __int__(self, num):
#         self.num = 20
#     def chouyan(self):
#         print('抽中华烟')
#         pass
#     pass
#
# b = B()
# b.chouyan()
# print(B.__mro__)

'''
显示地调用父类中的函数
'''
class AA(object):
    def __init__(self, price):
        self.price = price
        pass
    def chouyan(self):
        print('抽帝豪烟')
        pass
    def address(self):  # 产地
        print('漯河')
    pass
class B(AA):
    def __init__(self, price, name):  # 重写父类的init方法
        # AA.__init__(self, price)  # 调用父类的方法
        super().__init__(price)
        self.name = name   # 在子类中添加新的属性
    def chouyan(self):
        print('抽{},价格为：{}'.format(self.name, self.price))
        pass
    # def address(self):     # 属于重写类的方法
    #     super().address()   # 调用父类的方法
    # def __str__(self):
    #     return
    pass

b = B(50, '中华烟')
b.chouyan()
b.address()