dic_products = {'rice': 6.34, 'bean': 2.23, 'soda': 3.12, 'beaf':6.2,'suice':1.3}

print('Welcome to the store')
print(f'Here it is the products and your value: {dic_products}')
count = 0
total = 0

while True:
 product_ask = input('What product do you want?:').lower()
 if product_ask in dic_products:
    count += 1
    total += dic_products[product_ask]
    ask_new = input('Do you want to add another product?(S/N):').upper()
    if ask_new == 'S':
      continue
    else:
      maxvalue = max(dic_products, key=dic_products.get)
      maxvalueindic = dic_products[maxvalue]
      minvalue = min(dic_products, key=dic_products.get)
      minvalueindic = dic_products[minvalue]
                              
      print(f'Number of the products: {count}')
      print(f'The total price of the products: {total}')
      print(f'The expensive product is {maxvalue}: {maxvalueindic}')
      print(f'The cheapest product is {minvalue}:{minvalueindic}')
 else:
    print('Sorry, the product is not avaliable')
    continue


   
      
      
