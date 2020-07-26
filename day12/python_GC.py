'''
python中的的垃圾回收（GC）用到了计数机制
sys.getrefcount()  统计一个对象被引用的次数
'''
import sys
import psutil
import os
import gc
def showMemSize(tag):
    '''
    显示内存空间大小的函数
    :return:
    '''
    pid = os.getpid()
    p = psutil.Process(pid)   # 得到进程对象
    info = p.memory_full_info()
    memory = info.uss/1024/1024   # 字节转换为M
    print('{}当前内存使用情况为：{}MB'.format(tag, memory))
    pass

# 验证循环引用的情况
def func():
    showMemSize('初始化')
    a = [i for i in range(900000)]
    b = [i for i in range(900000)]
    a.append(b)
    b.append(a)
    showMemSize('创建列表对象a,b之后')
    # del a   # 删除a
    # del b   # 删除b
    pass

func()
gc.collect()  # 手动释放
showMemSize('完成时候的')

# a = []
# print('a对象引用的次数为：', sys.getrefcount(a))  # a对象引用的次数为2
# b = a
# print('a对象引用的次数为：', sys.getrefcount(a))  # a对象引用的次数为3
# c = b
# d = b
# e = c
# f = d
# g = e
# print('a对象引用的次数为：', sys.getrefcount(a))  # a对象引用的次数为8

