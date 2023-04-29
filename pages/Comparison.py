import numpy as np
import pandas as pd
import requests
import streamlit as st
import altair as alt
import sys
import json

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

apiKey = '7e11b8f6cbf740f69e253605a9b4eea0'

st.title("How many Articles had these topics mentioned in there date")
country = "us"
if country:
    finalURL = f"https://newsapi.org/v2/top-headlines?country={country}&apiKey={apiKey}"
    r = requests.get(finalURL).json()

    topicoptions = ('Abortion', 'Abstinence', 'Affirmative Action', 'Alternative medicine',
                    'Animal Testing', 'Artificial intelligence', 'Assisted suicide', 'Atheism',
                    'Biofuels', 'Book banning', 'Capital punishment', 'Censorship', 'Obesity',
                    'Civil rights', 'Climate change', 'Cloning', 'Concealed weapons', 'Cryptocurrency')
    selectedTopic = st.selectbox('Choose a topic', topicoptions)

    if selectedTopic:
        listUrl = f"https://newsapi.org/v2/everything?q={selectedTopic}&apiKey={apiKey}"
        l = requests.get(listUrl).json()
        if l["status"] == "error":
            st.error("There was an Error Fetching the data, please Try Again Later")
            sys.exit()
        tot = l['totalResults']
        articles = l['articles']
        st.write(f"Number of articles found: {tot}")

        df = pd.DataFrame(articles)
        df['publishedAt'] = pd.to_datetime(df['publishedAt'])
        df['date'] = df['publishedAt'].dt.date
        counts_by_date = df['date'].value_counts().sort_index()
        st.line_chart(counts_by_date)

categories = ['technology', 'politics', 'sports', 'business',
              'entertainment', 'health', 'general']

# Define function to get sources for a given category
def get_sources(category):
    finalURL = f"https://newsapi.org/v2/top-headlines?country=us&category={category}" \
           f"&apiKey={apiKey}"
    r = requests.get(finalURL).json()
    if r["status"] == "error":
        st.error("There was an Error Fetching the data, please Try Again Later")
        sys.exit()
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
"Number of Articles per Source"
st.altair_chart(bar_chart, use_container_width=True)

# Create data frame for article sources per category
data = {}
for category in categories:
    data[category.title()] = get_sources(category)

df = pd.DataFrame(data)

# Display data frame and allow user to resize it
"Sources Per Category"
st.checkbox("Use container width", value=False, key="use_container_width")
st.dataframe(df, use_container_width=st.session_state.use_container_width)
