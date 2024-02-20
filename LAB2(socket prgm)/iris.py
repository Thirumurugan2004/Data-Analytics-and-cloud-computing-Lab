import pandas as pd

data = pd.read_csv("/home/auist/Downloads/iris_csv.csv")
print(data.head(),"\n")
print(data.sample(20),"\n")
print(data.columns,"\n")
print(data.shape,"\n")
print(data)

slice_data = data[5:10]
print(slice_data,"\n")

length = data["sepallength"]
print(length.head(6),"\n")

print(data.iloc[6],"\n")

