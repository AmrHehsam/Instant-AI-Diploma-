import pandas as pd

# Import the dataset from this [address](https://raw.githubusercontent.com/justmarkham/DAT8/master/data/drinks.csv).
# Assign it to a variable called drinks.
drinks = pd.read_csv('https://raw.githubusercontent.com/justmarkham/DAT8/master/data/drinks.csv')
# Which continent drinks more beer on average?
beerAvg = drinks.groupby('continent')['beer_servings'].mean()
maxContinent = beerAvg.idxmax()
print('Continent which drinks most beer on average is:', maxContinent)
# For each continent print the statistics for wine consumption.
wineConsumption = drinks.groupby('continent')['wine_servings'].describe()
print('\nStatistics for wine consumption in each continent:')
print(wineConsumption)
# Print the mean alcohol consumption per continent for every column
meanAlcohol = drinks.iloc[:, 1:].groupby('continent').mean()
for col in meanAlcohol.columns:
    print(f"\nMean {col} consumption per continent:")
    print(meanAlcohol[col])
# Print the median alcohol consumption per continent for every column
medianAlcohol = drinks.iloc[:, 1:].groupby('continent').median()
for col in medianAlcohol.columns:
    print(f"\nMedian {col} consumption per continent:")
    print(medianAlcohol[col])
# Print the mean, min and max values for spirit consumption.
spiritStats = drinks.iloc[:, 1:]['spirit_servings'].agg(['mean', 'min', 'max']).to_frame().T
spiritStats.columns = ['Mean', 'Min', 'max']
print(spiritStats)
