import pandas as pd
data = {
    "product": ["Pen", "Pencil", "Book", "Eraser"],
    "price": [10, 5, 120, 3],
    "stock": [100, 200, 50, 500]
}
df=pd.DataFrame(data)
print(df)
print(df[df["price"]>10])
print(df[df["stock"]<100])
print(df.sort_values("price",ascending=False))
print(df[["product","price"]])
print(df.shape)