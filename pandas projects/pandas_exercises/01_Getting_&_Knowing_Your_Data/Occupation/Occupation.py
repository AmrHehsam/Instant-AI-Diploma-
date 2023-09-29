import pandas as pd
# assign dataset to a variable called and use user_id as index
users = pd.read_csv('https://raw.githubusercontent.com/justmarkham/DAT8/master/data/u.user', sep='|', index_col='user_id')
print('First 25 entries:\n', users.head(25))  # get first 25 entries
print('\nLast 10 entries:\n', users.tail(10))  # get last 10 entries
print('\nNumber of observations in the dataset =', users.shape[0])  # number of observations
print('\nNumber of columns in the dataset =', users.shape[1])  # number of columns
#  print columns names
print('\nColumns names are:')
for col in users.columns:
    print(col)
print('\nIndex of dataset:\n', users.index)  # dataset's index
# get datatype of each column
print('\ndatatype of each column:')
for col in users.columns:
    print(col, type(col))
# print occupation column only
print('\nOccupation column:\n', users['occupation'])
# How many different occupations in the dataset
print('\nDifferent occupations:', len(users['occupation'].unique()))
# most frequent occupation
maxOccupation = users['occupation'].value_counts().idxmax()
print('\nMost frequent occupation is:', maxOccupation)
# summarize dataframe
print('\nSummarize dataframe:\n', users.describe(include='all'))
# summarize all columns
print('\nSummarize all columns:')
print(users.info())
# describe occupation column only
print('\nSummarize occupation column:')
print(users['occupation'].info())
# what is the mean age
print('\nAverage age:', users['age'].mean())
# least occurred age
minAge = users.groupby('age')['age'].sum()
print('\nLeast occurred age is:', minAge.idxmin())
