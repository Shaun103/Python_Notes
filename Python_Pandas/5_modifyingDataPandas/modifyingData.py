import pandas as pd


people = {
    "first_name": ['Corey', 'Jane', 'John'],
    "last_name": ['Schafer', 'Doe', 'Doe'],
    "email": ['CoreyMSchafer@email.com', 'JaneDoe@gmail.com', 'JohnDoe@email.com']
}

df = pd.DataFrame(people)

print(df)

print(df.columns)

df.columns = ['first_name', 'last_name', 'email']

print(df)

# _____________________________________________________
# comment out line 68

# df.columns = [x.upper() for x in df.columns] # uppercase the columns name
# print(df)

# # _____________________________________________________
# comment out line 78

# df.columns = df.columns.str.replace('', '_') # seperates by underscore
# df.columns = df.columns.str.replace('_', ' ') # seperates by space
# print(df)

# _____________________________________________________
# Renaming columns 

df.rename(columns={'first_name': 'first', 'last_name': 'last'}, inplace=True) # renaming columns, mutating columns
print(df)

# _____________________________________________________

print(df.loc[2]) # grabing the second row 

df.loc[2] = ['John', 'Smith', 'JohnSmith@email.com']    # changing entire row 
print(df)

df.loc[2, ['last_name', 'email']] = ['Doe', 'JohnDoe@email.com'] # changing specific parts of data 
print(df)


# _____________________________________________________

df.loc[2, 'last_name'] = 'Smith'
print(df)

df.at[2, 'last_name'] = 'Doe'   # .at method does similar  
print(df)

filt = (df['email'] == 'JohnDoe@email.com')
print(df[filt])
df[filt]['last_name'] = 'Smith'  # use .loc or .at methods to change data 

filt = (df['email'] == 'JohnDoe@email.com')
df.loc[filt, 'last_name'] = 'Smith'
print(df)

# _____________________________________________________

print(df)

print(df['email'].str.lower())

df['email'] = df['email'].str.lower()  # lowercasing displayed email

print(df)

# _____________________________________________________
# apply - calling a function on a value (cannot work on a dataframe or series object)

print(df['email'].apply(len))

def update_email(email):
    return email.upper()

print(df['email'].apply(update_email))

df['email'] = df['email'].apply(update_email)

print(df)

# _____________________________________________________
# using lambda functions

df['email'] = df['email'].apply(lambda x: x.lower())

print(df)

# _____________________________________________________

print(df['email'].apply(len))
print(df.apply(len)) # number of rows in each column 
print(df.apply(len, axis='columns')) # number of rows in each column 
print(len(df['email'])) # number of rows in each column

# print(df.apply(pd.Series.min))

# print(df.apply(lambda x: x.min()))

# _____________________________________________________
# applyMap

# print(df.applymap(len))
# print(df.applymap(str.lower))

# _____________________________________________________
# Map method 

print(df)
print(df['first'].map({'Corey': 'Chris', 'Jane': 'Mary'})) 

# _____________________________________________________
# Replace method

print(df['first'].replace({'Corey': 'Chris', 'Jane': 'Mary'})) 

df['first'] = (df['first'].replace({'Corey': 'Chris', 'Jane': 'Mary'})) # Mutating changes
print(df)

# _____________________________________________________

df = pd.read_csv('survey_results_public.csv', index_col='Respondent')  # order by ether
df_schema = pd.read_csv('survey_results_schema.csv', index_col='Column') # order by Column


pd.set_option('display.max_columns', 85)
pd.set_option('display.max_rows', 85)

# ConvertedComp = salary 
df.rename(columns={'ConvertedComp': 'SalaryUSD'}, inplace=True)
print(df['SalaryUSD'])

# _____________________________________________________

print(df['Hobbyist'])
print(df['Hobbyist'].map({'Yes': True, 'No': False}))
