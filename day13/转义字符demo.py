import re
path = 'D:\视频资料\哔哩哔哩求知讲堂python+人工智能\13-正则Day\课件'
print(path)
path2 = 'D:\\视频资料\\哔哩哔哩求知讲堂python+人工智能\\13-正则Day\\课件'
print(path2)

# 利用正则表达式来匹配路径, 对于每个反斜线都要转义
print(re.match('c:\\\\a.txt', 'c:\\a.txt').group())
# 在正则前面加 r ,表示使用原生的字符串,python字符串就不进行转义了
print(re.match(r'c:\\a.txt', 'c:\\a.txt').group())