import pandas as pd
import streamlit as st
import requests
import json

f = open('states.json')

data = json.load(f)

# import pycountry
# from api import apiKEY
apiKey = '0a54baab3c394337aa46d1ea286cfb24'


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
st.title('News Stats')
tab1, tab2 = st.tabs(["Top Articles in the Country", "Top Articles by State"])

with tab1:
    st.header("Recently in the US")

with tab2:
    states = []
    for data in data:
        states += [data["state"]]
    choseState = st.selectbox("Chose a state",
                              states)
    if choseState:
        stateUrl = f"https://newsapi.org/v2/everything?q={choseState}&sortBy=relevancy" \
                   f"&apiKey={apiKey}"
        s = requests.get(stateUrl).json()
        articles = s['articles']
        for article in articles:
            st.header(article['title'])
            if article["urlToImage"]:
                st.image(article["urlToImage"])
            st.write(article['publishedAt'])
            # st.write(article['publishedAt'])
            if article['author']:
                st.write(article['author'])
            st.write(article['source']['name'])
            st.write(article['description'])
            st.write(article['url'])
            
country = "us"
category = st.selectbox('Choose A News Category', ('technology', 'politics', 'sports', 'business',
                                                       'entertainment', 'health', 'general'))
       
if country and category:
    # asking user for country input, ex us for us news and turns it into alpha_2 through user method
    # country= pycountry.countries.get(name=user).alpha_2

    finalURL = f"https://newsapi.org/v2/top-headlines?country={country}&category={category}" \
               f"&apiKey={apiKey}"
    r = requests.get(finalURL).json()
    print(r["articles"][0])
    print(r)
    articles = r['articles']
    for article in articles:
        st.header(article['title'])
        st.image(article["urlToImage"])
        st.write(article['publishedAt'])
        if article['author']:
            st.write(article['author'])
        st.write(article['source']['name'])
        st.write(article['description'])
        st.write(article['url'])
        

