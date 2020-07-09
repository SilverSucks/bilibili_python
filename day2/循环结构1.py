'''
循环的分类
1.while循环
2.for循环
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
while循环语法结构：
while 条件表达式：
    代码
语法特点：
1.有初始值
2.条件表达式
3.变量【循环体内计数变量】的自增自减，否则会造成死循环
使用条件：循环的次数不确定，依靠循环条件来结束
目的：为了将相似或者相同的代码变得更加简洁，使得代码可以重复利用
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
for循环
语法特点：遍历操作，依次取集合容器中的每个值
循环格式：
for 临时变量 in 字符串，列表等：
    执行代码块

通过对比发现：
while使用：适用于对未知的循环次数 用于判断
for使用：适用于已知的循环次数【可迭代对象遍历】
'''

# while 的使用，案例一，输出1~100之间的数
# 定义索引变量
# index = 1
# while index <= 100:
#     print (index)
#     index += 1
#     pass

# 案例二：对猜拳游戏进行改进，使得可以进行多次猜拳
# 导入随机数random模块
# import random
# while True:
#     print ('----------------------石头剪刀布------------------------')
#
#     people = input ('（0代表石头，1代表剪刀，2代表布）请输入：')  # 用people代表人为的输入
#     computer = random.randint (0, 2)  # 随机生成一个0,2之间的整数
#     if people == '0' or people == '1' or people == '2':  #用于规范用户的输入，限制只能输入0,1,2
#         people = int (people)  # 字符串转为int类型
#         print ('你的输入为：{}'.format (people))
#         print ('计算机的为：{}'.format (computer))
#         if people == computer:
#             print ('好吧，打平了~~')
#             pass
#         elif people == 0 and computer == 1:
#             print ('真棒，你赢了~')
#             pass
#         elif people == 1 and computer == 2:
#             print ('真棒，你赢了~')
#             pass
#         elif people == 2 and computer == 0:
#             print ('真棒，你赢了~')
#             pass
#         else:
#             print ('输了哦~')
#         pass
#     else:
#         print('输入不正确，请输入0或1或2')

# 打印三角形
# i = 1
# while i <= 5:
#     j = 1
#     while j <= i:
#         print('*',end='')
#         j += 1
#         pass
#     print('\n')
#     i += 1

# 案例三：打印九九乘法表
# i = 1   #表示行数 1~9
# while i <= 9:   #外循环控制行
#     j = 1  #表示列数  1~9
#     while j <= 9-i+1:  #内循环控制列
#         print('{}*{}={}'.format(j,10-i,j*(10-i)),end=' ')  #想方设法把i，j的值与对应程式中的数对应起来
#         j += 1
#     print('\n')
#     i += 1

'''
练习，打印等腰三角形如下：
    *
   ***
  *****
观察发现，该等腰三角形由空格和*号组成，可以分为左右两部分（列数为3 和 列数为2 两部分，行数都为3行）
'''
# 第一种方式
# row = 1
# while row <= 3: # 外层循环控制行数
#     # print(row)
#     a = 1
#     # 打印左半部分 列数为3的部分,而左半部分又分为上下两部分
#     while a <= 3: # 打印 1~3列
#         if a <= 3 - row:
#             print (' ', end='')  # end=''表示不换行
#         else:
#             print ('1', end='')
#         a += 1
#     b = 1
#     while b < 3:  #打印 4~5列，循环两次
#         if b < row:
#             print('1', end='')
#             pass
#         else:
#             print(' ', end='')
#         b += 1
#     row += 1
#     print ('\n')


# 打印等腰三角形的第二种方式
# row = 1   # row代表行数
# while row <= 3:  #外层循环 1~3 循环三次
#     m = 1
#     while m <= 3-row :      # 打印左边空格
#         print(' ', end='')
#         m += 1
#         pass
#     n = 1
#     while n <= 2*row-1:    # 打印1
#         print('1', end='')
#         n += 1
#         pass
#     row += 1   # 控制行数的变量自增
#     print('\n')

# 用for循环嵌套打印九九乘方表
row = 10
col = 10

for i in range(1, row):
    for j in range(1,col-i+1):
        print('{}*{}={}'.format(j,i,i*j),end=' ')
        j += 1
        pass
    print('\n')
    i += 1
    pass
