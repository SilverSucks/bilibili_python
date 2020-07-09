'''
递归函数，如果一个函数在内部不调用其他的函数，而是自己本身的话，这个函数就是递归函数
优点：
1.使代码看起来更加整洁、优雅
2.可以用递归将复杂任务分解成更简单的子问题
3.使用递归比使用一些嵌套迭代更容易
缺点：
1.递归逻辑很难调试，递归条件处理不好容易造成程序无法结束，直到达到最大递归错误（栈溢出，内存泄漏）
2.递归占用大量内存，耗费计算机资源
'''
# 案例一 求阶乘5！
# def factorial(n):
#     '''
#     递归实现
#     :param n:
#     :return:
#     '''
#     if n==1:
#         return 1
#     return n*factorial(n-1)
# print(factorial(3))



# 案例二，找出文件路径下的所有文件
import os # 引入文件操作模块
def findFile(file_Path):
    listRs = os.listdir(file_Path)  # 得到该路径下所有文件夹
    for fileItem in listRs:   # 遍历该路径下所有的文件夹
        full_path = os.path.join(file_Path, fileItem)  # 获取完整的文件路径
        if os.path.isdir(full_path):  # 判断是否是文件夹，是文件夹就调用自身
            findFile(full_path)
            pass
        else:   # 当遍历到文件是，打印文件
            print(fileItem)
            pass
        pass
    else:
        return
    pass

# 调用找出文件路径下所有文件的函数
findFile('')   # 第一个反斜杠是转义字符
