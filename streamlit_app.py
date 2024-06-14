import streamlit as st
import snowflake.connector
import pandas as pd
#from snowflake.snowpark.functions import col

# Write directly to the app
st.title("Zenas's Amazing Athleisure Catalog")

my_cnx = snowflake.connector.connect(**st.secrets["snowflake"])
my_cur = my_cnx.cursor()

my_cur.execute("SELECT COLOR_OR_STYLE,  FROM CATALOG_FOR_WEBSITE")
my_catalog = my_cur.fetchall()

df = pd.DataFrame(my_catalog)
#st.write(df)
color_list = df[0].values.tolist()
print(color_list)

coloroption = st.selectbox('Pick a sweatsuite color or style:', list(color_list))
#sizeoption = st.selectbox('Pick a sweatsuite color or style:', list(size_list))

product_caption = 'Our warm, comforable, ' + coloroption + 'sweatsuit!'
st.write(product_caption)

#my_data_row = my_cur.fetchone()

my_cur.execute("select direct_url, price, size_list, upsell_product_desc from catalog_for_website where color_or_style = '" + coloroption + "';")
df2 = my_cur.fetchone()
st.image(
df2[0],
width=400,
caption= product_caption
)
st.write('Price: ', df2[1])
st.write('Sizes Available: ',df2[2])
st.write(df2[3])
