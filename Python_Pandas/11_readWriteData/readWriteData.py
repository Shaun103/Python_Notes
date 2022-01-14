import pandas as pd 

df = pd.read_csv('survey_results_public.csv', index_col='Respondent')
df_schema = pd.read_csv('survey_results_schema.csv', index_col='Column')

pd.set_option('display.max_columns', 15)
pd.set_option('display.max_rows', 15)

print(df.head())

# _______________________________________________

filt = (df['Country'] == 'India')

india_df = df.loc[filt]

print(india_df.head())

# _______________________________________________
# creating csv file

india_df.to_csv('data/modified.csv')   

# _______________________________________________
# creating a tsv file from data

india_df.to_csv('data/modified.tsv', sep='\t') # seperate by tabs

# _______________________________________________
# creating a excel file from data

india_df.to_excel('data/modified.xlsx')

test = pd.read_excel('data/modified.xlsx', index_col='Respondent')

print(test.head())

# _______________________________________________
# Writing to json file 

india_df.to_json('data/modified.json')

# list like json file 

india_df.to_json('data/modified.json', orient='records', lines=True) # each line on a new line

# reading data from json file

test = pd.read_json('data/modified.json', orient='records', lines=True)

print(test.head())

# _______________________________________________
# # reading from a database

# # Reasource 
# https://www.youtube.com/watch?v=N6hyN6BW6ao&list=PL-osiE80TeTsWmV9i9c58mdDCSskIFdDS&index=11