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

apiKey = '0a54baab3c394337aa46d1ea286cfb24'
categories = ['technology', 'politics', 'sports', 'business',
              'entertainment', 'health', 'general']

finalURL = f"https://newsapi.org/v2/top-headlines?country=us&category=technology" \
           f"&apiKey={apiKey}"
r = requests.get(finalURL).json()
articles = r['articles']

sources = []
for article in articles:
    print(article['source']['name'])
    sources += [article['source']['name']]
print(r)

finalURL = f"https://newsapi.org/v2/top-headlines?country=us&category=politics" \
           f"&apiKey={apiKey}"
rp = requests.get(finalURL).json()
articles = rp['articles']

sourcesp = []
for article in articles:
    print(article['source']['name'])
    sourcesp += [article['source']['name']]
print(rp)

finalURL = f"https://newsapi.org/v2/top-headlines?country=us&category=sports" \
           f"&apiKey={apiKey}"
rs = requests.get(finalURL).json()
articles = rs['articles']

sourcess = []
for article in articles:
    print(article['source']['name'])
    sourcess += [article['source']['name']]
print(rs)

finalURL = f"https://newsapi.org/v2/top-headlines?country=us&category=business" \
           f"&apiKey={apiKey}"
rb = requests.get(finalURL).json()
articles = rb['articles']

sourcesb = []
for article in articles:
    print(article['source']['name'])
    sourcesb += [article['source']['name']]
print(rb)

finalURL = f"https://newsapi.org/v2/top-headlines?country=us&category=entertainment" \
           f"&apiKey={apiKey}"
re = requests.get(finalURL).json()
articles = re['articles']

sourcese = []
for article in articles:
    print(article['source']['name'])
    sourcese += [article['source']['name']]
print(re)

finalURL = f"https://newsapi.org/v2/top-headlines?country=us&category=health" \
           f"&apiKey={apiKey}"
rh = requests.get(finalURL).json()
articles = rh['articles']

sourcesh = []
for article in articles:
    print(article['source']['name'])
    sourcesh += [article['source']['name']]
print(rh)

finalURL = f"https://newsapi.org/v2/top-headlines?country=us&category=general" \
           f"&apiKey={apiKey}"
rg = requests.get(finalURL).json()
articles = rg['articles']

sourcesg = []
for article in articles:
    print(article['source']['name'])
    sourcesg += [article['source']['name']]
print(rg)

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

arr = []
rows, cols = len(sources), 7
for i in range(rows):
    col = []
    for j in range(cols):
        col.append(0)
    arr.append(col)
print(arr)
cow = 0
for sub in arr:
    sub[0] = sources[cow]
    cow += 1

for i in arr:
    for c in i:
        print(c, end=" ")
    print()

print(arr)

"Article Sources per category"
@st.cache_data
def load_data():
    return pd.DataFrame(
        {
            "Technology": sources,
            "Politics": sourcesp,
            "Sports": sourcess,
            "Business": sourcesb,
            "Entertainment": sourcese,
            "Health": sourcesh,
            "General": sourcesg
        }
    )


# Boolean to resize the dataframe, stored as a session state variable
st.checkbox("Use container width", value=False, key="use_container_width")

df = load_data()

# Display the dataframe and allow the user to stretch the dataframe
# across the full width of the container, based on the checkbox value
st.dataframe(df, use_container_width=st.session_state.use_container_width)