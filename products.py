# 讀取檔案
# .strip() 把尾巴換行去掉
# .split(',') 用逗點切割 切割完的結果為清單
products = []
with open('products.csv', 'r', encoding = 'utf-8') as f:
	for line in f:
		if 'product,price' in line:
			continue  #只能寫在迴圈裡 跳到下一迴
		name, price = line.strip().split(',')
		print(name, price)
		products.append([name, price])
print(products)

while True:
    name = input('請輸入商品名稱: ')
    if name == 'q':
        break
    price = input('請輸入商品價格: ')
    price = int(price)
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

with open('products.txt', 'w', encoding = 'utf-8') as f: #我只需要用 f 來稱呼這個檔案
	f.write('product,price\n')
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + '\n') # 加起來會成為同一字串

with open('products.csv', 'w',  encoding = 'utf-8') as f: #我只需要用 f 來稱呼這個檔案
	f.write('product,price\n')
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + '\n') 
		# 加起來會成為同一字串
		# CSV 檔可以用逗點區隔成不同儲存格
		# 有 open 就要有 close 關上檔案 
		# 加上 with 代表自動帶入 close 功能
		# str() 將整數轉字串