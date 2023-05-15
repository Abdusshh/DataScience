import pandas as pd

path = "FoodRecipes_DataProject/food_recipes.csv"
df = pd.read_csv(path)
df.head()


# Let's see the different types of record_healt column
df["record_health"].groupby(df["record_health"]).count()
# All of them are good, so we can drop this column

# Prep time and cook time are better off as sum of the two as total time so let's also drop them

new_df = df.drop(
    ["url", "record_health", "author", "tags", "category", "prep_time", "cook_time"],
    axis="columns",
)
new_df.head()

# 1. count the number of NaN values in time columns
num_nan = df["prep_time"].isna().sum()
print(num_nan)

# 2. for now replace the NaN values in time columns with 0
df["prep_time"] = df["prep_time"].fillna(0)
df["cook_time"] = df["cook_time"].fillna(0)

print(df["prep_time"].dtypes)
print(df["cook_time"].dtypes)

# 3. convert the datatype of prep_time and cook_time from object to str
df["prep_time"] = df["prep_time"].astype(str)
df["cook_time"] = df["cook_time"].astype(str)

# 4. convert the datatype of prep_time and cook_time to int and extract the numbers from the string
new_df["prep_time"] = df["prep_time"].str.extract("(\d+)").astype(int)
new_df["cook_time"] = df["cook_time"].str.extract("(\d+)").astype(int)

print(new_df["prep_time"].mean())

# 5. change the 0 values in prep_time and cook_time to mean of the column
new_df["prep_time"] = new_df["prep_time"].replace(0, new_df["prep_time"].mean())
new_df["cook_time"] = new_df["cook_time"].replace(0, new_df["cook_time"].mean())

# 6. add a new column total_time
new_df["total_time"] = (new_df["prep_time"] + new_df["cook_time"]).astype(int)

# 7. drop the prep_time and cook_time columns
new_df = new_df.drop(["prep_time", "cook_time"], axis="columns")

new_df.head()

# Let's check the total_time column for any absurd values
new_df["total_time"].describe()

# Let's find the super high and low values
new_df.loc[new_df["total_time"] > 800]
new_df.loc[new_df["total_time"] < 5]

# Let's see some of the instructions for the super high and low values
# new_df.loc[6207, 'instructions']

# Since we have only one Swedish dish and it breaks our data, let's drop it
new_df = new_df.drop([6207], axis="rows")

# There is an error in this Nepalese dish
new_df.loc[4917, "total_time"] = new_df["total_time"].mean()
new_df.loc[new_df["cuisine"] == "Nepalese"]

# Convert the total_time column to int
new_df["total_time"] = new_df["total_time"].astype(int)


# Save the cleaned data to a new csv file
# new_df.to_csv('cleaned_food_recipes.csv', index=False)

from bokeh.plotting import figure, show
from bokeh.io import output_notebook
from bokeh.models import ColumnDataSource, HoverTool
from bokeh.palettes import Category20c
from bokeh.transform import factor_cmap
from bokeh.palettes import Turbo256

current_df = pd.read_csv("FoodRecipes_DataProject/cleaned_food_recipes.csv")

# 1. group the dataframe by cuisine
grouped_df = current_df.groupby("cuisine")
grouped_df.head()

# 2. find the average of total_time for every cuisine
avg_time = grouped_df["total_time"].mean().round()
print(avg_time)

# 3. sort the values in descending order
avg_time = avg_time.sort_values(ascending=False)

output_notebook()

# Visualize the data using Bokeh
# create a ColumnDataSource object
source = ColumnDataSource(avg_time.to_frame())

# create a figure object
fig_cuisine_time = figure(
    x_range=avg_time.index.values,
    height=500,
    width=1500,
    title="Average time taken to cook every cuisine",
)


# add axis labels
fig_cuisine_time.xaxis.axis_label = "Cuisine"
fig_cuisine_time.yaxis.axis_label = "Average time taken to cook (in minutes)"

# create a palette of colors because we have many cuisines we use Turbo256
my_palette = Turbo256[::3]

# create a bar chart
fig_cuisine_time.vbar(
    x="cuisine",
    top="total_time",
    width=0.9,
    source=source,
    line_color="white",
    fill_color=factor_cmap(
        "cuisine", palette=my_palette, factors=avg_time.index.values
    ),
)

# set the y axis range
fig_cuisine_time.y_range.start = 0

# set the x axis labels to appear at 45 degree angle
fig_cuisine_time.xaxis.major_label_orientation = 1

# add a hover tool
fig_cuisine_time.add_tools(
    HoverTool(
        tooltips=[
            ("Cuisine", "@cuisine"),
            ("Average time taken to cook", "@total_time"),
        ]
    )
)

# show the plot
show(fig_cuisine_time)


# 1. group the dataframe by diet
grouped_df_diet = current_df.groupby("diet")
grouped_df_diet.head()

# 2. find the average of total_time for every diet
avg_time_diet = grouped_df_diet["total_time"].mean().round(2)
print(avg_time_diet)

# 3. sort the values in descending order
avg_time_diet = avg_time_diet.sort_values(ascending=False)

output_notebook()

# create a ColumnDataSource object
source = ColumnDataSource(avg_time_diet.to_frame())

# create a figure object
fig_diet_time = figure(
    x_range=avg_time_diet.index.values,
    height=500,
    width=750,
    title="Average time taken to cook every diet",
)

# add axis labels
fig_diet_time.xaxis.axis_label = "Diet"
fig_diet_time.yaxis.axis_label = "Average time taken to cook (in minutes)"

# create a palette of colors because we have less than 20 diets we use Category20c
my_palette = Category20c[20]

# create a bar chart
fig_diet_time.vbar(
    x="diet",
    top="total_time",
    width=0.9,
    source=source,
    line_color="white",
    fill_color=factor_cmap(
        "diet", palette=my_palette, factors=avg_time_diet.index.values
    ),
)

# set the y axis range
fig_diet_time.y_range.start = 0

# set the x axis labels to appear at 45 degree angle
fig_diet_time.xaxis.major_label_orientation = 1

# add a hover tool
fig_diet_time.add_tools(
    HoverTool(
        tooltips=[("Diet", "@diet"), ("Average time taken to cook", "@total_time")]
    )
)

# show the plot
show(fig_diet_time)

# 0. multiply ratings by 20 only once to scale it between 0 and 100
mid_df = current_df.copy()

mid_df["rating"] = current_df["rating"] * 20

# 1. group the dataframe by cuisine
grouped_df_likes = mid_df.groupby("cuisine")
grouped_df_likes.head()

# 2. find the average rating for every cuisine
avg_likes = grouped_df_likes["rating"].mean()
print(avg_likes)

# 3. sort the values in descending order
avg_likes = avg_likes.sort_values(ascending=False)

output_notebook()

# create a ColumnDataSource object
source = ColumnDataSource(avg_likes.to_frame())

# create a figure object
fig_cuisine_rating = figure(
    x_range=avg_likes.index.values,
    height=500,
    width=1500,
    title="Average rating of every cuisine",
)

# add axis labels
fig_cuisine_rating.xaxis.axis_label = "Cuisine"
fig_cuisine_rating.yaxis.axis_label = "Average rating"

# create a palette of colors because we have many cuisines we use Turbo256
my_palette = Turbo256[::3]

# create a bar chart
fig_cuisine_rating.vbar(
    x="cuisine",
    top="rating",
    width=0.9,
    source=source,
    line_color="white",
    fill_color=factor_cmap(
        "cuisine", palette=my_palette, factors=avg_likes.index.values
    ),
)

# set the y axis range
fig_cuisine_rating.y_range.start = 90

# set the x axis labels to appear at 45 degree angle
fig_cuisine_rating.xaxis.major_label_orientation = 1

# add a hover tool
fig_cuisine_rating.add_tools(
    HoverTool(tooltips=[("Cuisine", "@cuisine"), ("Average rating", "@rating")])
)

# show the plot
show(fig_cuisine_rating)

# 1. group the dataframe by diet
grouped_df_likes_diet = mid_df.groupby("diet")
grouped_df_likes_diet.head()

# 2. find the average rating for every diet
avg_likes_diet = grouped_df_likes_diet["rating"].mean()
print(avg_likes_diet)

# 3. sort the values in descending order
avg_likes_diet = avg_likes_diet.sort_values(ascending=False)

output_notebook()

# create a ColumnDataSource object
source = ColumnDataSource(avg_likes_diet.to_frame())

# create a figure object
fig_diet_rating = figure(
    x_range=avg_likes_diet.index.values,
    height=500,
    width=750,
    title="Average rating of every diet",
)

# add axis labels
fig_diet_rating.xaxis.axis_label = "Diet"
fig_diet_rating.yaxis.axis_label = "Average rating"

# create a palette of colors because we have less than 20 diets we use Category20c
my_palette = Category20c[20]

# create a bar chart
fig_diet_rating.vbar(
    x="diet",
    top="rating",
    width=0.9,
    source=source,
    line_color="white",
    fill_color=factor_cmap(
        "diet", palette=my_palette, factors=avg_likes_diet.index.values
    ),
)

# set the y axis range
fig_diet_rating.y_range.start = 97

# set the x axis labels to appear at 45 degree angle
fig_diet_rating.xaxis.major_label_orientation = 1

# add a hover tool
fig_diet_rating.add_tools(
    HoverTool(tooltips=[("Diet", "@diet"), ("Average rating", "@rating")])
)

# show the plot
show(fig_diet_rating)

# import the necessary libraries
from bokeh.io import show
from bokeh.layouts import row, column
from bokeh.io import curdoc

# create a dashboard layout
layout = row(
    column(fig_cuisine_time, fig_cuisine_rating, row(fig_diet_time, fig_diet_rating))
)

# add the layout to curdoc
curdoc().add_root(layout)

# Show the dashboard
show(layout)


df = pd.read_csv("cleaned_food_recipes.csv")

df.head()


# Find all nan values in the ingredients column
# print(df[df['ingredients'].isnull()])

# We'll need to replace the nan values with an empty string
df["ingredients"] = df["ingredients"].fillna("")


def get_recipes_with_ingredients(ingredients):
    # if len(ingredients) == 0, then the user didn't enter any ingredients
    if len(ingredients) == 0:
        return "You didn't enter any ingredients!"

    # We'll get a list of all the recipes that contain each ingredient
    recipes = []
    for ingredient in ingredients.split(" "):
        # convert the ingredient to lowercase
        ingredient = ingredient.lower()
        # strip the ingredient of any leading or trailing spaces
        ingredient = ingredient.strip()
        # make ingredients column lowercase
        df["ingredients"] = df["ingredients"].str.lower()

        # print(df[df['ingredients'].str.contains(ingredient)]['recipe_title'].tolist())
        recipes.append(
            df[df["ingredients"].str.contains(ingredient)]["recipe_title"].tolist()
        )

    # We'll find the intersection of all the lists
    recipes = set(recipes[0]).intersection(*recipes)

    return recipes

# Let's try it out
get_recipes_with_ingredients("Oil Salt Meat")


# random module will be used to generate a random number
import random

# print(df[df['diet'].isnull()])

# We'll need to replace the nan values with an Unknown string
df["diet"] = df["diet"].fillna("Unknown")

# Let's change the No Onion No Garlic (Sattvic) diet to No Onion No Garlic
df["diet"] = df["diet"].replace("No Onion No Garlic (Sattvic)", "No Onion No Garlic")

def get_random_diet_recipes(diet, n=5):
    # if the diet is not in diets column, we'll return "Sorry, we don't have any recipes for the given diet"
    if diet not in df["diet"].unique():
        return "Sorry, we don't have any recipes for the given diet!"

    # We'll get a list of all the recipes that contain each ingredient
    recipes = df[df["diet"].str.contains(diet)]["recipe_title"].tolist()

    # If the number of recipes is less than n, we'll return all the recipes
    if len(recipes) < n:
        return recipes

    # We'll return n random recipes
    return random.sample(recipes, n)


# Let's try it out
get_random_diet_recipes("Vegetarian")



# Find all nan values in the diet column
# print(df[df['cuisine'].isnull()])

# We'll need to replace the nan values with an Unknown string
df["cuisine"] = df["cuisine"].fillna("Unknown")


def get_random_cuisine_recipes(cuisine, n=5):
    # strip the cuisine of any leading or trailing spaces
    cuisine = cuisine.strip()

    # strip the cuisine of any leading or trailing " or ' characters
    cuisine = cuisine.strip('"')
    cuisine = cuisine.strip("'")

    # Capitalize the cuisine
    cuisine = cuisine.capitalize()

    # if the cuisine is not in cuisines column, we'll return "Sorry, we don't have any recipes for the given cuisine"
    if len(cuisine) == 0:
        return "Sorry, we don't have any recipes for the given cuisine!"

    # We'll get a list of all the recipes that contain each ingredient
    recipes = df[df["cuisine"].str.contains(cuisine)]["recipe_title"].tolist()

    # If the number of recipes is less than n, we'll return all the recipes
    if len(recipes) < n:
        return recipes

    # We'll return n random recipes
    return random.sample(recipes, n)


# Let's try it out
get_random_cuisine_recipes("Mediterranean")
# Get recipe explanation and ingredients based on recipe name
# Let's write a function that will take in a neme of a recipe and return ingredients, total_time, diet, cuisine, course and instructions


def get_recipe_info(recipe_name):

    # strip the recipe_name of any leading or trailing spaces
    recipe_name = recipe_name.strip()

    # strip the recipe_name of any leading or trailing " or ' characters
    recipe_name = recipe_name.strip('"')
    recipe_name = recipe_name.strip("'")

    # if the recipe_name is not in recipe_title column, we'll return "Sorry, we don't have any recipes for the given recipe name"
    if recipe_name not in df["recipe_title"].unique():
        return "Sorry, we don't have any recipes for the given recipe name!"

    # We'll find the row that is the recipe name using loc
    recipe = df.loc[df["recipe_title"].str.contains(recipe_name)]

    # We'll print out the information
    # print('Cuisine:', recipe['cuisine'].values[0])
    # print('Course:', recipe['course'].values[0])
    # print('Diet:', recipe['diet'].values[0])
    # print('Ingredients:', recipe['ingredients'].values[0])
    # print('Instructions:', recipe['instructions'].values[0])
    # print('Total Preparation Time:', recipe['total_time'].values[0])

    recipe = recipe[
        ["cuisine", "course", "diet", "ingredients", "instructions", "total_time"]
    ]

    # We'll return the recipe as a dictionary
    recipe = recipe.to_dict(orient="records")

    return recipe


# Let's try it out
get_recipe_info("Tzatziki Recipe")

