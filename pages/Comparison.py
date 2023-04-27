import streamlit as st
import pandas as pd
import requests
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
f = open('pages/states.json')

data = json.load(f)

apiKey = '51a9947ce63a403d8eca7e3a3bc0ece6'


country = "us"
if country:
    finalURL = f"https://newsapi.org/v2/top-headlines?country={country}&apiKey=0a54baab3c394337aa46d1ea286cfb24"
    r = requests.get(finalURL).json()

    states = []
    for data in data:
        states += [data["state"]]
    stateoptions = st.multiselect('select by state', states)

    if stateoptions:
        stateUrl = f"https://newsapi.org/v2/everything?q={stateoptions}" \
                       f"&apiKey={apiKey}"
        s = requests.get(stateUrl).json()
        articles = s['articles']
        list = st.selectbox('Choose a topic',
                            ('the', 'Abortion', 'Abstinence', 'Affirmative Action', 'Alternative medicine',
                             'Animal Testing', 'Artificial intelligence', 'Assisted suicide', 'Atheism',
                             'Biofuels', 'Book banning', 'Capital punishment', 'Censorship', 'Obesity',
                             'Civil rights', 'Climate change', 'Cloning', 'Concealed weapons', 'Cryptocurrency'))

        if list:
            listUrl = f"https://newsapi.org/v2/everything?q={list}&apiKey={apiKey}"
            l = requests.get(listUrl).json()
            finalURL = f"https://newsapi.org/v2/top-headlines?country={country}&apiKey=0a54baab3c394337aa46d1ea286cfb24"
            r = requests.get(finalURL).json()
            tot = l['totalResults']
            total =l['articles']
            print(tot)
            st.write(tot)

# df = pd.DataFrame
#     # map element
#     # a map of news by state
# df = pd.read_csv('news-articles.csv',
#                  ['title', 'article', 'publishdate'])
#
# df.columns = ['Source', 'Topic', 'Content']
# st.map(df)

st.title("button")
result = st.button("click me")
st.write(result)
if result:
    st.write(":success:")
st.title("welcome")
st.write("to this page")
# dataframe
df = pd.DataFrame({'first': [1, 2], 'second': [6, 7]})
st.sidebar.write(df)
df
st.sidebar.line_chart(df)
# checkbox widget
if st.checkbox("show table..."):
    df

    # selectbox
    opt = st.selectbox('which select')
    if opt == 'None':
        st.write("select val")
    else:
        st.write('selected', opt)

# slider
st.title("sliders")
st.subheader("news notification preferneces")
y = st.slider('select news inbox notification prefernece level from a scale of 0-10', value=50)
st.write("slider number: ", y)
# select-slider
news_options = ['politics', 'popular media']
news = st.select_slider("choose category")
options = news_options
st.write("selected:", news)

# radio button
newsr_radio = ['HomePage', 'FeaturedNews']
newsr = st.radio('Selected Stories', newsr_radio, index=1)
st.write("the 'news' returns", newsr)
if newsr['HomePage']:
    # if newsr='HomePage':
    st.subheader("welcome")
    st.write("hi")
else:
    st.subheader("hello")
    st.write("hi")

# success message
st.success('success')

# info box
st.info('this allows you to search for news stories based off regional and language preferences')

# error
st.error('please select your region of choice using the drop down menu')
#
# print(r)
