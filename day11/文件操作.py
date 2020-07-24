'''
打开文件，在python中打开文件使用open函数，可以打开一个已经存在的文件，
或者创建一个新文件

'''
# fileObj = open('./a.txt', 'w', encoding='utf-8')
# 文件操作，读/写操作
# fileObj.write('jing')
# fileObj.write('疑似地上霜')
# fileObj.close()

# 以二进制的形式去写数据
# fobj = open('./b.txt', 'wb')
# fobj.write('举头望明月\n'.encode('utf-8'))
# fobj.close()

# 以追加的形式向文件中写入数据
# fobj1 = open('./b.txt', 'a', encoding='utf-8')
# fobj1.write('低头思故乡\n')

# 以二进制的形式向文件中追加
# fobj2 = open('./b.txt','ab')
# fobj2.write('静夜思1\n'.encode('utf-8'))
# fobj2.write('唐-李白\n'.encode('utf-8'))

# 一首完整的静夜思
file = open('./c.txt', 'w', encoding='utf-8')
file.write('静夜思\n')
file.write('唐-李白\n')
file.write('床前明月光\n')
file.write('疑似地上霜\n')
file.write('举头望明月\n')
file.write('低头思故乡\n')
file.close()

print('------------------读文件------------------')
'''
readlines()按行读取，一次性读取所有内容，返回一个列表，
每一行内容作为一个元素
'''
f1 = open('./c.txt', 'r', encoding='utf-8')  # 以字符串的形式读取
# f2 = open('./c.txt', 'rb')  # 二进制的方式读取数据
# # print(f.read(20))
# content = f.read()
# print(content.decode('utf-8'))  # 二进制解码
# f2.close()

print('-------------with语句--------------')
'''
上下文管理对象  with
自动释放打开关联对象,
'''
# 用with关键字读取数据
with open('./c.txt', 'r', encoding='utf-8') as f:
    print(f.read())
# 用with关键字写入数据
with open('./c.txt', 'a', encoding='utf-8') as f:
    f.write('用with关键字进行写操作')
    pass


print('-----------------小结-------------------')
'''
读操作read  r  r+  rb  rb+
r，r+只读，使用普通读取场景
rb  rb+ 适用于文件  图片 视频 音频的读取
-----------------------------------------------------
写操作 write   w  w+ wb+ wb a ab
w、wb+、w+ 每次都会创建文件
二进制读写，要注意编码问题，默认为gbk,
a、ab、a+ 在原有的基础上追加【文件指针的末尾追加】，不会每次创建一个新文件  
'''