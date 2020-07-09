'''
内置函数
就是python安装后自带的函数

'''
print('---------------------常用数学运算函数-----------------------')
# abs()求绝对值
a = -10
print('abs()求绝对值函数', abs(a))
b = 3.1415926
# round()对浮点数近似取值
print('round()对浮点数进行近似取值，保留1位小数', round(b, 1))
print('round()对浮点数进行近似取值，保留2位小数', round(b, 2))
print('round()对浮点数进行近似取值，保留4位小数', round(b, 4))  # 此时进行了四舍五入
# pow()求指数
print('pow()求2的3次方结果：', pow(2,3))
print('pow(2,3,2)结果为2^3%2= ', pow(2,3,2))
print('pow(2,3,3)结果为2^3%3= ', pow(2,3,3))
print('pow(2,3,2)结果为2^3%4= ', pow(2,3,4))
print('pow(2,3,2)结果为2^3%5= ', pow(2,3,5))
print('pow(2,3,2)结果为2^3%6= ', pow(2,3,6))

'''
求商和余数
语法：divmod(a, b)
参数：a数字  b数字
返回值：一个包含商和余数的元组（a//b, a%b）
'''
print('divmod(7, 2)=', divmod(7, 2))
# print('divmod(3, 0)=', divmod(3, 0)) # ZeroDivisionError: integer division or modulo by zero

# max()求最大值
print('max(6,3,24,5,101)=', max(6, 3, 24, 5, 101))
# min()求最小值
print('min(6,3,24,5,101)=', min(6, 3, 24, 5, 101))

# sum()求和,传入的参数必须有一个是列表
print('sum([1],2)=', sum([1], 2))
print('sum[6,3,24,5,101]=', sum([6,3,24,5,101]))

'''
eval()函数用来执行一个字符串表达式，并返回表达式的值
语法：eval(expression[, globals[, locals]])
参数： 
'''
a,b,c = 1,2,3
print('eval("a+b+c")=', eval('a+b+c'))

# 通过eval()执行外部定义的函数
def TestFunc():
    print('我执行了吗')
    pass
eval('TestFunc()')   # 调用外部函数执行
