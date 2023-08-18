import streamlit

streamlit.title('My Parents new Health Dinner')

streamlit.header('Breakfast Menu')

streamlit.text(' 🥣 Omega 3 & Blueberry Omlet')
streamlit.text(' 🥗 Kale, Spinach and Rocket Smoothie')
streamlit.text(' 🐔 Hard-Boiled free range Eggs')
streamlit.text(' 🥑🍞Avocado Toast')

streamlit.header('Indian Breakfast Menu')

streamlit.text('Idly(2) , Peanut chutney and Sambar')
streamlit.text('Puri(3) and Allo kurma')
streamlit.text('Pesaretu and upuma with chutney')


streamlit.header('Build your own smoothie')
import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado','Strawberries'])

fruits_to_show = my_fruit_list.loc[fruits_selected]

# Display the table on the page.
streamlit.dataframe(fruits_to_show)

streamlit.header("Fruityvice Fruit Advice!")
import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + "Kiwi")
#streamlit.text(fruityvice_response.json())

# store in json format of fruit details? 
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())

# storing data in columnar format usinf the dataframe?
streamlit.dataframe(fruityvice_normalized)



