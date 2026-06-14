import requests
import streamlit as st

def get_weather(city):
    # Retrieve the key from Streamlit's secure storage
    api_key = st.secrets["	guuweather"]
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None

def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    if response.status_code == 200:
        return response.json()[0]
    return None