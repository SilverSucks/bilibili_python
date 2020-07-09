'''
break 代表中断结束，满足条件直接结束本层循环
案例：对于猜拳游戏，只要赢了3局就自动退出
'''
import random
score = 0  #初始分数为0分，赢一局加一分
while True:
    print ('----------------------石头剪刀布------------------------')

    people = input ('（0代表石头，1代表剪刀，2代表布）请输入：')  # 用people代表人为的输入
    computer = random.randint (0, 2)  # 随机生成一个0,2之间的整数
    if people == '0' or people == '1' or people == '2':  #用于规范用户的输入，限制只能输入0,1,2
        people = int (people)  # 字符串转为int类型
        print ('你的输入为：{}'.format (people))
        print ('计算机的为：{}'.format (computer))
        if people == computer:
            print ('好吧，打平了~~')
            pass
        elif people == 0 and computer == 1:
            print ('真棒，你赢了~')
            score += 1
            pass
        elif people == 1 and computer == 2:
            print ('真棒，你赢了~')
            score += 1
            pass
        elif people == 2 and computer == 0:
            print ('真棒，你赢了~')
            score += 1
            pass
        else:
            print ('输了哦~')
        pass
    else:
        print('输入不正确，请输入0或1或2')
        pass
    if score == 3:   # 如果分数累计到3分，退出循环，结束游戏
        break
        pass
    pass
