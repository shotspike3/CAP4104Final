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

apiKey = '0a54baab3c394337aa46d1ea286cfb24'

finalURL = f"https://newsapi.org/v2/top-headlines?country=us&category=technology" \
           f"&apiKey={apiKey}"
r = requests.get(finalURL).json()
articles = r['articles']
sources = []
for article in articles:
    print(article['source']['name'])
    sources += [article['source']['name']]
print(r)

source_count = {}
bruh = []
for word in sources:
    if word in source_count:
        source_count[word] += 1
    else:
        source_count[word] = 1


bruh += source_count.values()

print(source_count)
print(len(sources))
print(len(bruh))

"Number of articles per category"
df = pd.DataFrame({
"Sources": [sources],
"Number of Articles":  [bruh],
"Categories": [sources]
})

bar_chart = alt.Chart(df).mark_bar().encode(
    x="Categories:O",
    y="Number Of articles:Q",
    color="Sources:N"
)
st.altair_chart(bar_chart, use_container_width=True)

df