dic_products = {'rice': 6.34, 'bean': 2.23, 'soda': 3.12, 'beef':6.2,'juice':1.3}

print('Welcome to the store')
print(f'Here are the products and their prices: {dic_products}')

count = 0
total = 0

while True:
    product_ask = input('What product do you want?: ').lower()
    
    if product_ask in dic_products:
        count += 1
        total += dic_products[product_ask]  # soma sempre

        ask_new = input('Do you want to add another product?(S/N): ').upper()
        if ask_new == 'S':
            continue
        else:
            break  # sai do loop
    else:
        print('Sorry, the product is not available')
        continue

print(f'\nNumber of products: {count}')
print(f'Total price of the products: ${total:.2f}')