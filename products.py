products = []
while True:
    name = input('請輸入商品名稱: ')
    if name == 'q':
        break
    price = input('請輸入商品價格: ')
    # p = []
    # p.append(name)
    # p.append(price)
    # products.append(p)
    products.append([name, price]) # 直接 = 上面四行
print(products)
print(products[0][0])

for p in products:
	print(p)
	print(p[0], '的價格是', p[1])