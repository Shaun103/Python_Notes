import pandas as pd

people = {
    "first": ['Corey', 'Jane', 'John'],
    "last": ['Schafer', 'Doe', 'Doe'],
    "email": ['CoreyMSchafer@email.com', 'JaneDoe@gmail.com', 'JohnDoe@email.com']
}

df = pd.DataFrame(people)

#__________________________________________________
# Joining two columns

print(df['first'] + ' ' + df['last'])

df['full_name'] = df['first'] + ' ' + df['last']
print(df)

#__________________________________________________
# Removing columns

df.drop(columns=['first', 'last'], inplace=True)
print(df)

df['full_name'].str.split(' ', expand=True)
print(df)

#__________________________________________________
# Adding multiple columns (first, last) from one column (full_name)

df[['first', 'last']] = df['full_name'].str.split(' ', expand=True)
print(df)

# __________________________________________________
# adding row to data 

print(df.append({'first': 'Tony'}, ignore_index=True))

# __________________________________________________

people = {
    "first": ['Tony', 'Steve'],
    "last": ['Stark', 'Rogers'],
    "email": ['IronMan@email.com', 'Cap@gmail.com']
}

df2 = pd.DataFrame(people)
# print(df2)

# __________________________________________________
# adding df2 to df

df = df.append(df2, ignore_index=True, sort=False)

# __________________________________________________
# droping row of data 

df = df.drop(index=4)
print(df)

# __________________________________________________
# filtering through data rows 

filt = df['last'] == 'Doe'
df = df.drop(index=df[filt].index)

print(df)

# __________________________________________________
# Same as top but less readable

df = df.drop(index=df[df['last'] == 'Doe'].index)
print(df)