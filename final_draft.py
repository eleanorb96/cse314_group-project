import dash
from dash import Dash, dcc, html, Input, Output
import pandas as pd
import plotly.express as px
import dash_bootstrap_components as dbc

app = dash.Dash(external_stylesheets=[dbc.themes.CERULEAN])

df = pd.read_csv(
    "https://raw.githubusercontent.com/eleanorb96/cse314_group-project/all_restaurant_data.csv")

# 'McDonalds', 'Subway', 'Taco Bell', 'Chick-Fil-A', 'Wendy\'s', 'Burger King', 'Domino\'s', 'Panera Bread', 'Pizza Hut', 'Chipotle'

app.layout = html.Div(children=[
    html.H1(
        children='Compare Your Favorite Fast Food Meals',
        style={
            'textAlign': 'center',
        }
    ),
    html.H5(
        children="Welcome to our Dashboard to compare Nutrition Facts between your favorite meals at 10 of your favorite fast food restaurants!",
        style={
            'textAlign': 'center',
        }
    ),
    html.H5(
        children="Select two restaurants to begin and start building your meal!",
        style={
            'textAlign': 'center',
        }
    ),
    html.Div([
        html.Div([
            dcc.Dropdown(
                df['brand_name'].unique(),
                df['brand_name'][0],
                id='my-brand',
                clearable=False
            ),
            dcc.Dropdown(
                id='food-options',
                multi=True,
                placeholder="Select Food Items"
            ),
            dcc.RadioItems(
                ["Calories", "Nutrients"],
                "Calories",
                id="feature"
            ),
            dcc.Graph(id="graph-of-calories"),
            html.Br(),
            dbc.Table([
                html.Thead(html.Tr([html.Th("Nutrition Fact"), html.Th(
                    "Amount"), html.Th("Daily Value")])),
                html.Tr([html.Td("Total Calories:"), html.Td(
                    id='calorie-amount'), html.Td(id="daily-calories")]),
                html.Tr([html.Td("Total Fat:"), html.Td(
                    id='fat-amount'), html.Td(id="daily-fats")]),
                html.Tr([html.Td("Saturated Fat:"), html.Td(
                    id='satfat-amount'), html.Td(id="daily-satfat")]),
                html.Tr([html.Td("Trans Fat:"), html.Td(
                    id='tranfat-amount'), html.Td("")]),
                html.Tr([html.Td("Cholesterol:"), html.Td(
                    id='chol-amount'), html.Td(id="daily-chol")]),
                html.Tr([html.Td("Sodium:"), html.Td(
                    id='sodium-amount'), html.Td(id="daily-sodium")]),
                html.Tr([html.Td("Total Carbohydrate:"), html.Td(
                    id='carb-amount'), html.Td(id="daily-carb")]),
                html.Tr([html.Td("Dietary Fiber:"), html.Td(
                    id='fiber-amount'), html.Td(id="daily-fiber")]),
                html.Tr([html.Td("Sugars:"), html.Td(
                    id='sugar-amount'), html.Td("")]),
                html.Tr([html.Td("Protein:"), html.Td(
                    id='protein-amount'), html.Td(id="daily-protein")]),
                html.Tr([html.Td("Vitamin A:"), html.Td(
                    ""), html.Td(id="daily-A")]),
                html.Tr([html.Td("Vitamin C:"), html.Td(
                    ""), html.Td(id="daily-C")]),
                html.Tr([html.Td("Calcium:"), html.Td(
                    ""), html.Td(id="daily-calcium")]),
                html.Tr([html.Td("Iron:"), html.Td(
                    ""), html.Td(id="daily-iron")]),
            ]),
        ], style={'padding': 10, 'flex': 1}),
        html.Div([
            dcc.Dropdown(
                df['brand_name'].unique(),
                df['brand_name'][0],
                id='my-brand2',
                clearable=False
            ),
            dcc.Dropdown(
                id='food-options2',
                multi=True,
                placeholder="Select Food Items",
            ),
            dcc.RadioItems(
                ["Calories", "Nutrients"],
                "Calories",
                id="feature2"
            ),
            dcc.Graph(id="graph-of-calories2"),
            html.Br(),
            dbc.Table([
                html.Thead(html.Tr([html.Th("Nutrition Fact"), html.Th(
                    "Amount"), html.Th("Daily Value")])),
                html.Tr([html.Td("Total Calories:"), html.Td(
                    id='calorie-amount2'), html.Td(id="daily-calories2")]),
                html.Tr([html.Td("Total Fat:"), html.Td(
                    id='fat-amount2'), html.Td(id="daily-fats2")]),
                html.Tr([html.Td("Saturated Fat:"), html.Td(
                    id='satfat-amount2'), html.Td(id="daily-satfat2")]),
                html.Tr([html.Td("Trans Fat:"), html.Td(
                    id='tranfat-amount2'), html.Td("")]),
                html.Tr([html.Td("Cholesterol:"), html.Td(
                    id='chol-amount2'), html.Td(id="daily-chol2")]),
                html.Tr([html.Td("Sodium:"), html.Td(
                    id='sodium-amount2'), html.Td(id="daily-sodium2")]),
                html.Tr([html.Td("Total Carbohydrate:"), html.Td(
                    id='carb-amount2'), html.Td(id="daily-carb2")]),
                html.Tr([html.Td("Dietary Fiber:"), html.Td(
                    id='fiber-amount2'), html.Td(id="daily-fiber2")]),
                html.Tr([html.Td("Sugars:"), html.Td(
                    id='sugar-amount2'), html.Td("")]),
                html.Tr([html.Td("Protein:"), html.Td(
                    id='protein-amount2'), html.Td(id="daily-protein2")]),
                html.Tr([html.Td("Vitamin A:"), html.Td(
                    ""), html.Td(id="daily-A2")]),
                html.Tr([html.Td("Vitamin C:"), html.Td(
                    ""), html.Td(id="daily-C2")]),
                html.Tr([html.Td("Calcium:"), html.Td(
                    ""), html.Td(id="daily-calcium2")]),
                html.Tr([html.Td("Iron:"), html.Td(
                    ""), html.Td(id="daily-iron2")]),
            ]),
        ], style={'padding': 10, 'flex': 1}),



    ], style={'display': 'flex', 'flex-direction': 'row'}),

    dcc.Graph(id="comparison"),
])


# BOTTOM

@app.callback(
    Output(component_id='comparison', component_property='figure'),
    Input(component_id='my-brand', component_property='value'),
    Input(component_id='food-options', component_property='value'),
    Input(component_id='my-brand2', component_property='value'),
    Input(component_id='food-options2', component_property='value'),
)
def update_comparison(brand1, items1, brand2, items2):
    """
    This function compares the nutritional values of two meals, given the brand names and items for each meal. 
    The nutritional values compared are calories, calories from fat, calories from carbohydrates, and calories from 
    protein. The function returns a bar chart showing the differences between the two meals for each of these 
    nutritional values.

    Inputs:
        - brand1 (string): the name of the brand for the first meal
        - items1 (list of strings): the names of the items in the first meal
        - brand2 (string): the name of the brand for the second meal
        - items2 (list of strings): the names of the items in the second meal

    Output:
        - fig (plotly bar chart object): a bar chart showing the differences in 
        nutritional values between the two meals
    """

    filtered_df_item1 = df[df["brand_name"] == brand1]
    if items1 is None:
        items1 = list(filtered_df_item1['item_name'][0])
    filtered_df1 = filtered_df_item1[filtered_df_item1['item_name'].isin(
        items1)]
    calorie_total1 = sum(filtered_df1["nf_calories"])
    fat_total1 = sum(filtered_df1["nf_total_fat"])
    carb_total1 = sum(filtered_df1["nf_total_carbohydrate"])
    protein_total1 = sum(filtered_df1["nf_protein"])

    filtered_df_item2 = df[df["brand_name"] == brand2]
    if items2 is None:
        items2 = list(filtered_df_item2['item_name'][0])
    filtered_df2 = filtered_df_item2[filtered_df_item2['item_name'].isin(
        items2)]
    calorie_total2 = sum(filtered_df2["nf_calories"])
    fat_total2 = sum(filtered_df2["nf_total_fat"])
    carb_total2 = sum(filtered_df2["nf_total_carbohydrate"])
    protein_total2 = sum(filtered_df2["nf_protein"])

    calfat1 = fat_total1*9
    calfat2 = fat_total2*9
    calcarb1 = carb_total1*4
    calcarb2 = carb_total2*4
    calpro1 = protein_total1*4
    calpro2 = protein_total2*4

    fatdif = calfat1-calfat2
    carbdif = calcarb1 - calcarb2
    prodif = calpro1 - calpro2
    caldif = calorie_total1 - calorie_total2

    calcol = "red"
    fatcol = "red"
    carbcol = "red"
    procol = "red"

    if caldif < 0:
        calcol = "green"
    if fatdif < 0:
        fatcol = "green"
    if carbdif < 0:
        carbcol = "green"
    if prodif < 0:
        procol = "green"

    fig = px.bar(x=["Calorie Difference", "Calories from Fat Difference", "Calories from Carbs Difference", "Calories from Protein Difference"], y=[
                 caldif, fatdif, carbdif, prodif], title="Nutrition Differences (Meal 1 - Meal 2)", labels={"x": "Nutrition Statistic", "y": "Difference"})
    fig.update_traces(marker_color=[calcol, fatcol, carbcol, procol])

    return fig


# RIGHT SIDE

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
    Input(component_id='feature', component_property='value'),
    Input(component_id='food-options', component_property='value')
)
def update_graph(input_brand, input_feature, food_choices):
    """
    This function generates a bar chart that visualizes the nutritional values of a given set of food items 
    from a specified brand. The nutritional value to be visualized can be chosen from either calories or 
    the three macronutrients (fat, carbohydrates, and protein).

    Inputs:
        - input_brand (string): the name of the brand for the food items
        - input_feature (string): the nutritional value to be visualized. Acceptable values are "Calories" or "Nutrients"
        - food_choices (list of strings): the names of the food items to be included in the chart

    Output:
        - fig (plotly bar chart object): a bar chart showing the nutritional values of the specified food items
    """
    filtered_df_item = df[df["brand_name"] == input_brand]
    if food_choices is None:
        food_choices = list(filtered_df_item['item_name'][0])

    filtered_df = filtered_df_item[filtered_df_item['item_name'].isin(
        food_choices)]

    if input_feature == "Calories":
        fig = px.bar(filtered_df, x="item_name", y="nf_calories", labels={
            "nf_calories": "Calories",
            "item_name": "Item"
        })

    elif input_feature == "Nutrients":
        fig = px.bar(filtered_df, x="item_name", y=["nf_total_fat", "nf_total_carbohydrate", "nf_protein"], barmode="group", labels={
            "item_name": "Item",
            "value": "Grams",
            "variable": "Nutrient",
            "nf_total_fat": "Fat"
        })
        newnames = {'nf_total_fat': 'Fat',
                    'nf_total_carbohydrate': 'Carbs', "nf_protein": "Protein"}
        fig.for_each_trace(lambda t: t.update(name=newnames[t.name],
                                              legendgroup=newnames[t.name],
                                              hovertemplate=t.hovertemplate.replace(
                                                  t.name, newnames[t.name])
                                              )
                           )

    fig.update_layout(transition_duration=400)
    return fig


@app.callback(
    Output(component_id='calorie-amount', component_property='children'),
    Output(component_id='daily-calories', component_property='children'),
    Output(component_id='fat-amount', component_property='children'),
    Output(component_id='daily-fats', component_property='children'),
    Output(component_id='satfat-amount', component_property='children'),
    Output(component_id='daily-satfat', component_property='children'),
    Output(component_id='tranfat-amount', component_property='children'),
    Output(component_id='chol-amount', component_property='children'),
    Output(component_id='daily-chol', component_property='children'),
    Output(component_id='sodium-amount', component_property='children'),
    Output(component_id='daily-sodium', component_property='children'),
    Output(component_id='carb-amount', component_property='children'),
    Output(component_id='daily-carb', component_property='children'),
    Output(component_id='fiber-amount', component_property='children'),
    Output(component_id='daily-fiber', component_property='children'),
    Output(component_id='sugar-amount', component_property='children'),
    Output(component_id='protein-amount', component_property='children'),
    Output(component_id='daily-protein', component_property='children'),
    Output(component_id='daily-A', component_property='children'),
    Output(component_id='daily-C', component_property='children'),
    Output(component_id='daily-calcium', component_property='children'),
    Output(component_id='daily-iron', component_property='children'),
    Input(component_id='my-brand', component_property='value'),
    Input(component_id='food-options', component_property='value')
)
def word_output(input_brand, food_choices):
    """
    This function calculates the nutritional values for a given set of food items from a specified brand and 
    returns the values as strings. The nutritional values include total calories, calories from fat, saturated fat, 
    trans fat, cholesterol, sodium, total carbohydrates, dietary fiber, sugars, and protein, as well as 
    percent daily values for vitamin A, vitamin C, calcium, and iron.

    Inputs:
        - input_brand (string): the name of the brand for the food items
        - food_choices (list of strings): the names of the food items to be included in the calculation

    Output:
        - calorie_total (string): total calories for the specified food items, in grams
        - calorie_dv (string): percent daily value for calories, based on a 2000 calorie diet
        - fat_total (string): total fat for the specified food items, in grams
        - fat_dv (string): percent daily value for fat, based on a 78 gram daily intake
        - satfat_total (string): total saturated fat for the specified food items, in grams
        - satfat_dv (string): percent daily value for saturated fat, based on a 20 gram daily intake
        - tranfat_total (string): total trans fat for the specified food items, in grams
        - chol_total (string): total cholesterol for the specified food items, in milligrams
        - chol_dv (string): percent daily value for cholesterol, based on a 300 milligram daily intake
        - sodium_total (string): total sodium for the specified food items, in milligrams
        - sodium_dv (string): percent daily value for sodium, based on a 2300 milligram daily intake
        - carb_total (string): total carbohydrates for the specified food items, in grams
        - carb_dv (string): percent daily value for carbohydrates, based on a 275 gram daily intake
        - fiber_total (string): total dietary fiber for the specified food items, in grams
        - fiber_dv (string): percent daily value for dietary fiber, based on a 28 gram daily intake
        - sugar_total (string): total sugars for the specified food items, in grams
        - protein_total (string): total protein for the specified food items, in grams
        - protein_dv (string): percent daily value for protein, based on a 50 gram daily intake
        - vitamin_a_dv (string): percent daily value for vitamin A
        - vitamin_c_dv (string): percent daily value for vitamin C
        - calcium_dv (string): percent daily value for calcium
        - iron_dv (string): percent daily value for iron
    """
    filtered_df_item = df[df["brand_name"] == input_brand]
    if food_choices is None:
        food_choices = list(filtered_df_item['item_name'][0])
    filtered_df = filtered_df_item[filtered_df_item['item_name'].isin(
        food_choices)]
    calorie_total = str(round(sum(filtered_df["nf_calories"]), 2))+"g"
    calorie_dv = str(round((sum(filtered_df["nf_calories"])/2000.0)*100))+"%"
    fat_total = str(round(sum(filtered_df["nf_total_fat"]), 2))+"g"
    fat_dv = str(round((sum(filtered_df["nf_total_fat"])/78.0)*100))+"%"
    satfat_total = str(round(sum(filtered_df["nf_saturated_fat"]), 2))+"g"
    satfat_dv = str(round((sum(filtered_df["nf_saturated_fat"])/20.0)*100))+"%"
    tranfat_total = str(round(sum(filtered_df["nf_trans_fatty_acid"]), 2))+"g"
    chol_total = str(round(sum(filtered_df["nf_cholesterol"]), 2))+"mg"
    chol_dv = str(round((sum(filtered_df["nf_cholesterol"])/300.0)*100))+"%"
    sodium_total = str(round(sum(filtered_df["nf_sodium"]), 2))+"mg"
    sodium_dv = str(round((sum(filtered_df["nf_sodium"])/2300.0)*100))+"%"
    carb_total = str(round(sum(filtered_df["nf_total_carbohydrate"]), 2))+"g"
    carb_dv = str(
        round((sum(filtered_df["nf_total_carbohydrate"])/275.0)*100))+"%"
    fiber_total = str(round(sum(filtered_df["nf_dietary_fiber"]), 2))+"g"
    fiber_dv = str(round((sum(filtered_df["nf_dietary_fiber"])/28.0)*100))+"%"
    sugar_total = str(round(sum(filtered_df["nf_sugars"]), 2))+"g"
    protein_total = str(round(sum(filtered_df["nf_protein"]), 2))+"g"
    protein_dv = str(round((sum(filtered_df["nf_protein"])/50.0)*100))+"%"

    vitamin_a_dv = str(sum(filtered_df["nf_vitamin_a_dv"]))+"%"
    vitamin_c_dv = str(sum(filtered_df["nf_vitamin_c_dv"]))+"%"
    calcium_dv = str(sum(filtered_df["nf_calcium_dv"]))+"%"
    iron_dv = str(sum(filtered_df["nf_iron_dv"]))+"%"

    if vitamin_a_dv == "nan%":
        vitamin_a_dv = "Data not avaliable"
    if vitamin_c_dv == "nan%":
        vitamin_c_dv = "Data not avaliable"
    if calcium_dv == "nan%":
        calcium_dv = "Data not avaliable"
    if iron_dv == "nan%":
        iron_dv = "Data not avaliable"

    for val in [vitamin_a_dv, vitamin_c_dv, calcium_dv, iron_dv]:
        if val == "nan%":
            val = "Data not avaliable"

    return calorie_total, calorie_dv, fat_total, fat_dv, satfat_total, satfat_dv, tranfat_total, chol_total, chol_dv, sodium_total, sodium_dv, carb_total, carb_dv, fiber_total, fiber_dv, sugar_total, protein_total, protein_dv, vitamin_a_dv, vitamin_c_dv, calcium_dv, iron_dv

# LEFT SIDE


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
    Input(component_id='feature2', component_property='value'),
    Input(component_id='food-options2', component_property='value')
)
def update_graph(input_brand, input_feature, food_choices):
    """
    This function generates a bar chart that visualizes the nutritional values of a given set of food items 
    from a specified brand. The nutritional value to be visualized can be chosen from either calories or 
    the three macronutrients (fat, carbohydrates, and protein).

    Inputs:
        - input_brand (string): the name of the brand for the food items
        - input_feature (string): the nutritional value to be visualized. Acceptable values are "Calories" or "Nutrients"
        - food_choices (list of strings): the names of the food items to be included in the chart

    Output:
        - fig (plotly bar chart object): a bar chart showing the nutritional values of the specified food items
    """
    filtered_df_item = df[df["brand_name"] == input_brand]
    if food_choices is None:
        food_choices = list(filtered_df_item['item_name'][0])

    filtered_df = filtered_df_item[filtered_df_item['item_name'].isin(
        food_choices)]

    if input_feature == "Calories":
        fig = px.bar(filtered_df, x="item_name", y="nf_calories", labels={
            "nf_calories": "Calories",
            "item_name": "Item"
        })

    elif input_feature == "Nutrients":
        fig = px.bar(filtered_df, x="item_name", y=["nf_total_fat", "nf_total_carbohydrate", "nf_protein"], barmode="group", labels={
            "item_name": "Item",
            "value": "Grams",
            "variable": "Nutrient",
            "nf_total_fat": "Fat"
        })
        newnames = {'nf_total_fat': 'Fat',
                    'nf_total_carbohydrate': 'Carbs', "nf_protein": "Protein"}
        fig.for_each_trace(lambda t: t.update(name=newnames[t.name],
                                              legendgroup=newnames[t.name],
                                              hovertemplate=t.hovertemplate.replace(
                                                  t.name, newnames[t.name])
                                              )
                           )

    fig.update_layout(transition_duration=400)
    return fig


@app.callback(
    Output(component_id='calorie-amount2', component_property='children'),
    Output(component_id='daily-calories2', component_property='children'),
    Output(component_id='fat-amount2', component_property='children'),
    Output(component_id='daily-fats2', component_property='children'),
    Output(component_id='satfat-amount2', component_property='children'),
    Output(component_id='daily-satfat2', component_property='children'),
    Output(component_id='tranfat-amount2', component_property='children'),
    Output(component_id='chol-amount2', component_property='children'),
    Output(component_id='daily-chol2', component_property='children'),
    Output(component_id='sodium-amount2', component_property='children'),
    Output(component_id='daily-sodium2', component_property='children'),
    Output(component_id='carb-amount2', component_property='children'),
    Output(component_id='daily-carb2', component_property='children'),
    Output(component_id='fiber-amount2', component_property='children'),
    Output(component_id='daily-fiber2', component_property='children'),
    Output(component_id='sugar-amount2', component_property='children'),
    Output(component_id='protein-amount2', component_property='children'),
    Output(component_id='daily-protein2', component_property='children'),
    Output(component_id='daily-A2', component_property='children'),
    Output(component_id='daily-C2', component_property='children'),
    Output(component_id='daily-calcium2', component_property='children'),
    Output(component_id='daily-iron2', component_property='children'),
    Input(component_id='my-brand2', component_property='value'),
    Input(component_id='food-options2', component_property='value')
)
def word_output(input_brand, food_choices):
    """
    This function calculates the nutritional values for a given set of food items from a specified brand and 
    returns the values as strings. The nutritional values include total calories, calories from fat, saturated fat, 
    trans fat, cholesterol, sodium, total carbohydrates, dietary fiber, sugars, and protein, as well as 
    percent daily values for vitamin A, vitamin C, calcium, and iron.

    Inputs:
        - input_brand (string): the name of the brand for the food items
        - food_choices (list of strings): the names of the food items to be included in the calculation

    Output:
        - calorie_total (string): total calories for the specified food items, in grams
        - calorie_dv (string): percent daily value for calories, based on a 2000 calorie diet
        - fat_total (string): total fat for the specified food items, in grams
        - fat_dv (string): percent daily value for fat, based on a 78 gram daily intake
        - satfat_total (string): total saturated fat for the specified food items, in grams
        - satfat_dv (string): percent daily value for saturated fat, based on a 20 gram daily intake
        - tranfat_total (string): total trans fat for the specified food items, in grams
        - chol_total (string): total cholesterol for the specified food items, in milligrams
        - chol_dv (string): percent daily value for cholesterol, based on a 300 milligram daily intake
        - sodium_total (string): total sodium for the specified food items, in milligrams
        - sodium_dv (string): percent daily value for sodium, based on a 2300 milligram daily intake
        - carb_total (string): total carbohydrates for the specified food items, in grams
        - carb_dv (string): percent daily value for carbohydrates, based on a 275 gram daily intake
        - fiber_total (string): total dietary fiber for the specified food items, in grams
        - fiber_dv (string): percent daily value for dietary fiber, based on a 28 gram daily intake
        - sugar_total (string): total sugars for the specified food items, in grams
        - protein_total (string): total protein for the specified food items, in grams
        - protein_dv (string): percent daily value for protein, based on a 50 gram daily intake
        - vitamin_a_dv (string): percent daily value for vitamin A
        - vitamin_c_dv (string): percent daily value for vitamin C
        - calcium_dv (string): percent daily value for calcium
        - iron_dv (string): percent daily value for iron
    """
    filtered_df_item = df[df["brand_name"] == input_brand]
    if food_choices is None:
        food_choices = list(filtered_df_item['item_name'][0])
    filtered_df = filtered_df_item[filtered_df_item['item_name'].isin(
        food_choices)]
    calorie_total = str(round(sum(filtered_df["nf_calories"]), 2))+"g"
    calorie_dv = str(round((sum(filtered_df["nf_calories"])/2000.0)*100))+"%"
    fat_total = str(round(sum(filtered_df["nf_total_fat"]), 2))+"g"
    fat_dv = str(round((sum(filtered_df["nf_total_fat"])/78.0)*100))+"%"
    satfat_total = str(round(sum(filtered_df["nf_saturated_fat"]), 2))+"g"
    satfat_dv = str(round((sum(filtered_df["nf_saturated_fat"])/20.0)*100))+"%"
    tranfat_total = str(round(sum(filtered_df["nf_trans_fatty_acid"]), 2))+"g"
    chol_total = str(round(sum(filtered_df["nf_cholesterol"]), 2))+"mg"
    chol_dv = str(round((sum(filtered_df["nf_cholesterol"])/300.0)*100))+"%"
    sodium_total = str(round(sum(filtered_df["nf_sodium"]), 2))+"mg"
    sodium_dv = str(round((sum(filtered_df["nf_sodium"])/2300.0)*100))+"%"
    carb_total = str(round(sum(filtered_df["nf_total_carbohydrate"]), 2))+"g"
    carb_dv = str(
        round((sum(filtered_df["nf_total_carbohydrate"])/275.0)*100))+"%"
    fiber_total = str(round(sum(filtered_df["nf_dietary_fiber"]), 2))+"g"
    fiber_dv = str(round((sum(filtered_df["nf_dietary_fiber"])/28.0)*100))+"%"
    sugar_total = str(round(sum(filtered_df["nf_sugars"]), 2))+"g"
    protein_total = str(round(sum(filtered_df["nf_protein"]), 2))+"g"
    protein_dv = str(round((sum(filtered_df["nf_protein"])/50.0)*100))+"%"

    vitamin_a_dv = str(sum(filtered_df["nf_vitamin_a_dv"]))+"%"
    vitamin_c_dv = str(sum(filtered_df["nf_vitamin_c_dv"]))+"%"
    calcium_dv = str(sum(filtered_df["nf_calcium_dv"]))+"%"
    iron_dv = str(sum(filtered_df["nf_iron_dv"]))+"%"

    if vitamin_a_dv == "nan%":
        vitamin_a_dv = "Data not avaliable"
    if vitamin_c_dv == "nan%":
        vitamin_c_dv = "Data not avaliable"
    if calcium_dv == "nan%":
        calcium_dv = "Data not avaliable"
    if iron_dv == "nan%":
        iron_dv = "Data not avaliable"

    return calorie_total, calorie_dv, fat_total, fat_dv, satfat_total, satfat_dv, tranfat_total, chol_total, chol_dv, sodium_total, sodium_dv, carb_total, carb_dv, fiber_total, fiber_dv, sugar_total, protein_total, protein_dv, vitamin_a_dv, vitamin_c_dv, calcium_dv, iron_dv


if __name__ == '__main__':
    app.run_server(debug=True)
