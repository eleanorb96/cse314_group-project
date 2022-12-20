# Progress Report #1 - CSE 314A
### Team: Bennett Hoshaw, Matthew DeSantis, John Yoo, and Eleanor Brock
---
#### Problem Domain / Statement
Our group is interested in studying the relationships between nutrition facts and source of the product (either by restaurant or brand). We plan to get our data from the Nutritionix API and various resources to find food pricing. We chose this project because we believe it lends itself well to prediction algorithms and has a impact on our everyday lives through our personal consumption choices. 

Given only certain information about some food items (for example, name and price, though which variables are the predictors and which we want to predict may vary upon experimentation with the actual data), can you predict some other criteria about the food with a high degree of accuracy? For example, can you predict the caloric content of a Taco Bell menu item from just its name and price? We could have multiple questions along these lines, with the team that creates the best performing model being the winner (using the Kaggle framework).

#### Scope
We aim to cover the following features in our project: 
- **Data Gathering via API** (1 feature): We plan to take advantage of the USDA’s FoodData Central API and Nutritionix API to gather nutrition facts about various food products.
- **Data Cleaning/Normalization & SQL/NoSQL Databases** (1 feature): Once the data has been collected, we will then need to normalize the data, use databases to manage its immense size, and account for any potential errors or missing values in the gathered data.
- **Data Visualization/Dashboarding** (1 feature): We plan to give the user the opportunity to compare various food products and restaurants. 

In all, this sums up to collecting the data effectively, cleaning, normalizing, and storing the data in an effective and sensible manner, and providing opportunities to visualize the items at play with this problem. 

#### Timeline
The first step would have to be using various APIs and other data sources to create tables for food nutrition facts and pricing information. We plan to dive into the nutrition APIs we have located and decide which variable to include and how to properly source the data. In addition, we will begin looking into ways to source the prices of the various items. We plan to store/manage the data with a database implementing either SQL or NoSQL, making this decision later once we have covered that topic. After the data is gathered, we will clean it and make sure it is tidy and easy to use. The next step would be forming some sort of data visualization to help contestants explore the data in an intuitive manner. Following this, we would perform basic, baseline analysis to set a par score for the contest. I imagine the data visualization would take the longest due to the sheer number of moving pieces and attributes of each item.

#### Anticipated Roadblocks
Because we would be pulling data from many different sources, it may be a challenge to get all of it into one, cohesive database. We plan to continue looking into various sources to get the data we hope to use in the project (especially the pricing data). The data visualization will likely also be challenging due to the large scope and number of attributes in the data. 

#### Kaggle Format
We would be using the Kaggle competition format for this project. The dataset will be the various food facts, and the baseline model would be something like a simple linear regression. Scoring would be based on model performance (we would use R^2 or something similar. There would also be preference for simpler models, when performance is similar).

