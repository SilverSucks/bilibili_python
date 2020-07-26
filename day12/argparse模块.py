'''
argparse 模块可以轻松编写用户友好的命令行界面。
该程序定义了它需要的参数，argparse并将找出如何解析这些参数sys.argv。
该argparse模块还会自动生成帮助和用法消息，应在用户给出程序无效参数是发出错误
'''
import argparse
parser = argparse.ArgumentParser(prog='my-program', usage='%(prog)s[options] usage',
                                 description='my-自定义解析程序', epilog='my-epilog')

parser.add_argument('age', type=str, help='你的年龄')
# 添加可选参数
# parser.add_argument('-s', '--sex', action='append', type=str, help='你的性别')

# 参数限定在一个范围  输入格式为：python argparse模块.py 18 -s 男
parser.add_argument('-s', '--sex', default='男', choices=['男', '女', 'male', 'female'],
                    type=str, help='你的性别')

result = parser.parse_args()   # 开始解析参数
print(result.age, result.sex)