import pandas as pd

crime = pd.read_csv('https://raw.githubusercontent.com/guipsamora/pandas_exercises'
                    '/master/04_Apply/US_Crime_Rates/US_Crime_Rates_1960_2014.csv')

# What is the type of the columns?
print('The type of columns:')
print(crime.dtypes)

# Convert the type of the column Year to datetime64
crime['Year'] = pd.to_datetime(crime['Year'], format='%Y')
print('\nYear datatype after change:')
print(crime['Year'].dtypes)

# Set the Year column as the index of the dataframe
crime.set_index('Year', inplace=True)
print(crime.head())

# Delete the Total column
crime.drop('Total', axis=1, inplace=True)
print(crime.head())

# Group the year by decades and sum the values
crime_decade = crime.drop('Population', axis=1).resample('10Y').sum()
print(crime_decade.head())

# What is the most dangerous decade to live in the US?
most_dangerous = crime_decade.sum(axis=1).idxmax()
print('Most dangerous decade:', most_dangerous.date())
