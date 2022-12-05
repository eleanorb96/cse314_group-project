from dash import Dash, dcc, html, Input, Output
import pandas as pd
import plotly.express as px
import dash_bootstrap_components as dbc

app = Dash(external_stylesheets=[dbc.themes.COSMO])

df = pd.read_csv("sample_data.csv")

# 'McDonalds', 'Subway', 'Taco Bell', 'Chick-Fil-A', 'Wendy\'s', 'Burger King', 'Domino\'s', 'Panera Bread', 'Pizza Hut', 'Chipotle'

app.layout = html.Div(children = [
    html.H1(
        children='Compare Your Favorite Fast Food Meals',
        style={
            'textAlign': 'center',
        }
    ),
    html.H4("Choose Two Restaurants to Compare:"),
    html.Div([
        html.Div([
            dcc.Dropdown(
                df['brand_name'].unique(),
                df['brand_name'][0],
                id='my-brand',
                clearable = False
            ),
            dcc.Dropdown(
                id = 'food-options',
                multi = True,
                placeholder="Select Food Items"
            ),
            dcc.RadioItems(
                ["nf_calories", "nf_total_fat"],
                "nf_calories",
                id = "feature"
            ),
            dcc.Graph(id="graph-of-calories"),
            html.Br(),
            html.Table([
                html.Tr([html.Td("Total Calories:"), html.Td(id='calorie-amount')]),
                html.Tr([html.Td("Total Fats:"), html.Td(id='fat-amount')]),
                html.Tr([html.Td("Total Cholesterol:"), html.Td(id='chol-amount')]),
            ]),
        ], style={'padding': 10, 'flex': 1}), 
        html.Div([
            dcc.Dropdown(
                df['brand_name'].unique(),
                df['brand_name'][0],
                id='my-brand2',
                clearable = False
            ),
            dcc.Dropdown(
                id = 'food-options2',
                multi = True,
                placeholder="Select Food Items",
            ),
            dcc.RadioItems(
                ["nf_calories", "nf_total_fat"],
                "nf_calories",
                id = "feature2"
            ),
            dcc.Graph(id="graph-of-calories2"),
            html.Br(),
            html.Table([
                html.Tr([html.Td("Total Calories:"), html.Td(id='calorie-amount2')]),
                html.Tr([html.Td("Total Fats:"), html.Td(id='fat-amount2')]),
                html.Tr([html.Td("Total Cholesterol:"), html.Td(id='chol-amount2')]),
            ]),
        ], style={'padding': 10, 'flex': 1}),
    
    
    
    ], style={'display': 'flex', 'flex-direction': 'row'}),

    dcc.Graph(id="comparison"),
])



## BOTTOM

@app.callback(
    Output(component_id='comparison', component_property='figure'),
    Input(component_id='my-brand', component_property='value'),
    Input(component_id='food-options', component_property='value'),
    Input(component_id='my-brand2', component_property='value'),
    Input(component_id='food-options2', component_property='value'),
)
def update_comparison(brand1, items1, brand2, items2):

    filtered_df_item1 = df[df["brand_name"] == brand1]
    if items1 is None:
        items1 = list(filtered_df_item1['item_name'][0])
    filtered_df1 = filtered_df_item1[filtered_df_item1['item_name'].isin(items1)]
    calorie_total1 = sum(filtered_df1["nf_calories"])
    fat_total1 = sum(filtered_df1["nf_total_fat"])

    filtered_df_item2 = df[df["brand_name"] == brand2]
    if items2 is None:
        items2 = list(filtered_df_item2['item_name'][0])
    filtered_df2 = filtered_df_item2[filtered_df_item2['item_name'].isin(items2)]
    calorie_total2 = sum(filtered_df2["nf_calories"])
    fat_total2 = sum(filtered_df2["nf_total_fat"])

    if fat_total2==0:
        fat_total2+=1
    if calorie_total2==0:
        calorie_total2+=1
    if fat_total1==0:
        fat_total1+=1
    
    if calorie_total1==0:
        calorie_total1+=1

    calrat = calorie_total1/calorie_total2
    fatrat = fat_total1/fat_total2

    if calrat < 1:
        calcol = "green"
    else:
        calcol = "red"

    if fatrat < 1:
        fatcol = "green"
    else:
        fatcol = "red"
    

    fig = px.bar(x = ["Calories", "Fat"], y = [calrat, fatrat], title="Nutrion Ratios (Meal 1 / Meal 2)", labels={"x":"Nutrition Statistic", "y":"Ratio"})
    fig.update_traces(marker_color=[calcol, fatcol])
    fig.add_hline(y=1)



    return fig





## RIGHT SIDE

@app.callback(
    Output('food-options', 'options'),
    Input('my-brand', 'value'))
def set_options(selected_brand):
    filtered_df = df[df['brand_name'] == selected_brand]
    return filtered_df['item_name'].unique()

@app.callback(
    Output('food-options', 'value'),
    Input('food-options', 'options'))
def set_cities_value(available_options):
    return list(available_options[0])

@app.callback(
    Output(component_id='graph-of-calories', component_property='figure'),
    Input(component_id='my-brand', component_property='value'),
    Input(component_id = 'feature', component_property = 'value'),
    Input(component_id='food-options', component_property='value')
)
def update_graph(input_brand, input_feature, food_choices):
    filtered_df_item = df[df["brand_name"] == input_brand]
    if food_choices is None:
        food_choices = list(filtered_df_item['item_name'][0])

    filtered_df = filtered_df_item[filtered_df_item['item_name'].isin(food_choices)]

    fig = px.bar(filtered_df, x = "item_name", y=input_feature)
    fig.update_layout(transition_duration = 400)

    return fig

@app.callback(
    Output(component_id='calorie-amount', component_property='children'),
    Output(component_id='fat-amount', component_property='children'),
    Output(component_id='chol-amount', component_property='children'),
    Input(component_id='my-brand', component_property='value'),
    Input(component_id='food-options', component_property='value')
)
def word_output(input_brand, food_choices):
    filtered_df_item = df[df["brand_name"] == input_brand]
    if food_choices is None:
        food_choices = list(filtered_df_item['item_name'][0])
    filtered_df = filtered_df_item[filtered_df_item['item_name'].isin(food_choices)]
    calorie_total = sum(filtered_df["nf_calories"])
    fat_total = sum(filtered_df["nf_total_fat"])
    chol_total = sum(filtered_df["nf_cholesterol"])

    return calorie_total, fat_total, chol_total

## LEFT SIDE

@app.callback(
    Output('food-options2', 'options'),
    Input('my-brand2', 'value'))
def set_options(selected_brand):
    filtered_df = df[df['brand_name'] == selected_brand]
    return filtered_df['item_name'].unique()

@app.callback(
    Output('food-options2', 'value'),
    Input('food-options2', 'options'))
def set_cities_value(available_options):
    return list(available_options[0])

@app.callback(
    Output(component_id='graph-of-calories2', component_property='figure'),
    Input(component_id='my-brand2', component_property='value'),
    Input(component_id = 'feature2', component_property = 'value'),
    Input(component_id='food-options2', component_property='value')
)
def update_graph(input_brand, input_feature, food_choices):
    filtered_df_item = df[df["brand_name"] == input_brand]
    if food_choices is None:
        food_choices = list(filtered_df_item['item_name'][0])

    filtered_df = filtered_df_item[filtered_df_item['item_name'].isin(food_choices)]
    
    fig = px.bar(filtered_df, x = "item_name", y=input_feature)
    fig.update_layout(transition_duration = 400)

    return fig

@app.callback(
    Output(component_id='calorie-amount2', component_property='children'),
    Output(component_id='fat-amount2', component_property='children'),
    Output(component_id='chol-amount2', component_property='children'),
    Input(component_id='my-brand2', component_property='value'),
    Input(component_id='food-options2', component_property='value')
)
def word_output(input_brand, food_choices):
    filtered_df_item = df[df["brand_name"] == input_brand]
    if food_choices is None:
        food_choices = list(filtered_df_item['item_name'][0])
    filtered_df = filtered_df_item[filtered_df_item['item_name'].isin(food_choices)]
    calorie_total = sum(filtered_df["nf_calories"])
    fat_total = sum(filtered_df["nf_total_fat"])
    chol_total = sum(filtered_df["nf_cholesterol"])

    return calorie_total, fat_total, chol_total


if __name__ == '__main__':
    app.run_server(debug=True)