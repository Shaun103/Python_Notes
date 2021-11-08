import pandas as pd

people = {
    "first": ['Corety', 'Jane', 'John'],
    "last": ['Schafer', 'Doe', 'Doe'],
    "email": ['CoreyMSchafer@email.com', 'JaneDoe@gmail.com', 'JohnDoe@email.com']
}

df = pd.DataFrame(people)

print(df)

print(df['last'] == 'Doe') # grabs the columns where last name is 'Doe'

filt = (df['last'] == 'Doe')  

print(df.loc[filt]) # grabs the columns where last name is 'Doe'

#_________________________________________
# Differnt ways to filter

filt = (df['last'] == 'Doe') 

print(df.loc[filt])

print(df[(df['last'] == 'Doe')])

#_________________________________________
# Grabing columns while filtering

filt = (df['last'] == 'Doe') 

print(df.loc[filt, 'email']) # Grabs email Column 

filt2 = (df['last'] == 'Doe') & (df['first'] == 'John')   # & opperator  # Grabs only last name Doe and first name John
print(df.loc[filt2, 'email'])

filt2 = (df['last'] == 'Schafer') | (df['first'] == 'John') # | opperator Grabs only last name Doe OR first name John
print(df.loc[filt2, 'email'])

# _________________________________________
# Everything that DOES NOT match ~ Tilde key

print(df.loc[~filt2, 'email'])  

#_________________________________________

# Working with large Data Sets

df = pd.read_csv('survey_results_public.csv', index_col='Respondent')  # order by ether
df_schema = pd.read_csv('survey_results_schema.csv', index_col='Column') # order by Column

pd.set_option('display.max_columns', 15)
pd.set_option('display.max_rows', 15)

# ConvertedCOMP = Salaray Column 
high_salary = (df['ConvertedComp'] > 70000) # displays all salaries higher than 70\000

print(df.loc[high_salary]) # returns all conditions that ConvertedComp is over 70000

# LanguageWorkedWith - programming language worked with
print(df.loc[high_salary, ['Country', 'LanguageWorkedWith', 'ConvertedComp']]) # Grabs specified columns 

# _________________________________________
# Filters throguh a list 

countries = ['United States', 'India', 'United Kingdom', 'Germany', 'Canda']
filt = df['Country'].isin(countries)

print(df.loc[filt, 'Country'])

# # _________________________________________
# # Filtering through strings

filt = df['LanguageWorkedWith'].str.contains('Python', na=False)  #  nan values fill value

print(df.loc[filt, 'LanguageWorkedWith'])