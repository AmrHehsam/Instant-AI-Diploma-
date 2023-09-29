import pandas as pd

# get dataset and assign it ti a variable called chipo
chipo = pd.read_csv('https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv', delimiter='\t')
# get first 10 entries
print('first 10 entries:\n', chipo.head(10))
# get number of observations in 2 ways
rows = chipo.shape[0]
print('observations = ', rows)
rows2 = len(chipo)
print('observations = ', rows2)
# get number of columns
col = chipo.shape[1]
print('columns = ', col)
# print columns names
print('\ncolumns names:')
for cols in chipo.columns:
    print(cols)
# how is dataset indexed
print('\ndata index:', chipo.index)
# get most ordered item (then add the quantity)
itemCount = chipo.groupby('item_name')['quantity'].sum()
mostOrdered = itemCount.idxmax()
print('\nmost ordered item is ({}) with quantity = {}'.format(mostOrdered, itemCount[mostOrdered]))
# get most ordered item in choice description column
itemCount = chipo.groupby('choice_description')['quantity'].sum()
mostOrdered = itemCount.idxmax()
print('\nmost ordered item(choice description) is {} with quantity = {}'.format(mostOrdered, itemCount[mostOrdered]))
# get total items ordered
totalOrders = chipo['quantity'].sum()
print('\ntotal items that were ordered = ', totalOrders)
# check item_price type
print('\nprice datatype: ', chipo['item_price'].dtype)
# using lambda function to change datatype to float then check again
chipo['item_price'] = chipo['item_price'].apply(lambda x: float(x.replace('$', '')))
print('price datatype after change: ', chipo['item_price'].dtype)
# check the revenue for the period dataset
chipo['revenue'] = chipo['item_price'] * chipo['quantity']
totalRevenue = chipo['revenue'].sum()
print('\ntotal revenue = ', totalRevenue)
# get total number of orders made
ordersMade = chipo['order_id'].unique()
totOrders = len(ordersMade)
print('\nTotal orders made = ', totOrders)
# get average revenue per order(2 methods)
avgRevenue = chipo.groupby('order_id')['revenue'].sum().mean()
print('\naverage revenue per order (1st method) = ', avgRevenue)
avgRevenue2 = totalRevenue / totOrders  # both are above
print('average revenue per order (2nd method) = ', avgRevenue2)
# different items that were sold
itemsSold = chipo['item_name'].unique()
print('\ndifferent items that were sold = ', len(itemsSold))
