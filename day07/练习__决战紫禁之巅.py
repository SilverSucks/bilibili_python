'''
一个双人对战的小游戏
决战紫禁之巅有两个人物，西门吹雪以及叶孤城
属性：name玩家的名字
      blood玩家血量

方法：tong()捅对方一刀，对方掉10滴血
      kanren()砍对方一刀，对方掉15滴血
      chiyao()吃一颗药，补血10滴
      __str__打印玩家状态
'''
class Person():
    def __init__(self, name, blood):
        self.name = name
        self.blood = int(blood)
        pass
    def tong(self, cls):
        '''
        捅人的函数
        :param cls: 代表敌人
        :return:
        '''
        print('{} 捅了 {} 一下'.format(self.name, cls.name), end='，')
        cls.blood -= 10
        print('{} 还剩下 {} 滴血'.format(cls.name, cls.blood))
        pass
    def kanren(self, cls):
        '''
        砍人的函数
        :param cls: 为敌人
        :return:
        '''
        print('{} 砍了 {} 一下'.format(self.name, cls.name), end=',')
        cls.blood -= 15
        print('{} 还剩下 {} 滴血'.format(cls.name, cls.blood))
        pass
    def chiyao(self):
        '''
        吃药补血函数
        :return:
        '''
        self.blood += 10
        print('{} 吃了一片药，还剩 {} 滴血'.format(self.name, self.blood))
        pass
    def __str__(self):
        return '{}的血量为{}\n'.format(self.name, self.blood)

    pass

# 创建两个对象西门吹雪以及叶孤城
xi = Person('西门吹雪', 100)
ye = Person('叶孤城', 100)
i = 0 # 判断打了多少回合分胜负
while True:
    xi.kanren(ye)
    ye.tong(xi)
    # xi.tong(ye)
    ye.kanren(xi)
    xi.chiyao()
    ye.chiyao()
    print(xi)
    print(ye)
    i += 1
    if xi.blood <= 0 or ye.blood <= 0:  # 其中一个人没血就结束
        if xi.blood > ye.blood:    # 判断是比赛结果
            print('打了%d回合，西门吹雪胜出'%i)
            break
            pass
        elif xi.blood < ye.blood:
            print('打了%d回合，叶孤城胜出'%i)
            break
            pass
        else:
            print('打了%d回合,打成平手'%i)
            break
            pass
        pass

