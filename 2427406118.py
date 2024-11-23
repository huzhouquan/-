num = int(input('请输入一个3位整数：'))
one = num % 10
two = num % 100 //10
three = num // 100
sum = one + two + three
print('三位数字之和是{0:4d}'.format(sum))