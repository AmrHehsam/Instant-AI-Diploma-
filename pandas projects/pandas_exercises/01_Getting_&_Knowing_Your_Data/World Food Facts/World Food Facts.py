import pandas as pd
# assign the data set to a dataframe named food
link = "E:\AI Diploma\Instant AI Diploma\en.openfoodfacts.org.products.tsv"
food = pd.read_csv(link, sep='\t', low_memory=False)
# get top 5 entries
print("Top 5 entries\n", food.head(5))
# number of observations in the dataset
print('\nNumber of observations in the dataset =', food.shape[0])
# number of columns in the dataset
print('\nNumber of columns in the dataset =', food.shape[1])
# print the name of all columns in the dataset
print('\nColumns names:')
for col in food.columns:
    print(col)
# get the name of the 105th column
print('\n105th column is:', food.columns[104])
# what are the observations of the 105th column
print('\nObservations of the 105th column:')
print(food.iloc[:, 104])
# how is the dataset indexed
print('\nDataset index:', food.index)
# what is the product name of the 19th observation
print("\nProduct name of the 19th observation is:")
print(food.loc[18, "product_name"])


