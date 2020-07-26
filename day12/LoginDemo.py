'''
模拟mysql登陆
'''
import argparse
parser = argparse.ArgumentParser(prog='mysql登陆', usage='%(prog)s[options] usage',
                                 description='my-自定义解析程序', epilog='my-epilog')

parser.add_argument('loginType', type=str, help='登陆系统类型')

# 添加可选参数
parser.add_argument('-u', dest='user', type=str, help='用户名')
parser.add_argument('-p', dest='pwd', type=str, help='密码')

result = parser.parse_args()   # 开始解析参数
if(result.user == 'root' and result.pwd == '123'):
    print('login sucess!')
    pass
else:
    print('用户名或密码不正确！')