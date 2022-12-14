from dash import Dash, dcc, html, Input, Output
import pandas as pd
import plotly.express as px
import dash_bootstrap_components as dbc

app = Dash(external_stylesheets=[dbc.themes.COSMO])

df = pd.read_csv("sample_data.csv")

# 'McDonalds', 'Subway', 'Taco Bell', 'Chick-Fil-A', 'Wendy\'s', 'Burger King', 'Domino\'s', 'Panera Bread', 'Pizza Hut', 'Chipotle'

app.layout = html.Div(children=[
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
                df['brand'].unique(),
                df['brand'][0],
                id='my-brand',
                clearable=False
            ),
            dcc.Dropdown(
                id='food-options',
                multi=True,
                placeholder="Select Food Items"
            ),
            dcc.RadioItems(
                ["calories", "fat"],
                "calories",
                id="feature"
            ),
            dcc.Graph(id="graph-of-calories"),
            html.Br(),
            html.Table([
                html.Tr([html.Td("Total Calories:"),
                        html.Td(id='calorie-amount')]),
                html.Tr([html.Td("Total Fats:"), html.Td(id='fat-amount')]),
            ]),
        ], style={'padding': 10, 'flex': 1}),
        html.Div([
            dcc.Dropdown(
                df['brand'].unique(),
                df['brand'][0],
                id='my-brand2',
                clearable=False
            ),
            dcc.Dropdown(
                id='food-options2',
                multi=True,
                placeholder="Select Food Items",
            ),
            dcc.RadioItems(
                ["calories", "fat"],
                "calories",
                id="feature2"
            ),
            dcc.Graph(id="graph-of-calories2"),
            html.Br(),
            html.Table([
                html.Tr([html.Td("Total Calories:"),
                        html.Td(id='calorie-amount2')]),
                html.Tr([html.Td("Total Fats:"), html.Td(id='fat-amount2')]),
            ]),
        ], style={'padding': 10, 'flex': 1}),
    ], style={'display': 'flex', 'flex-direction': 'row'}),
])

# RIGHT SIDE


@app.callback(
    Output('food-options', 'options'),
    Input('my-brand', 'value'))
def set_options(selected_brand):
    """ Set the options on a given brand.

    Args:
        selected_brand (str): The brand name to filter the datafram by.

    Returns: 
        List[str]: A list of unique items from the "item" column of the filtered dataframe.
    """
    filtered_df = df[df['brand'] == selected_brand]
    return filtered_df['item'].unique()


@app.callback(
    Output('food-options', 'value'),
    Input('food-options', 'options'))
def set_cities_value(available_options):
    """
    Set the initial value of a list of cities based on a list of available options.

    The initial value of the list of cities is set to the first item in the
    `available_options` list.

    Args:
        available_options (List[List[str]]): A list of lists of city names, 
                                             where each sublist represents a group of cities.

    Returns:
        List[str]: The first group of cities from the `available_options` list.
    """
    return list(available_options[0])


@app.callback(
    Output(component_id='graph-of-calories', component_property='figure'),
    Input(component_id='my-brand', component_property='value'),
    Input(component_id='feature', component_property='value'),
    Input(component_id='food-options', component_property='value')
)
def update_graph(input_brand, input_feature, food_choices):
    """ Update a bar chart with data for a given brand and feature,
    and a list of food choices.

    Args:
        input_brand (str): The brand name to filter the dataframe by.
        input_feature (str): The column name to use for the y axis of the chart.
        food_choices (List[str]): A list of food item names to filter the dataframe by.

    Returns: 
        plotly.graph.objects.Figure: A figure object containing the updated bar chart.
    """
    filtered_df_item = df[df["brand"] == input_brand]
    if food_choices is None:
        food_choices = list(filtered_df_item['item'][0])

    filtered_df = filtered_df_item[filtered_df_item['item'].isin(food_choices)]

    fig = px.bar(filtered_df, x="item", y=input_feature)
    fig.update_layout(transition_duration=400)

    return fig


@app.callback(
    Output(component_id='calorie-amount', component_property='children'),
    Output(component_id='fat-amount', component_property='children'),
    Input(component_id='my-brand', component_property='value'),
    Input(component_id='food-options', component_property='value')
)
def word_output(input_brand, food_choices):
    """ 
    Generate the calorie and fat totals for a given brand and list of food choices.

    Args:
        input_brand (str): The brand name to filter the dataframe by.
        food_choices (List[str]): A list of food item names to filter the dataframe by.

    Returns:
        Tuple[int, int]: A tuple containing the total caloreis and fat content of the filtered dataframe.
    """
    filtered_df_item = df[df["brand"] == input_brand]
    if food_choices is None:
        food_choices = list(filtered_df_item['item'][0])
    filtered_df = filtered_df_item[filtered_df_item['item'].isin(food_choices)]
    calorie_total = sum(filtered_df["calories"])
    fat_total = sum(filtered_df["fat"])

    return calorie_total, fat_total

# LEFT SIDE


@app.callback(
    Output('food-options2', 'options'),
    Input('my-brand2', 'value'))
def set_options(selected_brand):
    """ Set the options on a given brand.

    Args:
        selected_brand (str): The brand name to filter the datafram by.

    Returns: 
        List[str]: A list of unique items from the "item" column of the filtered dataframe.
    """
    filtered_df = df[df['brand'] == selected_brand]
    return filtered_df['item'].unique()


@app.callback(
    Output('food-options2', 'value'),
    Input('food-options2', 'options'))
def set_cities_value(available_options):
    """
    Set the initial value of a list of cities based on a list of available options.

    The initial value of the list of cities is set to the first item in the
    `available_options` list.

    Args:
        available_options (List[List[str]]): A list of lists of city names, 
                                             where each sublist represents a group of cities.

    Returns:
        List[str]: The first group of cities from the `available_options` list.
    """
    return list(available_options[0])


@app.callback(
    Output(component_id='graph-of-calories2', component_property='figure'),
    Input(component_id='my-brand2', component_property='value'),
    Input(component_id='feature2', component_property='value'),
    Input(component_id='food-options2', component_property='value')
)
def update_graph(input_brand, input_feature, food_choices):
    """ Update a bar chart with data for a given brand and feature,
    and a list of food choices.

    Args:
        input_brand (str): The brand name to filter the dataframe by.
        input_feature (str): The column name to use for the y axis of the chart.
        food_choices (List[str]): A list of food item names to filter the dataframe by.

    Returns: 
        plotly.graph.objects.Figure: A figure object containing the updated bar chart.
    """
    filtered_df_item = df[df["brand"] == input_brand]
    if food_choices is None:
        food_choices = list(filtered_df_item['item'][0])

    filtered_df = filtered_df_item[filtered_df_item['item'].isin(food_choices)]

    fig = px.bar(filtered_df, x="item", y=input_feature)
    fig.update_layout(transition_duration=400)

    return fig


@app.callback(
    Output(component_id='calorie-amount2', component_property='children'),
    Output(component_id='fat-amount2', component_property='children'),
    Input(component_id='my-brand2', component_property='value'),
    Input(component_id='food-options2', component_property='value')
)
def word_output(input_brand, food_choices):
    """ 
    Generate the calorie and fat totals for a given brand and list of food choices.

    Args:
        input_brand (str): The brand name to filter the dataframe by.
        food_choices (List[str]): A list of food item names to filter the dataframe by.

    Returns:
        Tuple[int, int]: A tuple containing the total caloreis and fat content of the filtered dataframe.
    """
    filtered_df_item = df[df["brand"] == input_brand]
    if food_choices is None:
        food_choices = list(filtered_df_item['item'][0])
    filtered_df = filtered_df_item[filtered_df_item['item'].isin(food_choices)]
    calorie_total = sum(filtered_df["calories"])
    fat_total = sum(filtered_df["fat"])

    return calorie_total, fat_total


if __name__ == '__main__':
    app.run_server(debug=True)
