'''
需求1：利用脚本完成自动备份，要求用户输入文件名称，完成自动备份
'''
def copyfile():
    # 接收用户输入的文件名
    old_file = input('请输入要备份的文件名：')
    file_list = old_file.split('.')
    # 构造新的文件名.加上备份后缀
    new_file = file_list[0] + '_备份.' + file_list[1]
    old_f = open(old_file, 'r')  # 打开需要备份的文件
    new_f = open(new_file, 'w')  # 以写的模式打开新文件，不存在则创建
    content = old_f.read()   # 将文件内容读取出来
    new_f.write(content)   # 将读取的内容写入备份文件
    # 将打开的问价关闭
    old_f.close()
    new_f.close()
    pass

# copyfile()

'''
需求2：
如果处理超大文件，一次将全部内容读取出来显然是不合适的，
在需求1的基础上改进代码，让它备份大文件也不会导致内存被占满
'''
def copyBigFile():
    # 接收用户输入的文件名
    old_file = input('请输入要备份的文件名：')
    file_list = old_file.split('.')
    # 构造新的文件名.加上备份后缀
    new_file = file_list[0] + '_备份.' + file_list[1]
    try:
        # 监视要处理的逻辑
        with open(old_file, 'r') as old_f,open(new_file, 'w') as new_f:
            while True:
                content = old_f.read(1024)  # 一次性读取1024个字符
                new_f.write(content)
                if len(content) < 1024:   # 读取数据的结束条件
                    break
        pass
    except Exception as msg:
        print(msg)
    pass