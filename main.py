import streamlit as st
import pandas as pd
from supabase import create_client, Client

# Initialize connection to db
@st.cache_resource
def init_connection():
    url: str = st.secrets['supabase_url']
    key: str = st.secrets['supabase_key']

    client: Client = create_client(url, key)

    return client

supabase = init_connection()

# Query the db
#@st.cache_data(ttl=600)  # cache clears after 10 minutes
def run_query():
    # Return all data
    return supabase.table('car_parts_monthly_sales').select("*").execute()

    # Filter data
    # return supabase.table('car_parts_monthly_sales').select("*").eq("parts_id", 2674).execute()


st.title("Query a database")
rows = run_query()
 
# Store in dataframe
df = pd.json_normalize(rows.data)
st.write(df)

def run_query_Filter():
    # Filter data
    return supabase.table('car_parts_monthly_sales').select("*").eq("parts_id", 2674).execute()

rows = run_query_Filter()
 
# Store in dataframe
df = pd.json_normalize(rows.data)
st.write(df)

# update data in databse
supabase.table("car_parts_monthly_sales").update({"volume": "100"}) .eq("id", 1).execute()

rows = run_query()

df = pd.json_normalize(rows.data)
st.write(df)

# insert data in databse
supabase.table("car_parts_monthly_sales") .insert({"id": 99999, "parts_id": 323412, "date": "4/8/2024", "volume": "109990"}).execute()
rows = run_query()

df = pd.json_normalize(rows.data)
st.write(df)