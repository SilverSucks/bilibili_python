'''
通过模拟用户的登陆，来训练分支结构
要求：用户输入用户名和密码，判断是否正确，正确则登陆成功，错误提示输入不正确

'''

# 从数据库中查询到的数据
username = "lkl"
password = "123"

# print('-----------------------双分支结构----------------------')
# # 用户输入
# usr = input('请输入用户名：')
# pwd = input('请输入密码：')
# if username == usr and password == pwd:
#     print('欢迎{}'.format(usr))
#     pass  #空语句，占位语句。作用：表示这个分支结束，体现在敲回车键后，光标缩进的位置。
# else:
#     print('用户名或密码错误！')
#     pass
# print('---------------------单分支结构结束---------------------------')

'''
多分支结构：
特征：
1.只要满足其中一个分支，就会退出本层if语句结构【必定会执行】
2.至少有两种情况可以选择
elif 后面必须要写上条件和语句
else 根据实际情况来写，不一定必须要写。
'''
# 多分支demo，用户注册。条件：用户名密码必填，年龄大于等于18
# print('-------------------多分支练习，用户注册-------------------')
# usr = input('请输入用户名：')
# pwd = input ('请输入密码：')
# age = input('请输入年龄：')
# age = int(age)
# print(type(age))
# if usr == '':
#     print('请输入用户名！')
#     pass
# elif pwd == '':
#     print('请输入密码！')
#     pass
# elif age < 18:
#     print('年龄不符合规定！注册失败')
#     pass
# else:
#     print('欢迎{},您的年龄是{}'.format(usr, age))
# print('------------------用户注册---------------------')

'''
多分支练习，猜拳头
0：石头  1：剪刀  2：布
用户给定一个类型，石头或剪刀或布
计算机随机生成一个，比较二者，得出结果
'''
# 导入随机数random模块
import random

print('----------------------石头剪刀布------------------------')

people = input('（0代表石头，1代表剪刀，2代表布）请输入：')# 用people代表人为的输入
people = int(people)  #字符串转为int类型
computer = random.randint(0,2)   #随机生成一个0,2之间的整数
print('你的输入为：{}'.format(people))
print('计算机的为：{}'.format(computer))

# if people == computer:
#     print('好吧，打平了~~')
#     pass
# elif people == 0 and computer == 1:
#     print('真棒，你赢了~')
#     pass
# elif people == 1 and computer == 2:
#     print('真棒，你赢了~')
#     pass
# elif people ==2 and computer == 0:
#     print('真棒，你赢了~')
#     pass
# else:
#     print('输了哦~')


if people == 0:   # 对于人为给出0的时候，计算给出的三种情况一一判断
    if computer == 0:
        print('打平了呢~')
        pass
    elif computer == 1:
        print('真棒，你赢了~')
        pass
    else:
        print('输了哦~')
    pass
elif people == 1: # 对于人为给出1的时候，计算给出的三种情况一一判断
    if computer == 0:
        print('输了哦~')
        pass
    elif computer == 1:
        print('打平了呢~')
        pass
    else:
        print('真棒，你赢了')
        pass
    pass
elif people == 2: # 对于人为给出2的时候，计算给出的三种情况一一判断
    if computer == 0:
        print('真棒，你赢了')
        pass
    elif computer == 1:
        print('输了哦~')
        pass
    else:
        print('打平了呢~')
        pass
    pass


