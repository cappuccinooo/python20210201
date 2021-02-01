a=int(input('輸入分數'))
if a>100:
    print('輸入錯誤')
elif a<0:
    print('輸入錯誤')
elif a>89:
    print('A級!')
elif a>79:
    print('B級!')
elif a>69:
    print('C級!')
elif a>59:
    print('D級!')
else:
    print('E級!')
    