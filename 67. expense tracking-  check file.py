# 確認檔案在不在 + 66 讀取檔案
import os

products = []
if os.path.isfile('64. products.csv'):
    print('找到檔案了')
    with open('64. products.csv', 'r', encoding='utf-8') as f:
        for line in f:
            if '商品名稱, 價格' in line:
                continue  # 繼續 (跳出此次，執行下一輪)
            name, price = line.strip().split(',')  # 移除首尾的字符（空格或换行符）
            products.append([name, price])
    print(products)

else:
    print('沒有找到檔案……')

# 使用者輸入資料
while True:
    name = input('請輸入商品名稱:')
    if name == 'q':
        break
    price = input('請輸入商品價格:')
    price = int(price)
    products.append([name, price])
print(products)

# 逐筆印出消費紀錄
for p in products:
    print(p)
    print(p[0], '的價格是', p[1])

# 將資料存成csv檔案
with open('64. products.csv', 'w', encoding='utf-8') as f:
    f.write('商品名稱,價格\n')
    for p in products:
        f.write(p[0] + ',' + str(p[1]) + '\n')
