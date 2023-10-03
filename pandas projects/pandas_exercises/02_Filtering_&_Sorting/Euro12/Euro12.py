import pandas as pd

# Assign it to a variable called euro12
link = 'https://raw.githubusercontent.com/guipsamora/' \
       'pandas_exercises/master/02_Filtering_%26_Sorting/Euro12/Euro_2012_stats_TEAM.csv'
euro12 = pd.read_csv(link)
# Select only the Goal column
goals = euro12['Goals']
print('Goals column:')
print(goals)
# How many team participated in the Euro2012?
numOfTeams = euro12.shape[0]  # number of observations
print('\nTeams participated in Euro2012 =', numOfTeams)
# What is the number of columns in the dataset?
print('\nNumber of columns in the dataset =', euro12.shape[1])
# View only the columns Team, Yellow Cards and Red Cards and assign them to a dataframe called discipline
discipline = euro12[['Team', 'Yellow Cards', 'Red Cards']]
print('\n')
print(discipline)
# Sort the teams by Red Cards, then to Yellow Cards
sortedByYCRC = euro12.sort_values(by=['Red Cards', 'Yellow Cards'], ascending=[False, False])
print('\nSorted By Red cards, then Yellow Cards')
print(sortedByYCRC)
# Calculate the mean Yellow Cards given per Team
YCMean = euro12['Yellow Cards'].mean()
print('\nYellow Cards Average =', YCMean)
# Filter teams that scored more than 6 goals
moreThan6Goals = euro12[euro12['Goals'] > 6]
print('\nteams scored more than 6 goals:')
print(moreThan6Goals)
# Select the teams that start with G
teamsStartingWithG = euro12[euro12['Team'].str.startswith('G')]
print('\nTeams that start with G:')
print(teamsStartingWithG)
# Select the first 7 columns
print('\nFirst 7 teams')
print(euro12.head(7))
# Select all columns except the last 3
exceptLast3Cols = euro12.iloc[:, :-3]
# Present only the Shooting Accuracy from England, Italy and Russia

EIR = euro12[euro12['Team'].isin(['England', 'Italy', 'Russia'])][['Team', 'Shooting Accuracy']]
print('\nShooting Accuracy from England, Italy and Russia:')
print(EIR)
