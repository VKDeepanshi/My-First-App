import streamlit as st
from api_utils import get_weather, get_quote

st.set_page_config(page_title="Life-Sync Hub", layout="wide")

st.title("☀️ Life-Sync Hub")

# Sidebar for controls
city = st.sidebar.text_input("Enter your city", "Ghaziabad")

# Main display area
col1, col2 = st.columns(2)

with col1:
    st.subheader("Weather Update")
    if st.button("Check Weather"):
        data = get_weather(city)
        if data:
            st.metric("Temperature", f"{data['main']['temp']}°C")
            st.write(f"Condition: {data['weather'][0]['description']}")
        else:
            st.error("Could not fetch weather. Check your API Key.")

with col2:
    st.subheader("Daily Motivation")
    quote_data = get_quote()
    if quote_data:
        st.info(f"'{quote_data['q']}' \n\n— *{quote_data['a']}*")

st.divider()
st.subheader("Quick Tasks")
if "tasks" not in st.session_state:
    st.session_state.tasks = []

new_task = st.text_input("Add a new task")
if st.button("Add Task"):
    st.session_state.tasks.append(new_task)

for i, task in enumerate(st.session_state.tasks):
    st.write(f"{i+1}. {task}")