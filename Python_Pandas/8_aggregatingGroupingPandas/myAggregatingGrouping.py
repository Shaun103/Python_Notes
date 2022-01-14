import pandas as pd

df = pd.read_csv('survey_results_public.csv', index_col='Respondent')  # order by ether
df_schema = pd.read_csv('survey_results_schema.csv', index_col='Column') # order by Column

pd.set_option('display.max_columns', 85)
pd.set_option('display.max_rows', 85)

#__________________________________________________
# grabing the first 15 columns of ConvertedComp
print(df['ConvertedComp'].head(15))

#__________________________________________________
# displaying the median of ConvertedComp 

print(df['ConvertedComp'].median())

print(df.median())    # displaying median of all data

#__________________________________________________
# Describe - overview of data 
    # count = NAN missing rows 

print(df.describe())   # Brief description of data

print(df['ConvertedComp'].count())  # how many NAN rows 

#__________________________________________________
# value_counts - how many times event occured

print(df['Hobbyist']) # grabing the Hobbyist column

print(df['Hobbyist'].value_counts())

print(df['Hobbyist'].value_counts(normalize=True)) # showing by percentage

#__________________________________________________
# #
#
# IMPORTANT # country_grp
# grouypby - Spliting the data, appling a function, and combine results
# #
#__________________________________________________

print(df['Country'].values)  # showing columns 
print(df['Country'].value_counts())  

#__________________________________________________
# groupby objects - spliting data __________________________________________________ 

country_grp = df.groupby(['Country']) # dataframe object
print(country_grp)

################################################
################################################

print(country_grp.get_group('United States'))

filt = df['Country'] == 'United States'  # creating a filter 
print(df.loc[filt])

#__________________________________________________

print(df.loc[filt]['Hobbyist'].value_counts())

# #__________________________________________________
# Viewing value counts on entire data

print(country_grp['Hobbyist'].value_counts().head(50))

#__________________________________________________
# value_counts - on specific country

print(country_grp['Hobbyist'].value_counts().loc['United States'])

#__________________________________________________
# value_counts - Showing percents 

print(country_grp['Hobbyist'].value_counts(normalize=True).loc['United States']) 

#__________________________________________________

print(country_grp['ConvertedComp'].median())

print(country_grp['ConvertedComp'].median().loc['Germany'])

print(country_grp['ConvertedComp'].agg(['median', 'mean']).loc['Canada'])

#__________________________________________________

filt = df['Country'] == 'India'
print(df.loc[filt]['LanguageWorkedWith'])

print(df.loc[filt]['LanguageWorkedWith'].str.contains('Python'))

print(df.loc[filt]['LanguageWorkedWith'].str.contains('Python').sum())

print(country_grp['LanguageWorkedWith'].apply(lambda x: x.str.contains('Python').sum()))

#__________________________________________________
# Setting up columns side by side together

# How many people from each Country
country_respondents = df['Country'].value_counts() 
print(country_respondents)

# Different number of programming languages worked with  
countries_uses_python = country_grp['LanguageWorkedWith'].apply(lambda x: x.str.contains('Python').sum())
print(countries_uses_python)

# Combining all data together
python_df = pd.concat([country_respondents, countries_uses_python], axis='columns', sort=False)

# Renaming columns 
python_df.rename(columns={'Country': 'NumRespondents', 'LanguageWorkedWith': 'NumKnowsPython'}, inplace=True)

# creating new column 
python_df['PctKnowsPython'] = (python_df['NumKnowsPython']/python_df['NumRespondents']) * 100
print(python_df)

# Sorting data 
python_df.sort_values(by='PctKnowsPython', ascending=False, inplace=True)

print(python_df.head(50))

# #__________________________________________________
# # Grabing specific Country

print(python_df.loc['Japan'])
