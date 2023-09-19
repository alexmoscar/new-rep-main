import pandas as pd
order = pd.read_csv('объединение таблиц/orders.csv', sep = ';')
prod = pd.read_csv('объединение таблиц/products.csv', sep = ';')
order_products = order.merge(prod, left_on = 'ID товара', right_on = 'Product_ID', how = 'left')
order_products['Profit'] = order_products['Price']*order_products['Количество']
ф = order_products[order_products['Оплачен'] == 'Да'].groupby('ID Покупателя')['Profit'].sum().sort_values(ascending=False)
print(ф)