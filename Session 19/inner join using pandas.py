import pandas as pd
name = {
    'ID': [1, 2, 3, 4, 5],
    'Name': ['Amr', 'Taha', 'Ahmed', 'Youssef', 'Loai']
}

age = {
    'ID': [2, 3, 4, 5, 6],
    'Age': [20, 22, 18, 17, 19]
}
df1 = pd.DataFrame(name)
print(df1)
df2 = pd.DataFrame(age)
print(df2)

innerJoin = pd.merge(df1, df2, on='ID', how='inner')
print(innerJoin)
