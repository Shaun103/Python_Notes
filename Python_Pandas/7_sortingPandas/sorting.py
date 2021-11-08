import pandas as pd

people = {
    "first": ['Corety', 'Jane', 'John', 'Adam'],
    "last": ['Schafer', 'Doe', 'Doe', 'Doe'],
    "email": ['CoreyMSchafer@email.com', 'JaneDoe@gmail.com', 'JohnDoe@email.com', 'A@email.com']
}

df = pd.DataFrame(people)


print(df)

#_____________________________________________________
# sorting_values

print(df.sort_values(by='last'))

#_____________________________________________________
# sorting on multiple columns 

print(df.sort_values(by=['last', 'first'], ascending=False))

#_____________________________________________________

print(df.sort_values(by=['last', 'first'], ascending=[False, True]))


#_____________________________________________________
#Mutating on sort

print(df.sort_values(by=['last', 'first'], ascending=[False, True], inplace=True))

df.sort_index()

print(df)

#_____________________________________________________
# only see last name, sorting

df['last'].sort_values()

#_____________________________________________________ #

df = pd.read_csv('survey_results_public.csv', index_col='Respondent')  # order by ether
df_schema = pd.read_csv('survey_results_schema.csv', index_col='Column') # order by Column

pd.set_option('display.max_columns', 85)
pd.set_option('display.max_rows', 85)

print(df.head())

#_____________________________________________________
# Sorting Country in Ascending, Sorting ConvertedComp is Descending

df.sort_values(by=['Country', 'ConvertedComp'], ascending=[True, False], inplace=True)

print(df['Country'].head(50))

#_____________________________________________________
# Showing the first 50 from Country and ConvertedComp

print(df[['Country', 'ConvertedComp']].head(50))


#_____________________________________________________
# largest numbers in columns

print(df['ConvertedComp'].nlargest(10))

#_____________________________________________________
# Finding the largest in a column 

print(df.nlargest(10, 'ConvertedComp'))

#_____________________________________________________
# smallest number in column 

print(df.nsmallest(10, 'ConvertedComp'))