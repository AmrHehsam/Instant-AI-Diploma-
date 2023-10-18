import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/guipsamora/pandas_exercises/'
                 'master/04_Apply/Students_Alcohol_Consumption/student-mat.csv')

# For the purpose of this exercise slice the dataframe from 'school' until the 'guardian' column
df = df.loc[:, 'school':'guardian']

# Create a lambda function that will capitalize strings.
capitalize_string = lambda x: x.capitalize()

# Capitalize both Mjob and Fjob
df['Mjob'].apply(capitalize_string)
df['Fjob'].apply(capitalize_string)

# Print the last elements of the data set.
print(df.tail())

# Did you notice the original dataframe is still lowercase? Why is that? Fix it and capitalize Mjob and Fjob.
df['Mjob'] = df['Mjob'].apply(capitalize_string)
df['Fjob'] = df['Fjob'].apply(capitalize_string)


# Create a function called majority that returns a boolean value to a new column called legal_drinker
# (Consider majority as older than 17 years old)
def majority(age):
    return age > 17

df['legal_drinker'] = df['age'].apply(majority)

# Multiply every number of the dataset by 10.
is_numeric = df.select_dtypes(include=['int64', 'float64'])
df[is_numeric.columns] = is_numeric * 10

print(df.tail())

