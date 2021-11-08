import pandas as pd
import numpy as np 

# Table of contents__________________________________________

    # Removing NA values 
    # removing rows with missing values
        # dropna() - 
    # Show unique values 
    # replacing unique values with other values 

# Table of contents__________________________________________


people = {
    "first": ['Corety', 'Jane', 'John', 'Chris', np.nan, None,'NA'],
    "last": ['Schafer', 'Doe', 'Doe', 'Schafer', np.nan, np.nan, 'Missing'],
    "email": ['CoreyMSchafer@email.com', 'JaneDoe@gmail.com', 'JohnDoe@email.com', None, np.nan, 'Anonymous@email.com', 'NA'],
    "age": ['33', '55', '63', '36', None, None, 'Missing']
}

df = pd.DataFrame(people)

#________________________________________
# Removing NA values 
df.replace('NA', np.nan, inplace=True)
df.replace('Missing', np.nan, inplace=True)


#________________________________________
# removing rows with missing values
# dropna() - 

print(df.dropna())
print(df.dropna(axis='index', how='any'))  # default arguments

print(df.dropna(axis='index', how='all'))   # all values have to be missing to be dropped

print(df.dropna(axis='columns', how='all')) # removes columns that have missing values

print(df.dropna(axis='columns', how='any'))   # removes all empty rows with missing data

print(df.dropna(axis='index', how='any', subset=['email']))   # displays atleast rows with at least email

print(df.dropna(axis='index', how='any', subset=['last', 'email'])) # displays at least last name or email 

print(df.isna())

#________________________________________
# Replace missing data

print(df.fillna(0)) # fill navalues with 0

print(df.dtypes)    # prints type

df['age']  = df['age'].astype(float)  # changes type to float
print(df['age'])

print(df.dtypes)

print(df.mean())

#####change all nan types#### print(df.astype())

#________________________________________

na_vals = ['NA', 'Missing']  # if values are missing, replace with

df = pd.read_csv('survey_results_public.csv', index_col='Respondent', na_values=na_vals)  # order by ether
df_schema = pd.read_csv('survey_results_schema.csv', index_col='Column') # order by Column

pd.set_option('display.max_columns', 85)
pd.set_option('display.max_rows', 85)

print(df)

print(df['YearsCode'].head(10))

print(df['YearsCode'].head(10).mean())

###ERROR#### df['YearsCode'] = df['YearsCode'].astype(float) ####ERROR less than one year, new string type

#______________________________________________________
# Show unique values 

print(df['YearsCode'].unique())

#______________________________________________________
# replacing unique values with other values 

df['YearsCode'].replace('Less than 1 year', 0, inplace=True)

df['YearsCode'].replace('More than 50 years', 51, inplace=True)


df['YearsCode'] = df['YearsCode'].astype(float) # Changes values to float

print(df['YearsCode'].unique())
print(df['YearsCode'].mean())
print(df['YearsCode'].median())