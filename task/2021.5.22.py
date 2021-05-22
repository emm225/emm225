# 开发时间:2021/5/22 0:34
print('本程序将对输入的整数进行绝对值输出')
b=0
while b==0:
    a = int(input('请输入一个整数:'))
    print('输入的数为', a)
    if a>=0:
        print('绝对值为',a)
    else:
        print('绝对值为',(-a))
    judge=input('是否要再一次执行程序(y/n)')
    c=0
    while c==0:
        if judge=='y':
            b=0
            c=1
        elif judge=='n':
            b=1
            c=1
        else:
            judge=input('你的操作为非法操作，请重新输入是否再一次执行程序(y/n)')
            c=0   
