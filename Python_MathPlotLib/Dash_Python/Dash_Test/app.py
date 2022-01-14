#######################################################
# visit http://127.0.0.1:8050/ in your web browser.
#######################################################


from os import name
import dash
import dash_table
import pandas as pd

path = '/Users/User/Desktop/Python/Dash_Python/archive/bestsellers_with_categories.csv'
# df = pd.read_csv(path)

## Selects the first two rows
data = pd.read_csv(path, nrows=6)
print(data)

dataName1 = data['Author']
print(dataName1)

dataName2 = data['Price']
print(dataName2)

dataName3 = data['Year']
print(dataName3)


# app = dash.Dash(__name__)

# app.layout = dash_table.DataTable(
#     id='table',
#     columns=[{"name": i, "id": i} for i in df.columns],
#     data=df.to_dict('records'),
#     # style_table={'height': '300px', 'overflowY': 'auto'}
# )

# if __name__ == '__main__':
#     app.run_server(debug=True)

#######################################################
#######################################################
#######################################################

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

path = '/Users/User/Desktop/Python/Dash_Python/archive/bestsellers_with_categories.csv'
# df = pd.read_csv(path)


## Selects the first two rows
data = pd.read_csv(path, nrows=6)
print(data)

dataName1 = data['Author'] # selects the Author Category 
print(dataName1)

dataName2 = data['Price'] # selects the Price Category 
print(dataName2)

dataName3 = data['Year'] # selects the Year Category 
print(dataName3)


# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options

df = pd.DataFrame({
    "Fruit": dataName1,
    "Amount": dataName2,
    "City": dataName3
})

fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

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


######################################
######################################
######################################
# import dash
# import dash_core_components as dcc
# import dash_html_components as html
# import plotly.express as px
# import pandas as pd

# external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

# app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


# # assume you have a "long-form" data frame
# # see https://plotly.com/python/px-arguments/ for more options

# # df = pd.DataFrame({
# #     "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
# #     "Amount": [40, 10, 20, 20, 40, 50],
# #     "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
# # })

# df = [{'Fruit': strings, 'Amount': numbers, 'City': strings2} for strings,numbers,strings2 in zip(strings,numbers,strings2)]

# # mydict1 = {}
# strings = list("#A{0}".format(i) for i in range(1,101))
# # strings = mydict1["Fruits: "] = strings
# # print(strings)

# # mydict2 = {}
# numbers = list(i for i in range(101,201))
# # numbers = mydict2["Amount: "] = numbers
# # # print(mydict2)

# # mydict3 = {}
# strings2 = list("#B{0}".format(i) for i in range(1,101))
# # strings2 = mydict3["City: "] = strings2
# # print(mydict3)

# df = [{'Fruit': strings, 'Amount': numbers, 'City': strings2} for strings,numbers,strings2 in zip(strings,numbers,strings2)]


# fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

# app.layout = html.Div(children=[
#     html.H1(children='Hello Dash'),

#     html.Div(children='''
#         Dash: A web application framework for Python.
#     '''),

#     dcc.Graph(
#         id='example-graph',
#         figure=fig
#     )
# ])

# if __name__ == '__main__':
#     app.run_server(debug=True)


############################################################
############################################################
############################################################
############################################################
############################################################


# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

# import dash
# import dash_html_components as html
# import pandas as pd

# # Data being visualized 
# df = pd.read_csv('https://gist.githubusercontent.com/chriddyp/c78bf172206ce24f77d6363a2d754b59/raw/c353e8ef842413cae56ae3920b8fd78468aa4cb2/usa-agricultural-exports-2011.csv')


# def generate_table(dataframe, max_rows=10):
#     return html.Table([
#         html.Thead(
#             html.Tr([html.Th(col) for col in dataframe.columns])
#         ),
#         html.Tbody([
#             html.Tr([
#                 html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
#             ]) for i in range(min(len(dataframe), max_rows))
#         ])
#     ])


# external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

# app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# app.layout = html.Div(children=[
#     html.H4(children='US Agriculture Exports (2011)'),
#     generate_table(df)
# ])

# if __name__ == '__main__':
#     app.run_server(debug=True)


############################################################
############################################################
############################################################
############################################################
############################################################


# # Run this app with `python app.py` and
# # visit http://127.0.0.1:8050/ in your web browser.

# import dash
# import dash_core_components as dcc
# import dash_html_components as html
# import plotly.express as px
# import pandas as pd


# external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

# app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# df = pd.read_csv('https://gist.githubusercontent.com/chriddyp/5d1ea79569ed194d432e56108a04d188/raw/a9f9e8076b837d541398e999dcbac2b2826a81f8/gdp-life-exp-2007.csv')

# fig = px.scatter(df, x="gdp per capita", y="life expectancy",
#                  size="population", color="continent", hover_name="country",
#                  log_x=True, size_max=60)

# app.layout = html.Div([
#     dcc.Graph(
#         id='life-exp-vs-gdp',
#         figure=fig
#     )
# ])

# if __name__ == '__main__':
#     app.run_server(debug=True)


############################################################
############################################################
############################################################
# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

# import dash
# import dash_html_components as html
# import pandas as pd

# df = pd.read_csv('https://gist.githubusercontent.com/chriddyp/c78bf172206ce24f77d6363a2d754b59/raw/c353e8ef842413cae56ae3920b8fd78468aa4cb2/usa-agricultural-exports-2011.csv')


# def generate_table(dataframe, max_rows=10):
#     return html.Table([
#         html.Thead(
#             html.Tr([html.Th(col) for col in dataframe.columns])
#         ),
#         html.Tbody([
#             html.Tr([
#                 html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
#             ]) for i in range(min(len(dataframe), max_rows))
#         ])
#     ])


# external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

# app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# app.layout = html.Div(children=[
#     html.H4(children='US Agriculture Exports (2011)'),
#     generate_table(df)
# ])

# if __name__ == '__main__':
#     app.run_server(debug=True)