import pandas as pd
df=pd.read_csv('Products.csv')
print(df.to_string(index=False))
total_rows=len(df)
print("Total number of rows=",total_rows)
above_500=df[df['price']>500]
print("Products with Price above 500=",len(above_500))
average_price =df['price'].mean()
print("average price=",average_price)
catagory=input("Enter the category to filter products=")
filtered_products=df[df['category'].str.lower()==catagory.lower()]
print("Products in category{catagory}:")
if filtered_products.empty:
    print("No products found in this category.")
else:
    print(filtered_products)
total_quantity=df['quantity'].sum()
print("Total quantity of all products=",total_quantity)       

