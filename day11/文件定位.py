'''
文件定位，指的是当前文件指针读取到的位置，光标位置。
在读写文件的过程中，如果想知道当前的位置，可以用tell()来获取
'''
# 以读模式打开test.txt文件
# f = open('a.txt', 'r', encoding='utf-8')
# content = f.read(3)   # 读取三个字符
# 查看当前游标所在位置
# cur = f.tell()
# print(cur)

# 如果指定了编码格式为utf-8，则每个汉字占用三个字节
# with open('a.txt', 'r', encoding='utf-8') as f:
#     print(f.read(2))
#     print(f.tell())

# print('---------------truncate()方法对源文件进行截取操作---------------------')
# fileObj = open('a.txt', 'r', encoding='utf-8')
# # print(fileObj.read())
# # fileObj.close()
# with open('a.txt', 'r', encoding='utf-8') as f:
#     print(fileObj.read())
#     pass
# fileObj.close()
# print('------------截取之后的数据-----------')
# fileObj2 = open('a.txt', 'r+', encoding='utf-8')
# fileObj2.truncate(9)
# print(fileObj2.read())
# fileObj2.close()

print('---------------seek()定位到文件的其他位置---------------')
f = open('a.txt', 'rb')
content = f.read(9)  # 读取三个字符
print('指针所在位置：',f.tell())
print('读取的内容是：', content.decode())
f.seek(-3, 1)   # 在当前位置往回偏移两个字节
print('指针所在的位置：', f.tell())
print('', f.read(6).decode())
'''
注意：对于用'r'这种模式打开文件这种情况，在文本文件中没有使用二进制的选项打开
文件，只允许从文件的开头计算相对位置，从文件尾部计算或者当前计算的话，会引发异常
'''



