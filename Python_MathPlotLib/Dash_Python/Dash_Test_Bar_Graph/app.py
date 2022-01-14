#######################################################
# visit http://127.0.0.1:8050/ in your web browser.
#######################################################

from os import name
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

path = '/Users/User/Desktop/Python/Dash_Python/Dash_Test_Bar_Graph/bestsellers_with_categories.csv'

# # Data to be read
data = pd.read_csv(path)

# ##############################################################
# # # # Deletes duplicates
# # path2 = '/Users/User/Desktop/Python/Dash_Python/Dash_Test_Bar_Graph/bestsellers_with_categories2.csv'
# # data.drop_duplicates(keep = False, inplace = True) 
# # data.to_csv(path2)
# ##############################################################

# # Selects the n rows
data = pd.read_csv(path, nrows=20)
# print(data)

dataName1 = data['Author'] # selects the Author Category 
# print(dataName1)

dataName2 = data['Price'] # selects the Price Category 
# print(dataName2)

dataName3 = data['Year'] # selects the Year Category 
# print(dataName3)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options

df = pd.DataFrame({
    "Author": dataName1,
    "Price": dataName2,
    "Year": dataName3
})

fig = px.bar(df, x="Author", y="Price", color="Year", barmode="group")

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for Python.
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)


###################################################
###################################################
import pandas as pd

path = '/Users/User/Desktop/Python/Dash_Python/Dash_Test_Bar_Graph/bestsellers_with_categories.csv'

# # Selects the n rows
data = pd.read_csv(path, nrows=20)

# print(data) # Prints all data 

dataName1 = data['Author'] # selects the Author Category 
print(dataName1)

