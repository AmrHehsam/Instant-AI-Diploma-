import pandas as pd

# Create an example dataframe about a fictional army
raw_data = {'regiment': ['Nighthawks', 'Nighthawks', 'Nighthawks', 'Nighthawks', 'Dragoons', 'Dragoons',
                         'Dragoons', 'Dragoons', 'Scouts', 'Scouts', 'Scouts', 'Scouts'],
            'company': ['1st', '1st', '2nd', '2nd', '1st', '1st', '2nd', '2nd','1st', '1st', '2nd', '2nd'],
            'deaths': [523, 52, 25, 616, 43, 234, 523, 62, 62, 73, 37, 35],
            'battles': [5, 42, 2, 2, 4, 7, 8, 3, 4, 7, 8, 9],
            'size': [1045, 957, 1099, 1400, 1592, 1006, 987, 849, 973, 1005, 1099, 1523],
            'veterans': [1, 5, 62, 26, 73, 37, 949, 48, 48, 435, 63, 345],
            'readiness': [1, 2, 3, 3, 2, 1, 2, 3, 2, 1, 2, 3],
            'armored': [1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1],
            'deserters': [4, 24, 31, 2, 3, 4, 24, 31, 2, 3, 2, 3],
            'origin': ['Arizona', 'California', 'Texas', 'Florida', 'Maine', 'Iowa', 'Alaska', 'Washington',
                       'Oregon', 'Wyoming', 'Louisana', 'Georgia']}

# Create a dataframe and assign it to a variable called army.
army = pd.DataFrame(raw_data, columns=['regiment', 'company', 'deaths', 'battles', 'size', 'veterans', 'readiness',
                                       'armored', 'deserters', 'origin'])
# Set the 'origin' colum as the index of the dataframe
army.set_index('origin', inplace=True)
# Print only the column veterans
veterans = army['veterans']
print('\nVeterans column:')
print(veterans)
# Print the columns 'veterans' and 'deaths'
veteransAndDeaths = army[['veterans', 'deaths']]
print('\nVeterans and deaths columns:')
print(veteransAndDeaths)
# Print the name of all the columns
print('\nColumns names:')
for col in army.columns:
    print(col)
# Select the 'deaths', 'size' and 'deserters' columns from Maine and Alaska
selectedColumns = army.loc[['Maine', 'Alaska'], ['deaths', 'size', 'deserters']]
print('\nDeaths and size and deserters in Maine and Alaska:')
print(selectedColumns)
# Select the rows 3 to 7 and the columns 3 to 6
selectedCols = army.iloc[2:7, 2:6]
print('\nRows 3 to 7 and columns 3 to 6:')
print(selectedCols)
# Select every row after the fourth row and all columns
selected = army.iloc[4:, :]
print('\nRows after the fourth row and all columns:')
print(selected)
# Select every row up to the 4th row and all columns
sel = army.iloc[:4, :]
print('\nRows up to fourth row and all columns:')
print(sel)
# Select the 3rd column up to the 7th column
Sel = army.iloc[:, 2:7]
print('\n3rd column up to the 7th:')
print(Sel)
# Select rows where df.deaths is greater than 50
greaterThan50 = army[army['deaths'] > 50]
print('\nRows where deaths is greater than 50:')
print(greaterThan50)
# Select rows where df.deaths is greater than 500 or less than 50
lessOrGreater = army[(army['deaths'] > 500) | (army['deaths'] < 50)]
print('\nRows where deaths is greater than 500 or less than 50:')
print(lessOrGreater)
# Select all the regiments not named "Dragoons"
notDragoons = army[army['regiment'] != 'Dragoons']
print('\nRegiments not named Dragoons:')
print(notDragoons)
# Select the rows called Texas and Arizona
TexasAndArizona = army.loc[['Texas', 'Arizona']]
print('\nRows called Texas and Arizona:')
print(TexasAndArizona)
# Select the third cell in the row named Arizona
arizona = army.loc['Arizona'].iloc[2]
print('\nThird cell in Arizona:')
print(arizona)
# Select the third cell down in the column named deaths
deaths3 = army['deaths'].iloc[2]
print('\nThird cell in the column deaths:')
print(deaths3)
