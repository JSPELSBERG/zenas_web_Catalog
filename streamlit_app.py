import streamlit as st
import snowflake.connector
from snowflake.snowpark.functions import col

# Write directly to the app
st.title("Zenas's Amazing Athleisure Catalog")
st.write(
    """Pick a sweatsuite color or style:"""
)
