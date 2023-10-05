import pandas as pd

users = pd.read_csv('https://raw.githubusercontent.com/justmarkham/DAT8/master/data/u.user', delimiter='|')

# Discover what is the mean age per occupation
ageAvg = users.groupby('occupation')['age'].mean()
print('Mean age per occupation is:')
print(ageAvg)
# Discover the Male ratio per occupation and sort it from the most to the least
users['gender'] = users['gender'].map({'M': 1, 'F': 0})
maleRatio = users.groupby('occupation')['gender'].mean()
maleRatioSorted = maleRatio.sort_values(ascending=False)
print('\nSorted male ration per occupation:')
print(maleRatioSorted)
users['gender'] = users['gender'].map({1: 'M', 0: 'F'})  # return gender to default
# For each occupation, calculate the minimum and maximum ages
ageMaxMin = users.groupby('occupation')['age'].agg(['max', 'min'])
print('\nMin and Max age per occupation:')
print(ageMaxMin)
# For each combination of occupation and gender, calculate the mean age
occGender = users.groupby(['occupation', 'gender'])['age'].mean()
print('\nMean age for occupation and gender:')
print(occGender)
#  For each occupation present the percentage of women and men
genderPercentage = users.groupby('occupation')['gender'].value_counts(normalize=True).unstack() * 100
print('\nPercentage of women and men per occupation:')
print(genderPercentage)
