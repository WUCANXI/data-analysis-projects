name=input('你的名字是：')
age=int(input('你的年龄是：'))
print(f'我的名字是{name},我今年{age}岁了')
a=float(input('第一个数字是：'))
b=float(input('第二个数字是：'))
print(f'他们的和为：{a+b:.2f}\n他们的差为：{a-b:.2f}\n他们的积为：{a*b}\n他们的商为：{a/b}')
r=float(input('园的半径为：'))
pai=3.14159
print(f'该圆的周长为{2*pai*r:.2f}\n该圆的面积为{pai*r**2:.2f}')
a=int(input('输入一个三位数整数：'))
print(f'该整数的百分位为:{a//100}\n该整数的十分位为:{a//10%10}\n该整数的个位数为：{a%100%10}')
a=float(input('输入一个数字：'))
if a>0:
   print('该数为正数')
elif a<0:
   print('该数为负数')
else:
   print('这个数是0')
a=float(input('三角形第一条边长为：'))
b=float(input('三角形第二条边长为：'))
c=float(input('三角形第三条边长为：'))
if (a+b-c>0 or a+c-b>0 or b+c-a>0):
   print('能构成三角形')
   if (a==b==c):
       print('该三角形是等边三角形')
   elif (a**2+b**2==c**2 or a**2+c**2==b**2 or a**2+b**2==c**2):
       print('该三角形是直角三角形')
   else:
       print('该三角形是普通三角形')
else:
   print('不能构成三角形')
a=input('请输入你需要查询的字母：')
if 'A' <= a <= 'Z':
    print('该字母是大写字母')
elif 'a' <= a <= 'z':
    print('该字母是小写字母')
elif '0'<=a<='9':
    print('数字')
else:
    print('其他字符')
a=float(input('你总共行驶的公里数为：'))
if a<=3:
   print('您需要支付13元')
elif 3<=a<=10:
   print(f'您需要支付{(a-3)*2.3+13}元')
else:
   print(f'您需要支付{(a-3)*2.3+13+(a-10)*2.3*3/2}')
day=input('请问您是否是周末来看电影y/n：')
age=int(input('请问您的年龄是：'))
student=input('请问您是否是学生y/n：')
if day == 'y':
    price=60
else:
    price=40
if student == 'y' and age<=12:
     price=price*4/5/2
elif student == 'y' and age>12:
    price=price*4/5
elif student == 'n' and age<=12:
    price=price/2
else:
    price=price
print(price)
