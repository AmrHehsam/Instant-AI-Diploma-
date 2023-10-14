import pandas as pd

raw_data = {'regiment': ['Nighthawks', 'Nighthawks', 'Nighthawks', 'Nighthawks', 'Dragoons', 'Dragoons', 'Dragoons', 'Dragoons', 'Scouts', 'Scouts', 'Scouts', 'Scouts'],
        'company': ['1st', '1st', '2nd', '2nd', '1st', '1st', '2nd', '2nd','1st', '1st', '2nd', '2nd'],
        'name': ['Miller', 'Jacobson', 'Ali', 'Milner', 'Cooze', 'Jacon', 'Ryaner', 'Sone', 'Sloan', 'Piger', 'Riani', 'Ali'],
        'preTestScore': [4, 24, 31, 2, 3, 4, 24, 31, 2, 3, 2, 3],
        'postTestScore': [25, 94, 57, 62, 70, 25, 94, 57, 62, 70, 62, 70]}

regiment = pd.DataFrame(raw_data)
# What is the mean preTestScore from the regiment Nighthawks?
nighthawks_mean_preTestScore = regiment[regiment['regiment'] == 'Nighthawks']['preTestScore'].mean()
print('The mean preTestScore from the regiment Nighthawks:', nighthawks_mean_preTestScore)
# Present general statistics by company
company_statistics = regiment.groupby('company').describe()
print('\ngeneral statistics by company:')
print(company_statistics)
# What is the mean of each company's preTestScore?
company_mean_preTestScore = regiment.groupby('company')['preTestScore'].mean()
print('\nThe mean of each company preTestScore:')
print(company_mean_preTestScore)
# Present the mean preTestScores grouped by regiment and company
company_regiment_mean_preTestScore = regiment.groupby(['company', 'regiment'])['preTestScore'].mean()
print('\nThe mean preTestScores grouped by regiment and company:')
print(company_regiment_mean_preTestScore)
# Present the mean preTestScores grouped by regiment and company without hierarchical indexing
mean_preTestScores = regiment.groupby(['regiment', 'company'])['preTestScore'].mean().reset_index()
print('\nThe mean preTestScores grouped by regiment and company without hierarchical indexing:')
print(mean_preTestScores)
# Group the entire dataframe by regiment and company
regiment_company = regiment.groupby(['regiment', 'company']).apply(lambda x: x.reset_index(drop=True)).reset_index(drop=True)
print('\nDataframe grouped by regiment and company:')
print(regiment_company)
# What is the number of observations in each regiment and company
regiment_company_observations = regiment.groupby(['regiment', 'company']).size()
print('\nThe number of observations in each regiment and company')
print(regiment_company_observations)
# Iterate over a group and print the name and the whole data from the regiment
for name, group_data in regiment.groupby('regiment'):
    print(f'\nRegiment: {name}')
    print(group_data)
