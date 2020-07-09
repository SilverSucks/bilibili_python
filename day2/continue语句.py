'''
continue 结束本次循环，继续进行下次循环
当continue提交满足时，本次循环剩下的语句不再执行，后面的循环继续。

continue和break这两个关键字只能用在循环中(while 和 for )
'''

# 1~100进行累加，如果累加和大于1500就退出循环
# sum = 0
# for item in range(1, 101):
#     sum += item
#     if sum > 1500:
#         print('循环执行到%d，满足条件退出'%item)
#         break  # 满足
#         pass
# print('此时的和为{}'.format(sum))


# 案例：continue的使用，输出1~100之间的偶数
print('------------continue的使用,输出1~100之间的偶数如下---------------------')
for item in range(1,101):
    if item%2 != 0:
        continue
        pass
    else:
        print('%d'%item, end=' ')