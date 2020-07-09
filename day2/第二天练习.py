'''
练习一
猜年龄小游戏，有三点需求
1.允许用户最多尝试3次
2.每尝试3次后，如果还没猜对，就问用户是否还想继续玩，如果回答Y或y，就继续让其猜3次，
以此往复，如果回答N或n,就退出程序。
3.如果猜对了，就直接退出

'''
# 游戏开始前，先设置一个谜底
# age = 23
#
# i = 1  # 用户玩游戏的次数
# flag = 'y' # 循环变量，当flag为 N 或 n 时结束游戏
# while flag == 'y' or flag == 'Y':
#     age_usr = input('请输入年龄：')
#     age_usr = int(age_usr)  # 把用户输入的年龄转为int型
#     if age == age_usr:
#         print('恭喜你，猜对了~')
#         # 用户猜对了，也要问是否继续玩
#         flag = input('还想继续玩吗？Y或y代表是/N或n代表否：')
#         if flag == 'Y' or flag == 'y':
#             i = 0  # 循环变量赋值为1，代表从第一局开始玩
#         elif flag == 'N' or flag == 'n':
#             print('游戏退出，欢迎下次光临~')
#             break
#         pass
#     i += 1
#     # 用户3次都没有猜对，问他是否要继续玩
#     if i > 3:
#         flag = input('还想继续玩吗？Y或y代表是/N或n代表否：')
#         if flag == 'Y' or flag == 'y':
#             i = 1  # 循环变量赋值为1，代表从第一局开始玩
#         elif flag == 'N' or flag == 'n':
#             print('游戏退出，欢迎下次光临~')
#             break
#         pass
#     pass


'''
练习二
输入您的身高（m）,体重（kg）。根据BMI公式（体重除以身高的平方）帮小王计算他的BMI指数，
并根据BMI指数：
低于18.5 过轻
18.5-25  正常
25-28    过重
28-32    肥胖
用if-elif判断，并打印结果
'''
# 提示用户输入身高体重
# height = input('请输入您的身高（m）：')
# weight = input('请输入您的体重（kg）：')
# 用户输入的身高体重转为int类型
# height = int(height)
# weight = int(weight)
# 根据用户输入的身高体重计算BMI指数
# usr_BMI = weight/(height ** 2)
flag = 'Y' # 循环控制变量
while flag == 'Y' or flag == 'y':
    # 提示用户输入身高体重
    height = input('请输入您的身高（m）：')
    weight = input('请输入您的体重（kg）：')
    # 用户输入的身高体重转为int类型
    height = float(height)
    weight = float(weight)
    # 根据用户输入的身高体重计算BMI指数
    usr_BMI = weight/(height ** 2)
    print('您的BMI指数是：%d'%usr_BMI)
    if usr_BMI < 18.5:
        print('您过轻了~')
        flag = input('您想继续测试吗？Y或y代表是/N或n代表否：')
        if flag == 'N' or flag == 'n':
            print('谢谢使用~')
            break
        pass
    elif usr_BMI < 25:
        print('您正常~')
        flag = input ('您想继续测试吗？Y或y代表是/N或n代表否：')
        if flag == 'N' or flag == 'n':
            print ('谢谢使用~')
            break
        pass
    elif usr_BMI < 28:
        print('您过重了~')
        flag = input ('您想继续测试吗？Y或y代表是/N或n代表否：')
        if flag == 'N' or flag == 'n':
            print ('谢谢使用~')
            break
        pass
    elif usr_BMI < 32:
        print('您肥胖~')
        flag = input ('您想继续测试吗？Y或y代表是/N或n代表否：')
        if flag == 'N' or flag == 'n':
            print ('谢谢使用~')
            break
        pass
    else:
        print('您严重肥胖~')
        flag = input ('您想继续测试吗？Y或y代表是/N或n代表否：')
        if flag == 'N' or flag == 'n':
            print ('谢谢使用~')
            break
        pass





