'''
python 中使用lambda关键字创建匿名函数，
所谓匿名即这个函数没有名字不用def关键字创建标准的函数
lambda 参数1，参数2，参数3:执行代码语句
特点：
    1.使用lambda关键字去创建函数
    2.没有名字的函数
    3.匿名函数冒号后面的表达式有且只有一个。冒号后面是表达式
    4.匿名函数自带return，而这个return的结果就是表达式计算后的结果
缺点：
    1.lambda只是单个表达式，不是一个代码块，lambda设计就是为了满足简单
    函数的功能，仅仅能封装有限的逻辑，复杂逻辑实现不了。
'''
# 使用lambda表达式计算两个数和：
test = lambda x,y:x+y
# 等价于如下函数
# def test(x, y):
#     return x + y
result = test(1,3)  # 第一种调用的方式
print('第一种调用的方式', result)

# 第二种调用的方式，在定义匿名函数后，直接传入参数
rs = (lambda a,b:a+b)(3,4)    # 直接调用
print('第二种调用的方式，定义时直接传入参数：', rs)

# 使用lambda创建匿名函数，接收可变长参数
test2 = lambda *x:print(x)
test2(1, 2, 3, 4, 5)

print('------------------------lambda与三元运算符-----------------------------')
age = 19
print('可以参军' if age>18 else '继续上学' ) #可以替换传统双分支的写法

# 定义匿名函数，输出两个数中最大的
MaxNum = lambda x,y:x if x>y else y
print('输出两个数中最大的数', MaxNum(3,34))