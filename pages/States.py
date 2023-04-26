import numpy as np
import pandas as pd
import requests
import streamlit as st
import altair as alt

st.markdown(
    """
    <style>
        [data-testid="stSidebarNav"]::before {
            content: "News API";
            margin-left: 20px;
            margin-top: 20px;
            font-size: 30px;
            position: relative;
            top: 20px;
        }
    </style>
    """,
    unsafe_allow_html=True,
)


# Set up API key and categories
apiKey = "0a54baab3c394337aa46d1ea286cfb24"
categories = ['technology', 'politics', 'sports', 'business',
              'entertainment', 'health', 'general']

# Define function to get sources for a given category
def get_sources(category):
    finalURL = f"https://newsapi.org/v2/top-headlines?country=us&category={category}" \
           f"&apiKey={apiKey}"
    r = requests.get(finalURL).json()
    articles = r['articles']
    sources = [article['source']['name'] for article in articles]
    return sources


# Get sources for all categories and combine into a single list
sources = []
for category in categories:
    sources += get_sources(category)

# Count sources and create chart
source_count = {}
for word in sources:
    if word in source_count:
        source_count[word] += 1
    else:
        source_count[word] = 1

df = pd.DataFrame({
    "Sources": list(source_count.keys()),
    "Number of Articles": list(source_count.values())
})

bar_chart = alt.Chart(df).mark_bar().encode(
    x="Sources:O",
    y="Number of Articles:Q",
)

st.altair_chart(bar_chart, use_container_width=True)

# Create data frame for article sources per category
data = {}
for category in categories:
    data[category.title()] = get_sources(category)

df = pd.DataFrame(data)

# Display data frame and allow user to resize it
st.checkbox("Use container width", value=False, key="use_container_width")
st.dataframe(df, use_container_width=st.session_state.use_container_width)
