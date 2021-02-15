import os # operating system 給程式權限

# .strip() 把尾巴換行去掉
# .split(',') 用逗點切割 切割完的結果為清單
# 把各區程式碼重構 function 並設置參數 (投幣孔) 把從外面拿的資料設成參數
# 有改變東西就 return 回傳
# function 的中心思想是只做一件事情，所以 refactor(重構程式)就是不斷改寫程式碼 
# 讓 function 盡量只做一件事

# 讀取檔案
def read_file(filename):
    products = []
    with open(filename, 'r', encoding = 'utf-8') as f:
        for line in f:
            if 'product,price' in line:
                continue  #只能寫在迴圈裡 跳到下一迴
            name, price = line.strip().split(',')
            print(name, price)
            products.append([name, price])
    return products # 有 return, function 的執行結果就可以存下來開

# 讓使用者輸入
def use_input(products):
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
    return products

# 印出所有購買紀錄
def print_product(products):
    for p in products:
        print(p)
        print(p[0], '的價格是', p[1])

# 寫入檔案
def write_file(filename_txt, filename_csv, products):
    with open(filename_txt, 'w', encoding = 'utf-8') as f: #我只需要用 f 來稱呼這個檔案
        f.write('product,price\n')
        for p in products:
            f.write(p[0] + ',' + str(p[1]) + '\n') # 加起來會成為同一字串

    with open(filename_csv, 'w',  encoding = 'utf-8') as f: #我只需要用 f 來稱呼這個檔案
        f.write('product,price\n')
        for p in products:
            f.write(p[0] + ',' + str(p[1]) + '\n') 
        # 加起來會成為同一字串
        # CSV 檔可以用逗點區隔成不同儲存格
        # 有 open 就要有 close 關上檔案 
        # 加上 with 代表自動帶入 close 功能
        # str() 將整數轉字串

# 主要功能 (主要執行程式碼)
def main():
    filename = 'products.csv'
    if os.path.isfile(filename): # 在程式同資料夾內尋找 檢查檔案在不在
        print('file got it!')
        products = read_file(filename)      
        print(products)
    else:
        print('FILE NOT FOUND ERROR')
    
    products = use_input(products)
    print_product(products)
    write_file('products.txt', 'products.csv', products)

if __name__ == '__main__':
	main()


