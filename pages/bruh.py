import streamlit as st
import requests
import pandas as pd
import pydeck as pdk
import json

# Define the API URL and API key
api_url = "https://newsapi.org/v2/everything"
api_key = "8d40a72404ec4f20bc701b1afb95c89e"
f = open('states.json')

states = json.load(f)


# Define a function to get the number of articles for a state
def get_num_articles(state):
    # Make a request to the News API for the given state
    url = f"{api_url}?q={state}&sortBy=relevancy&apiKey={api_key}"
    response = requests.get(url).json()

    # Get the total number of results from the response
    total_results = response["totalResults"]

    return total_results


# Create a DataFrame of the state data
state_data = pd.DataFrame(states)

# Add a column for the number of articles for each state
state_data["num_articles"] = state_data["state"].apply(get_num_articles)

# Define the PyDeck layer for the map
layer = pdk.Layer(
    "ScatterplotLayer",
    state_data,
    get_position=["longitude", "latitude"],
    get_radius="num_articles",
    get_fill_color=[255, 0, 0, 255],
    pickable=True,
    auto_highlight=True,
)

# Define the PyDeck view for the map
view_state = pdk.ViewState(
    longitude=-96,
    latitude=37.5,
    zoom=3,
    min_zoom=3,
    max_zoom=15,
)

# Render the map with Streamlit
st.pydeck_chart(pdk.Deck(
    layers=[layer],
    initial_view_state=view_state,
    tooltip={"text": "{state}: {num_articles} articles"},
))
