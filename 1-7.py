a=int(input('輸入數學成績'))
b=int(input('輸入英文成績'))
if a<60 and b <60:
    print('要處罰!')
elif a>90 and b>=90:
    print('有獎品!')
elif a<60 or b <60:
    print('再加油')
    