import streamlit as st
import requests
import pandas as pd
from snowflake.snowpark.functions import col

# Write directly to the app
st.title("Zenas's Amazing Athleisure Catalog")
st.write(
    """Pick a sweatsuite color or style:"""
)
