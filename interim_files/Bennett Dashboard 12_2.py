from dash import Dash, dcc, html, Input, Output
import pandas as pd
import plotly.express as px
import dash_bootstrap_components as dbc

app = Dash(external_stylesheets=[dbc.themes.COSMO])

df = pd.read_csv("updated_mcd_data.csv")

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
                ["Calories", "Total Fat"],
                "Calories",
                id = "feature",
                inline = True,
            ),
            dcc.Graph(id="graph-of-calories"),
            dcc.Graph(id='daily-value-pie'),
            dbc.Table([
                html.Thead(html.Tr([html.Th("Nutrition Fact"), html.Th("Amount"), html.Th("Daily Value")])),
                html.Tr([html.Td("Total Calories:"), html.Td(id='calorie-amount'), html.Td(id="daily-calories")]),
                html.Tr([html.Td("Total Fats:"), html.Td(id='fat-amount'), html.Td(id="daily-fats")]),
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
            ]),
        ], style={'padding': 10, 'flex': 1}),
    ], style={'display': 'flex', 'flex-direction': 'row'}),
])

## LEFT SIDE

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

    input_dict = {"Calories": "nf_calories", "Total Fat":"nf_total_fat"}

    fig = px.bar(filtered_df, x = "item_name", y=input_dict[input_feature])
    fig.update_layout(transition_duration = 400)

    return fig

@app.callback(
    Output(component_id='calorie-amount', component_property='children'),
    Output(component_id='fat-amount', component_property='children'),
    Output(component_id='daily-calories', component_property='children'),
    Output(component_id='daily-fats', component_property='children'),
    Output(component_id='daily-value-pie', component_property='figure'),
    Input(component_id='my-brand', component_property='value'),
    Input(component_id='food-options', component_property='value'),
    Input(component_id = 'feature', component_property = 'value'),
)
def word_pie_output(input_brand, food_choices, feature):
    filtered_df_item = df[df["brand_name"] == input_brand]
    if food_choices is None:
        food_choices = list(filtered_df_item['item_name'][0])
    filtered_df = filtered_df_item[filtered_df_item['item_name'].isin(food_choices)]
    calorie_total = sum(filtered_df["nf_calories"])
    fat_total = sum(filtered_df["nf_total_fat"])
    calorie_daily = (round((calorie_total / 2000) * 100, 2)) 
    fat_daily = (round((fat_total / 78) * 100, 2))

    if feature == "Calories":
        leftover = 100 - calorie_daily
        if calorie_daily >= 100:
            pie = px.pie(values=[calorie_daily, 0], names = ["Daily Value from Meal", "Remaining"], title="Daily Value of Calories -- Meal Exceeds Daily Value")
        else:    
            pie = px.pie(values=[calorie_daily, leftover], names = ["Daily Value from Meal", "Remaining"], title="Daily Value of Calories")
    if feature == "Total Fat":
        leftover = 100 - fat_daily
        if fat_daily >= 100:
            pie = px.pie(values=[fat_daily, 0], names = ["Daily Value from Meal", "Remaining"], title="Daily Value of Fats -- Meal Exceeds Daily Value")
        else:
            pie = px.pie(values=[fat_daily, leftover], names = ["Daily Value from Meal", "Remaining"], title="Daily Value of Fats")

    return calorie_total, fat_total, str(calorie_daily) + "%", str(fat_daily) + "%", pie

## RIGHT SIDE

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

    return calorie_total, fat_total


if __name__ == '__main__':
    app.run_server(debug=True)