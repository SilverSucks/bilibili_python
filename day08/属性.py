'''
属性：分为类属性、实例属性
实例属性在每个实例中独有一份，而类属性是所有实例对象共有一份
实验结果显示：
通过类对象访问不了实例属性，但是修改过实例属性的值后就能访问了
比如，此案例中age是实例属性，直接打印Student.age会报AttributeError错误
'''
class Student:
    name = 'lkl'  # 类属性
    def __init__(self, age):
        self.age = age    # 实例属性
        pass
    pass
print('-----------------------------通过实例对象的方式访问属性，先创建对象，再访问-------------------------------')
s = Student(23)   # 创建实例对象
print('s类属性是：{}'.format(s.name))   # 通过实例对象访问类属性
print('s类实例属性是：{}'.format(s.age))# 通过实例对象访问实例属性
s.name = 'hahaha'   # 通过实例对象修改类中属性的值
s.age = 18
print('修改后的name属性的值为:{}'.format(s.name))
print('修改后的age的值为：{}'.format(s.age))
print('-------------------------通过类对象Student.name, Student.age进行访问，不用创建对象------------------------')
print('通过实例对象访问类属性：{}'.format(Student.name))  # 通过类对象访问类属性
Student.name = 'xiaohong'   # 用类对象的方式修改  类中name属性的值
Student.age = 19
print('通过实例对象修改后的类属性name的值为：{}'.format(Student.name))
print('修改后的age的值为：{}'.format(Student.age))

student2 = Student(16)
print(student2.name, student2.age)
# # print('通过实例对象访问实例属性：{}'.format(Student.age)) # AttributeError通过类对象访问不了实例属性
