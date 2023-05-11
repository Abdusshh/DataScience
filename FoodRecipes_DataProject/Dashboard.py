# import the necessary libraries
import pandas as pd
import streamlit as st
import plotly.express as px

st.set_page_config(page_title='Food Recipe Dashboard',
                   page_icon=":shallow_pan_of_food:",
                   layout='wide')

# import the necessary files
import Research as rs

# ---- MAINPAGE ----
st.title("Food Recipes Dashboard")
st.markdown("# :spaghetti: :doughnut: :hamburger: :falafel: :pancakes: :dumpling: :stew: :pizza: :sushi: :cookie: :fried_shrimp: :waffle: :taco: :burrito: :ramen: :poultry_leg: :croissant: :pie: :curry:")
st.markdown("###")
st.write("The purpose of this dashboard is to create meaningful applications from the [Food Recipes](https://www.kaggle.com/datasets/sarthak71/food-recipes) dataset while conducting a research on the dataset. The dashboard is divided into 4 sections: **Get Your Recipe of Choice**, **Introduction**, **Research Questions**, and **Research Results**. The **Get Your Recipe of Choice** section allows the user to get a random recipe based on the cuisine, diet, or ingredients. The **Introduction** section provides a brief introduction to the dashboard and the dataset. The **Research Questions** section provides the research questions that will be answered using the dataset. The **Research Results** section provides the results of the research questions.")
st.markdown("###")
st.write("---")


# ---- TABLE OF CONTENTS ----
st.sidebar.title("Table of Contents 📚 ")
st.sidebar.markdown("###")
st.sidebar.write("---")
st.sidebar.markdown("#### [Get Your Recipe of Choice](#get_recipes) :open_book:")
st.sidebar.markdown("#### [Research Introduction](#introduction) 🔍")
st.sidebar.markdown("#### [Research Questions](#research) :memo:")
st.sidebar.markdown("#### [Research Results](#research_results) :bar_chart:")
st.sidebar.write("---")


# ---- GET RECIPES ----
st.markdown("## Get Your Recipe of Choice <a name='get_recipes'></a>", unsafe_allow_html=True)
st.markdown("###")

# 5 random recipes depending on the cuisine
st.markdown("#### Enter a cuisine to get recipes:")
cuisine_input = st.text_input("", key="cuisine")
cuisine_output = rs.get_random_cuisine_recipes(cuisine_input)
st.write(cuisine_output)
st.markdown("###")

# 5 random recipes depending on the diet
st.markdown("#### Enter a diet to get recipes:")
options = rs.df['diet'].unique()
diet_input = st.selectbox("", options)
diet_output = rs.get_random_diet_recipes(diet_input)
st.write(diet_output)
st.markdown("###")

# Recipe based on the given ingredients
st.markdown("#### Enter ingredients to get a recipe that uses these ingredients:")
ingredient_input = st.text_input("", key="ingredient")
ingredient_output = rs.get_recipes_with_ingredients(ingredient_input)
st.write(ingredient_output)
st.markdown("###")

# Recipe search
st.markdown("#### Enter a recipe to search for:")
search_input = st.text_input("", key="search")
search_output = rs.get_recipe_info(search_input)
st.write(search_output)
st.markdown("###")

st.write("---")


# ---- INTRODUCTION ----
st.markdown("## Research Introduction <a name='introduction'></a>", unsafe_allow_html=True)
st.markdown("###")
st.markdown("#### What is the purpose of this research?")
st.write("""The purpose of this research is to provide a visual representation of the data collected from the Food Recipes dataset. The data is presented in a way that is easy to understand and interpret, and can be used to answer questions about the dataset.""")
st.markdown("###")

st.markdown("#### What is the data source?")
st.write(f"""The data used in this dashboard was collected from the [Food Recipes](https://www.kaggle.com/datasets/sarthak71/food-recipes) dataset, which is available on Kaggle. The dataset contains information about the ingredients, cooking time, and ratings of over 8,000 recipes from around the world. The data was collected by scraping the Allrecipes website, and is available for download on Kaggle.""")
st.markdown("###")

st.write("---")


# ---- RESERACH ----
st.markdown("## Research Questions <a name='research'></a>", unsafe_allow_html=True)
st.markdown("###")
st.markdown("##### [1. Which cuisines receive the highest ratings?](#cuisine_rating)")
st.markdown("##### [2. Which cuisines require the longest cooking time?](#cuisine_time)")
st.markdown("##### [3. Which diets receive the highest ratings?](#diet_rating)")
st.markdown("##### [4. Which diets require the longest cooking time?](#diet_time)")
st.markdown("###")

st.markdown("### 1. Which cuisines receive the highest ratings? <a name='cuisine_rating'></a>", unsafe_allow_html=True)
st.bokeh_chart(rs.fig_cuisine_rating, use_container_width=True)
st.markdown("###")

st.markdown("### 2. Which cuisines require the longest cooking time? <a name='cuisine_time'></a>", unsafe_allow_html=True)
st.bokeh_chart(rs.fig_cuisine_time, use_container_width=True)
st.markdown("###")


col1, col2 = st.columns(2)

with col1:
    st.markdown("### 3. Which diets receive the highest ratings? <a name='diet_rating'></a>", unsafe_allow_html=True)
    st.bokeh_chart(rs.fig_diet_rating, use_container_width=True)

with col2:
    st.markdown("### 4. Which diets require the longest cooking time? <a name='diet_time'></a>", unsafe_allow_html=True)
    st.bokeh_chart(rs.fig_diet_time, use_container_width=True)
st.markdown("###")

st.write("---")


# ---- RESEARCH RESULTS ----
st.markdown("## Research Results <a name='research_results'></a>", unsafe_allow_html=True)
st.markdown("###")

st.markdown("### Are there any correlations between cooking time and ratings of cuisines or diets?")
st.write("Based on the research on cuisines and diets, the findings suggest that there is no significant correlation between cooking time and rating. This indicates that the length of time it takes to cook a dish is not a determining factor in how well it is rated. Other factors, such as the quality of ingredients, cooking technique, and personal taste preferences, may play a more significant role in determining how well a dish is received. It's important to consider these factors when evaluating the success of a cuisine or diet and to focus on creating dishes that appeal to a broad range of tastes and preferences.")
st.markdown("###")

st.markdown("### Why is average rating of cuisines and diets important?")
st.write("""The average user rating of certain cuisines or diets is another important piece of data that can be incredibly useful for those interested in exploring new flavors and cuisines. By knowing the average rating of different cuisines or diets, you can get a sense of which dishes are particularly popular and highly regarded by others. This can help you identify recipes that are likely to be delicious, and that will appeal to your own personal tastes and preferences. 
        \n Additionally, the average user rating of certain cuisines or diets can help you discover new recipes and dishes that you may not have otherwise considered. By looking for highly rated recipes in a particular cuisine or diet, you can expand your culinary horizons and explore new flavors and ingredients that you may not have tried before. 
        \n Another important benefit of knowing the average user rating of certain cuisines or diets is that it can help you avoid recipes that are likely to be disappointing or not worth your time and effort. By looking for recipes with high ratings, you can be more confident that you are investing your time and resources into a dish that is likely to be delicious and well-received by your family and friends. 
        \n In conclusion, the average user rating of certain cuisines or diets is a valuable piece of data that can help you discover new recipes, explore new flavors, and avoid recipes that are likely to be disappointing. Whether you are a seasoned cook or a novice in the kitchen, this data can help you make the most of your culinary adventures and ensure that every meal you prepare is delicious and satisfying.""")
st.markdown("###")

st.markdown("### Why is average cooking time of diets and cuisines important?")
st.write("""The data on the average preparation times of different cuisines and diets is a valuable resource for anyone who is interested in exploring new flavors, managing their time effectively, and making healthy and delicious meals. This data can help you plan your meals with ease, and ensure that you have enough time to prepare your food while adhering to your dietary needs. 
         \n One of the most significant advantages of this data is that it helps you understand the level of difficulty associated with preparing dishes from different cuisines and diets. This can be especially helpful for those who are new to a particular cuisine or diet, as it can help them identify dishes that are easier to prepare and gradually work their way up to more complex recipes. Additionally, knowing the average preparation time of different cuisines and diets can help you identify recipes that can be prepared quickly, without compromising on flavor or nutrition. 
         \n Another important benefit of this data is that it can help you explore new cuisines and flavors with ease. By identifying recipes with shorter preparation times, you can start experimenting with new ingredients and techniques, without feeling overwhelmed or intimidated by the process. This can be particularly useful for those who are looking to expand their culinary horizons, but may not have a lot of time to spend in the kitchen. 
         \n In conclusion, the data on the average preparation times of different cuisines and diets is a valuable tool for anyone who is interested in making healthy and delicious meals while managing their time effectively. This data can help you plan your meals, explore new cuisines and flavors, and ensure that you are making the most of your time in the kitchen.""")
st.markdown("###")
