import pandas as pd

data_dict={'Id':["001","002","003","004","003","005"],'Order':["Buy","Sell","Buy","Buy","Buy","Sell"],'Type':["Add","Add","Add","Add","Remove","Add"],
              'Price':[20.0,25.0,23.0,23.0,23.0,28.0],'Quantity':[100, 200, 50,70,50,100]}


df=pd.DataFrame(data_dict)


Bought_orders= {}
Sold_orders= {}


for index, row in df.iterrows():
    Total_price = row['Price'] * row['Quantity']
    if row['Order']=="Buy":
        Bought_orders[f'Order {index+1}'] = Total_price

    else:
        Sold_orders[f'Order {index+1}'] = Total_price



print(f"Bought orders: {Bought_orders}")
print(f"Best bought price {max(Bought_orders, key=Bought_orders.get)}")
print(f"Sold orders:{Sold_orders}")
print(f"Best sold price {max(Sold_orders, key=Sold_orders.get)}")

