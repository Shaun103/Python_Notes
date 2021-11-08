import pandas as pd

people = {
    "first_name": ['Corety', 'Jane', 'John'],
    "last_name": ['Schafer', 'Doe', 'Doe'],
    "email": ['CoreyMSchafer@email.com', 'JaneDoe@gmail.com', 'JohnDoe@email.com']
}

df = pd.DataFrame(people)

print(df['email'])

print(df.set_index('email'))

print(df.set_index('email', inplace=True)) # Mutates the datafame using useing labels - 'email' 

print(df.index)

print(df.loc['CoreyMSchafer@email.com', 'last'])

print(df.iloc[0])

df.reset_index(inplace=True)  # delete index

# ___________________________________________________________________


df = pd.read_csv('survey_results_public.csv', index_col='Respondent')  # order by ether
df_schema = pd.read_csv('survey_results_schema.csv', index_col='Column') # order by Column

pd.set_option('display.max_columns', 85)
pd.set_option('display.max_rows', 85)

print(df)
print(df_schema)

print(df_schema.loc['Hobbyist']) # locates by column 
print(df_schema.loc['JobSat'])  # prints column for jobsat
print(df_schema.loc['JobSat', 'QuestionText'])  # prints just the text

print(df_schema.sort_index())   # sorts by indexed 'Column'

print(df_schema.sort_index(ascending=False)) # reverse sorting 

df_schema.sort_index(ascending=False,inplace=True)  # mutates dataframe sort

print(df_schema)