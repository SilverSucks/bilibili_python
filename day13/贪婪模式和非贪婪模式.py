'''
python里数量词默认是贪婪的，总是尝试匹配尽可能多的字符，
非贪婪则相反，总是尝试匹配尽可能少的字符
在* ? + {m,n}后面加上？，使贪婪变成非贪婪
'''
import re
res1 = re.match('.*\d', 'aasdf1234567890')
print(res1.group())
res2 = re.match('.*?\d', 'aasdf1234567890')
print(res2.group())