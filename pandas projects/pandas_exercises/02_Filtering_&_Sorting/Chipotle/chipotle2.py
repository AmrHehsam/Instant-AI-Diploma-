import pandas as pd

# assign dataset to a dataframe called chipo
chipo = pd.read_csv('https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv', delimiter='\t')
# how many products cost more than $10.00
# change datatype from string to float first
chipo['item_price'] = chipo['item_price'].replace('[\$,]', '', regex=True).astype(float)
greaterThan10 = chipo[chipo['item_price'] > 10]
print('Products that cost more than $10.00 =', greaterThan10.shape[0])
# price of each item
itemPrice = chipo[['item_name', 'item_price']].reset_index(drop=True)
print('\nPrice of all items:\n')
print(itemPrice)
# sort by name of item
sortedByName = chipo.sort_values(by='item_name')
print('\nItems sorted by name:')
print(sortedByName)
# What was the quantity of the most expensive item ordered?
maxPrice = chipo.loc[chipo['item_price'].idxmax()]
print('\nQuantity of most expensive item ordered =', maxPrice['quantity'])
# How many times was a Veggie Salad Bowl ordered
veggie = chipo[chipo['item_name'] == 'Veggie Salad Bowl']
totalVeggieOrdered = veggie['quantity'].sum()
print('\nVeggie Salad was ordered', totalVeggieOrdered, 'times')
# How many times did someone order more than one Canned Soda?
soda = chipo[(chipo['item_name'] == 'Canned Soda') & (chipo['quantity'] > 1)]
quantSum = soda.shape[0]
print('\nNumber of times more than one canned soda was ordered', quantSum, 'times')

