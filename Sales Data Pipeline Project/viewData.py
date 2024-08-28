import pandas as pd

file_path = r"D:\Sales Data Pipeline Project\pizza_sales.csv"
df = pd.read_csv(file_path)

print(df.head())
print(df.dtypes)



