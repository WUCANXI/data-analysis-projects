price=float(input('该商品的价格为：'))
if price>=1000:
    print('太贵了，买不起')
elif price>=800:
    print('我是穷孩子，买不起奢饰品')
elif price>=500:
    print('虽然也很贵，但是咬咬牙拿下了')
else:
    print('随便的买')