'''
输出
'''
name = "haha"
classname = "理工1902"
age = 18

# 第一种输出方式
print('my name is :%s \n班级:[%s] \nage is %d'%(name,classname,age))

# 第二种输出方式
print('我的信息是：', name, classname, age)

# 第三种输出方式，format 的使用
print('--------------format的使用-----------')
print('姓名是{},班级是{}，年龄是{}'.format(name,classname,age))

'''
输入，从键盘上获取外部的数据，把内存中的数据拿过来，通过变量接收
input  接收的键盘输入 都是str类型的，根据需要进行转换
'''
str = input("请输入一个字符串：")
print(str)
num = input('请输入一个数字：')
print(num)
print(type(num))
print('-----------------input and output demo--------------')
username = input("请输入您的用户名：")
password = input("请输入您的密码：")
usr = 'lkl'
pwd = '123'
if usr == username and pwd == password:
    print('欢迎{}~~'.format(username))
else:
    print('用户名或密码不正确')