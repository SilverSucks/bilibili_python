'''
魔术变量__all__的作用；
如果在一个文件中存在all变量，配合from XX import * 导入模块的方式，只导入__all__中已经声明的
元素（方法，变量等）
'''

__all__ = ['add', 'subtract']
def add(a, b):
    '''
    加法
    :param a:
    :param b:
    :return:
    '''
    return a + b

def subtract(a, b):
    '''
    减法
    :param a:
    :param b:
    :return:
    '''
    return a - b
def mult(a, b):
    '''
    乘法
    :param a:
    :param b:
    :return:
    '''
    return a*b

if __name__=='__main__':
    print('模块中的函数调用结果：', add(5,6))
    print('模块__name__变量=%s'%__name__)