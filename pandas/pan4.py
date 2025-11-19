import pandas as pd
df=pd.read_csv(r"pandas\coffedata.csv")

print(df[df["coffee_name"]=="Latte"]["Monthsort"].value_counts())
print(df.shape)
print(df.columns.to_list())
print(df["coffee_name"].unique())
print(df[df.isnull().any(axis=1)])
print(df["Weekday"].isnull().sum())
print(df[df["Weekday"].isnull()])
print(df[df["Weekday"].isnull()])
print(df.dropna())