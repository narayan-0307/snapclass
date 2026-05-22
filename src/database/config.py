import streamlit as st
import os
from supabase import create_client, Client

# Try to get from Streamlit secrets first, fallback to environment variables
try:
    supabase_url = st.secrets["SUPABASE_URL"]
    supabase_key = st.secrets["SUPABASE_KEY"]
except (KeyError, FileNotFoundError):
    supabase_url = os.getenv("SUPABASE_URL")
    supabase_key = os.getenv("SUPABASE_KEY")

if not supabase_url or not supabase_key:
    raise ValueError("Supabase credentials not found. Please add them to Streamlit secrets or environment variables.")

supabase: Client = create_client(supabase_url, supabase_key)

