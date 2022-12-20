# BDD-style feature docs

## Title: Gathering nutrition data for analysis

### Narrative:

- As a: Data Scientist interested in researching the differences in nutrition facts between different restaurants and also interested in understand the predictive ability of various food attributions on the number of calories in a product
- I want: Up-to-date data from trusted sources
- So that: I can perform the analysis and feel confident in my findings.

### Scenario 1: Preparing the Data for Analysis

- Given: Interest in understanding how food characteristics affect the calories count present in a specific fast food product
- And: I know potential sources to retrieve the data from
- When: The data is called for and collected
- Then: I can begin cleaning the data and working through the data science process.

### Scenario 2: Updating the Foods Present in my Database

- Given: Interest in collecting nutrition data on fast food products
- And: I have an understanding of how to use the USDA’s FoodData Central API and NurtirionIX API
- When: I want to collect and update the data
- Then: The API will quickly provide me with new products that have been added to their database that I can incorporate into my analysis.

## Title: Data Cleaning/Normalization

### Narrative:

- As a: Data scientist attempting to prepare the collected API data for analysis
- I want: The data to be cleaned/normalized in a fashion that easily allows me to select products based on brand and name
- So that: The data is immediately consistent and easy to work with.

### Scenario 1: Preparing the NutritionIX API Raw Data

- Given: Data from the NurtitionIX API based on a specific query such as a brand name (restaurant name)
- And: An interest in selecting specific restaurants and specific foods
- When: Data cleaning/normalization techniques are applied
- Then: I can easily retrieve information about my requested item in a timely fashion and in a clean and consistent manner.

## Title: Understanding Nutrition Trends at Fast Food Restaurants (Data Aggregation)

### Narrative:

- As a: Nutritionist interested in understanding nutrition trends of a particular type of product or restaurant
- I want: Aggregated data
- So that: I can gain an understanding of the nutritional value of a particular restaurant or product type.

### Scenario 1: Understanding a Restaurant’s Nutritional Value

- Given: Food data from a particular restaurant
- And: The ability to aggregate the data based on food type (burger, drink, etc.)
- When: I call for a particular statistic
- Then: I will gain an understanding of the average nutritional value of that food type at the restaurant.

## Title: Data Visualization/Dashboarding

### Narrative:

- As a: Data scientist looking to visualize and compare the nutrition facts of restaurants and particular products
- I want: The ability to select the restaurants/products displayed and the specific statistics requested in a side-by-side manner
- So that: I can accurately make a visual comparison between two restaurant/products.

### Scenario 1: Create Comparisons Between Individual Products at Two Restuarants

- Given: A dashboard with the capability to select two restaurants
- And: The ability to select specific attributes about each restaurant (average calories, average fats, etc.)
- And: The Dashboard is configured to provide me with a side-by-side display of the requested features
- When: I make my selection
- Then: I will receive an easy to read and analyze visual display that is conducive to understanding more about each product and how they compare.
- For Example: Nutrition Facts about a cheeseburger from McDonalds and a cheeseburger from Burger King.

### Scenario 2: Create Comparisons Between Two Products at a Given Restaurant

- Given: A dashboard with the capability to select multiple products from one restaurant
- And: The ability to select specific nutrition facts
- And: The Dashboard is configured to provide me with a side-by-side display of the requested items
- When: I make my food selections
- Then: I will receive an easy to read and analyze visual display that is conducive to understanding more about each product and how they compare.
- For Example: Nutrition Facts about a cheeseburger and double cheeseburger from McDonalds.
