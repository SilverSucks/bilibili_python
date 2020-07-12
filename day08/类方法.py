'''
类方法的声明：
在方法的上面加上  @classmethod
类方法的作用：类方法可以对类进行访问、修改
类方法的调用：类方法的调用同类属性的调用一样，可以通过实例对象和类对象调用
注意：通过下面实例的验证，发现无论是通过实例对象调用修改country的类方法还是
                         通过类对象调用修改的country，country的值都发生了变化
'''
class Person(object):
    country = 'China' # 类属性
    def __init__(self, name):
        self.name = name
        pass
    # 类方法，用装饰器classmethod装饰，调用方式和类属性一样，可以通过实例对象和类对象
    @classmethod
    def get_country(cls):
        return cls.country
        pass
    @classmethod
    def modify_country(cls, country):
        cls.country = country
    pass
print('----------------------通过实例对象访问-----------------------')
people = Person('haha')
print(people.get_country())
people.modify_country('Janpan')
print('修改后的country是：{}'.format(people.get_country()))

print('-----------------------通过类对象访问------------------')
result = Person.get_country()
print(result)
Person.modify_country('America')
print('修改后的country是：{}'.format(Person.get_country()))

