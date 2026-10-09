weight=float(input('你的体重为：'))
height=float(input('你的身高为:'))
bmi=weight/height**2
if bmi < 18.5:
    print('偏瘦')
elif bmi >= 18.5 and bmi < 24:
    print('正常')
elif bmi >= 24 and bmi <= 28:
    print('超重')
else:
    print('肥胖')