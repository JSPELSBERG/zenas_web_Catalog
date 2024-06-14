import streamlit as st
import snowflake.connector
import pandas as pd
from snowflake.snowpark.functions import col

# Write directly to the app
st.title("Zenas's Amazing Athleisure Catalog")



my_cnx = snowflake.connector.connect(**st.secrets["snowflake"])
my_cur = my_cnx.cursor()

my_cur.execute("SELECT COLOR_OR_STYLE FROM CATALOG_FOR_WEBSITE")
my_catalog = my_cur.fetchall()

df = pd.DataFrame(my_catalog)
#st.write(df)
color_list = df[0].values.tolist()

option = st.selectbox('Pick a sweatsuite color or style:', list(color_list))

product_caption = 'Our warm, comforable, ' + option + 'sweatsuit!'
st.write(product_caption)

my_data_row = my_cur.fetchone()
