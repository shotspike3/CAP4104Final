from datetime import date
import requests
import streamlit as st

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

st.header("Search")
# Store the initial value of widgets in session state

text_input = st.text_input(
    "Search",
    label_visibility="collapsed",
    placeholder="Search for an Article"
)

date1 = st.checkbox('Would you like to limit it by release date', key="disabled")

d = date.today

if date1:
    d = st.date_input("Will search for articles starting from this date", date.today())

if text_input and date1:
    searchUrl = f"https://newsapi.org/v2/everything?q={text_input}&from={d}&sortBy=relevancy" \
                f"&apiKey={apiKey}"
    s1 = requests.get(searchUrl).json()
    if s1["totalResults"] == 0:
        st.error("No Results where Found")
        st.info("Try Refining your search and use keywords")
    articles = s1['articles']
    for article in articles:
        st.header(article['title'])
        st.markdown(
            f"<span style='background-color:blue;padding:10px;border-radius:'> "
            f"Published at: {article['publishedAt']}</span>",
            unsafe_allow_html=True)
        # st.write(article['publishedAt'])
        if article['author']:
            st.write(article['author'])
        st.write(article['source']['name'])
        st.write(article['description'])
        st.write(article['url'])
        if article["urlToImage"]:
            st.image(article["urlToImage"])


elif text_input:
    searchUrl = f"https://newsapi.org/v2/everything?q={text_input}&sortBy=relevancy" \
                f"&apiKey={apiKey}"
    s1 = requests.get(searchUrl).json()
    if s1["totalResults"] == 0:
        st.error("No Results where Found")
        st.info("Try Refining your search and use keywords")
    articles = s1['articles']
    for article in articles:
        st.header(article['title'])
        st.markdown(
            f"<span style='background-color:blue;padding:10px;border-radius:'> "
            f"Published at: {article['publishedAt']}</span>",
            unsafe_allow_html=True)
        # st.write(article['publishedAt'])
        if article['author']:
            st.write(article['author'])
        st.write(article['source']['name'])
        st.write(article['description'])
        st.write(article['url'])
        if article["urlToImage"]:
            st.image(article["urlToImage"])
