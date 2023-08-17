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
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado','Strawberries'])

# Display the table on the page.
streamlit.dataframe(my_fruit_list)





